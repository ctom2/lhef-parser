import re
from typing import NamedTuple
from matplotlib import pyplot as plt

EVENT_TAG = '<event>'
INIT_TAG = '<init>'
INIT_END_TAG = '</init>'
FILE_END_TAG = '</LesHouchesEvents>'

prefixes = {'eV' : 1, 
            'keV' : 10**3,
            'MeV' : 10**6,
            'GeV' : 10**9,
            'TeV' : 10**12,
            'PeV' : 10**15}

class Parameters(NamedTuple):
    id_a : int # IDBMUP(1)
    id_b : int # IDBMUP(2)
    energy_a : float # EBMUP(1)
    energy_b : float # EBMUP(2)
    pdfgup_a : int # PDFGUP(1)
    pdfgup_b : int # PDFGUP(2)
    pdfsup_a : int # PDFSUP(1)
    pdfsup_b : int # PDFSUP(2)
    weight : int # IDWTUP
    nprup : int # NPRUP
    xsecup : float # XSECUP(MAXPUP)
    xerrup : float # XERRUP(MAXPUP)
    xmaxup : float # XMAXUP(MAXPUP)
    lprup : float # LPRUP(MAXPUP)

class Particle(NamedTuple):
    pdgid : int # IDUP
    status : int # ISTUP
    mother_a : int # MOTHUP(1)
    mother_b : int # MOTHUP(2)
    color_a : int # ICOLUP(1)
    color_b : int # ICOLUP(2)
    px : float # PUP(1)
    py : float # PUP(2)
    pz : float # PUP(3)
    E : float # PUP(4)
    M : float # PUP(5)
    lifetime : float # VTIMUP
    spin : float # SPINUP

class Event(NamedTuple):
    nparticles : int # NUP
    subprocess : int # IDPRUP
    weight : float # XWGTUP
    scale : float # SCALUP
    qedcoupling : float # AQEDUP 
    qcdcoupling : float # AQCDUP
    particles : list # List of particles in the event

class Process(NamedTuple):
    init : Parameters
    events : list

def ReadLHEF(filepath): # Reads LHEF file and stores the information in according classes
    fp = open(filepath)
    init = []
    line = fp.readline()

    while line.strip() != INIT_TAG: line = fp.readline()

    line = fp.readline()
    while line.strip() != INIT_END_TAG: # Reading the initialisation parameters
        line = re.sub('\s+', ' ', line).strip().split(' ')
        line = [float(i) for i in line]
        init = init + line
        line = fp.readline()

    p = Process(Parameters(*init),[])

    line = fp.readline()
    while line.strip() != FILE_END_TAG: # Reading the events
        if line.strip() == EVENT_TAG:
            line = fp.readline()
            line = re.sub('\s+', ' ', line).strip().split(' ')
            line[0:2] = map(int, line[0:2])
            line[2:6] = map(float, line[2:6])
            e = Event(*line, [])

            for i in range(e.nparticles):
                line = fp.readline()
                line = re.sub('\s+', ' ', line).strip().split(' ')
                line[0:6] = map(int, line[0:6])
                line[6:13] = map(float, line[6:13])
                line[6] = line[6] * 10**9 # from GeV to eV
                line[7] = line[7] * 10**9 # from GeV to eV
                line[8] = line[8] * 10**9 # from GeV to eV
                line[9] = line[9] * 10**9 # from GeV to eV
                line[10] = line[10] * 10**9 # from GeV to eV
                e.particles.append(Particle(*line))

            p.events.append(e)

        line = fp.readline()

    return p

def CreateHistogram(process, particles, unit, prefix, bins): # Creates histogram
    data = []
    for event in process.events:
        for i in particles:
            data.append(getattr(event.particles[i], unit))

    data = [i / prefixes[prefix] for i in data]

    plt.hist(data, bins=bins, histtype='step', color='black')
    label = unit + ' [' + prefix + ']'
    plt.xlabel(label)
    plt.ylabel('count')
    plt.xticks(rotation='vertical')
    plt.show()