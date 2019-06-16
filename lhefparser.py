import re
from typing import NamedTuple

EVENT_TAG = '<event>'
INIT_TAG = '<init>'
INIT_END_TAG = '</init>'
FILE_END_TAG = '</LesHouchesEvents>'

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
    e : float # PUP(4)
    m : float # PUP(5)
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

def ReadLHEF(filepath):
    fp = open(filepath)
    init = []
    line = fp.readline()

    while line.strip() != INIT_TAG: line = fp.readline()

    line = fp.readline()
    while line.strip() != INIT_END_TAG: # Reading the initialisation parameters
        line = re.sub('\s+', ' ', line).strip().split(' ')
        init = init + line
        line = fp.readline()

    p = Process(Parameters(*init),[])

    line = fp.readline()
    while line.strip() != FILE_END_TAG: # Reading the events
        if line.strip() == EVENT_TAG:
            line = fp.readline()
            line = re.sub('\s+', ' ', line).strip().split(' ')
            line = [float(i) for i in line]
            line[0], line[1] = int(line[0]), int(line[1])
            e = Event(*line, [])

            for i in range(e.nparticles):
                line = fp.readline()
                line = re.sub('\s+', ' ', line).strip().split(' ')
                e.particles.append(Particle(*line))

            p.events.append(e)

        line = fp.readline()

    return p

p = ReadLHEF('evrecout.dat')