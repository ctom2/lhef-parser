import re
from typing import NamedTuple
from matplotlib import pyplot as plt
from matplotlib.ticker import ScalarFormatter,AutoMinorLocator
import matplotlib as mpl
import numpy as np
from math import exp
import math
import os

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# PARSER

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

    init[2] = init[2] * 10**9 # from GeV to eV
    init[3] = init[3] * 10**9 # from GeV to eV

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

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# ANALYSING DATA

class Analyser:
    def __init__(self, filename):
        self.p = ReadLHEF(filename)
        self.energy_a = self.p.init.energy_a
        self.energy_b = self.p.init.energy_b
        self.events = self.p.events

    def GetPairEnergy(self):
        pair_energy = []
        for event in self.p.events: pair_energy.append(event.particles[2].E / 10**9)

        return pair_energy

    def GetPairMass(self):
        pair_mass = []
        for event in self.p.events: pair_mass.append(event.particles[2].M / 10**9)

        return pair_mass

    def GetPairLoss(self):
        pair_loss = []
        pair_loss_zoom = []

        for event in self.p.events:
            p_z_sum = event.particles[2].pz

            p = (event.particles[2].px**2 + event.particles[2].py**2 + event.particles[2].pz**2)**0.5

            cos_theta = p_z_sum/p
            theta = math.acos(cos_theta)
            eta = -math.log(math.tan(theta/2))

            x = event.particles[2].M/(12000000000000 * math.exp(eta))
            pair_loss.append(x)

            if x >= 0.02 and x <= 0.1:
                pair_loss_zoom.append(x)

        return pair_loss, pair_loss_zoom

    # calculated only with p_x and p_y
    def GetAcoplanarity(self):
        aco_array = []
        # aco = 0
        
        for event in self.p.events:
            p1x = event.particles[3].px
            p1y = event.particles[3].py

            p2x = event.particles[4].px
            p2y = event.particles[4].py

            p1 = (p1x**2 + p1y**2)**0.5
            p2 = (p2x**2 + p2y**2)**0.5

            angle = math.acos((p1x*p2x + p1y*p2y)/(p1*p2))
            acoplanarity = 1 - abs(angle/math.pi)

            # if acoplanarity < 0.01:
            #     aco = aco + 1

            aco_array.append(acoplanarity)

        return aco_array

    def GetStartElement1Energy(self):
        energy = []
        for event in self.p.events: energy.append(event.particles[3].E / 10**9)

        return energy

    def GetStartElement1Theta(self):
        theta = []
        for event in self.p.events:
            p_z_sum = event.particles[3].pz
            p = (event.particles[3].px**2 + event.particles[3].py**2 + event.particles[3].pz**2)**0.5
            cos_theta = p_z_sum/p

            theta.append(math.acos(cos_theta))

        return theta

    def GetStartElement1Eta(self):
        eta = []
        for event in self.p.events: 
            p_z_sum = event.particles[3].pz
            p = (event.particles[3].px**2 + event.particles[3].py**2 + event.particles[3].pz**2)**0.5
            cos_theta = p_z_sum/p
            theta = math.acos(cos_theta)
            
            eta.append(-math.log(math.tan(theta/2)))

        return eta

    def GetStatElement1Pt(self):
        pt = []
        for event in self.p.events: pt.append(((event.particles[3].px ** 2 + event.particles[3].py ** 2) ** 0.5) / 10**9)

        return pt

    def GetStartElement2Energy(self):
        energy = []
        for event in self.p.events: energy.append(event.particles[4].E / 10**9)

        return energy

    def GetStartElement2Theta(self):
        theta = []

        for event in self.p.events:
            p_z_sum = event.particles[4].pz
            p = (event.particles[4].px**2 + event.particles[4].py**2 + event.particles[4].pz**2)**0.5
            cos_theta = p_z_sum/p

            theta.append(math.acos(cos_theta))

        return theta

    def GetStartElement2Eta(self):
        eta = []
        for event in self.p.events: 
            p_z_sum = event.particles[4].pz
            p = (event.particles[4].px**2 + event.particles[4].py**2 + event.particles[4].pz**2)**0.5
            cos_theta = p_z_sum/p
            theta = math.acos(cos_theta)
            
            eta.append(-math.log(math.tan(theta/2)))

        return eta

    def GetStatElement2Pt(self):
        pt = []
        for event in self.p.events: pt.append(((event.particles[4].px ** 2 + event.particles[4].py ** 2) ** 0.5) / 10**9)

        return pt

    def GetBeam1Loss(self):
        loss = []
        for event in self.p.events: loss.append((self.energy_a - event.particles[0].E)/self.energy_a)

        return loss

    def GetBeam2Loss(self):
        loss = []
        for event in self.p.events: loss.append((self.energy_b - event.particles[1].E)/self.energy_b)

        return loss

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # WORKING WITH DATA

    def GetSingleTag(self, lowerBound, upperBound):
        single_tag = []
        for event in self.p.events:
            x = ((self.energy_a - event.particles[0].E)/self.energy_a)
            y = ((self.energy_b - event.particles[1].E)/self.energy_b)

            if (x >= lowerBound and x <= upperBound) or (y >= lowerBound and y <= upperBound):
                single_tag.append(x)

        return single_tag

    def GetDoubleTag(self, lowerBound, upperBound):
        double_tag = []
        for event in self.p.events:
            x = ((self.energy_a - event.particles[0].E)/self.energy_a)
            y = ((self.energy_b - event.particles[1].E)/self.energy_b)

            if (x >= lowerBound and x <= upperBound) and (y >= lowerBound and y <= upperBound):
                double_tag.append(x)

        return double_tag

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # MAKING PLOTS

    def PlotData(self, data, start, stop, step, title='test', xlabel='test', save=False, path='./', name='plot.pdf'):
        plt.rcParams['xtick.labelsize'] = 16
        plt.rcParams['ytick.labelsize'] = 16

        plt.rcParams['font.size'] = 15
        plt.rcParams['figure.autolayout'] = True
        plt.rcParams['figure.figsize'] = 7.2, 6.2
        plt.rcParams['axes.titlesize'] = 16
        plt.rcParams['axes.labelsize'] = 17
        plt.rcParams['lines.linewidth'] = 2
        plt.rcParams['lines.markersize'] = 6
        plt.rcParams['legend.fontsize'] = 13
        plt.rcParams['mathtext.fontset'] = 'stix'
        plt.rcParams['font.family'] = 'STIXGeneral'

        fig, ax = plt.subplots()

        ax.yaxis.set_major_formatter(ScalarFormatter())
        ax.yaxis.major.formatter._useMathText = True
        ax.yaxis.set_minor_locator(AutoMinorLocator(5))
        ax.xaxis.set_minor_locator(AutoMinorLocator(5))

        plt.hist(data, color='black', linewidth=1.8, histtype='step', align='mid', bins=np.arange(start=start, stop=stop, step=step))
        plt.xlabel(xlabel, horizontalalignment='right', x=1.0)
        plt.ylabel('Events')
        plt.title(title, horizontalalignment='right', x=1.0)

        if save == True: 
            plt.savefig(os.path.join(path,name),dpi=200)
        else: 
            plt.show()
