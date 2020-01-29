import LAT_formulas as form
import LAT_groups as groups

class LAT_getter:
    # input parameter is the process class from LAT_reader.py
    def __init__(self, p):
    # proton beam energies
        self.energy_a = p.init.energy_a
        self.energy_b = p.init.energy_b
        
        self.events = p.events
        # sqrt(s) = 13 GeV
        self.sqrt_s = 13000

    # returns labels for plots and bins configurations
    def Control(self):
        # generated system PDGID
        sysid = self.events[0].particles[2].pdgid
        # product particle PDGID
        pdgid = self.events[0].particles[3].pdgid

        # ALP system
        if sysid is 90:
            return groups.alp, groups.ALP_bins
        # SM system
        else:
            if pdgid is 22:
                # photon
                return groups.gg, groups.SM_bins
            elif pdgid is 13:
                # muon
                return groups.mm, groups.SM_bins
            elif pdgid is 11:
                # electron
                return groups.ee, groups.SM_bins

    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

    # returns the energy component based on index i
    def Energy(self, i):
        return [event.particles[i].E for event in self.events]

    # returns the mass component based on index i
    def Mass(self, i):
        return [event.particles[i].M for event in self.events]

    # returns the relative energy loss of the two product particles
    def SystemLoss(self, rapidity=False):
        if rapidity is False:
            return [form.XiEta(event, self.sqrt_s) for event in self.events]
        else:
            return [form.XiY(event, self.sqrt_s) for event in self.events]

    # returns the relative energy loss of a beam proton
    def ProtonLoss(self, i):
        if i is 0: 
            return [form.XiProton(event, i, self.energy_a) for event in self.events]
        elif i is 1: 
            return [form.XiProton(event, i, self.energy_b) for event in self.events]

    # returns the theta
    def Theta(self, i):
        return [form.Theta(event, i) for event in self.events]

    # returns the eta
    def Eta(self, i):
        return [form.Eta(event, i) for event in self.events]

    # returns the transverse momentum of chosen particle
    def TransverseMomentum(self, i):
        return [form.TransverseMomentum(event, i) for event in self.events]

    # returns the acoplanarity
    def Acoplanarity(self):
        return [form.Acoplanarity(event) for event in self.events]