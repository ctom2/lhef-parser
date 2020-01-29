SM_bins = {
    'se' : (5, 100, 1),
    'sm' : (5, 50, 0.5),
    'sl' : (0, 0.05, 0.0005),
    'pe' : (0, 50, 0.5),
    'tm' : (0, 25, 0.25),
    'th' : (0, 3, 0.03),
    'et' : (-2.5, 2.5, 0.05),
    'bl' : (0, 0.01, 0.0001)
}

ALP_bins = {
    'se' : (1000, 2500, 15),
    'sm' : (999, 1001, 0.1),
    'sl' : (0, 0.8, 0.01),
    'pe' : (0, 2000, 20),
    'tm' : (100, 575, 5),
    'th' : (0, 3, 0.03),
    'et' : (-2.5, 2.5, 0.05),
    'bl' : (0, 0.4, 0.004)
}

gg = {
    'id' : 'gg',
    'p_' : 'Photon',
    'se' : 'Photon pair energy $E_{\gamma\gamma}$ [GeV]',
    'sm' : 'Photon pair mass $M_{\gamma\gamma}$ [GeV]',
    'sl' : 'Photon pair relative energy loss $ξ_{\gamma\gamma}$',
    'pe' : 'Photon 1 energy $E_{\gamma_1}$, photon 2 energy $E_{\gamma_2}$ [GeV]',
    'tm' : 'Photon 1 $p_{T_{\gamma_1}}$, electron 2 $p_{T_{\gamma_2}}$ [GeV]',
    'th' : 'Photon 1 $θ_{\gamma}$, photon 2 $θ_{\gamma_2}$',
    'et' : 'Photon 1 $η_{\gamma_1}$, photon 2 $η_{\gamma_2}$',
    'bl' : 'Proton 1 $ξ_{p_1}$, proton 2 $ξ_{p_2}$'
}

mm = {
    'id' : 'mm',
    'p_' : 'Muon',
    'se' : 'Muon pair energy $E_{\mu\mu}$ [GeV]',
    'sm' : 'Muon pair mass $M_{\mu\mu}$ [GeV]',
    'sl' : 'Muon pair relative energy loss $ξ_{\mu\mu}$',
    'pe' : 'Muon 1 energy $E_{\mu_1}$, Muon 2 energy $E_{\mu_2}$ [GeV]',
    'tm' : 'Muon 1 $p_{T_{e_1}}$, electron 2 $p_{T_{e_2}}$ [GeV]',
    'th' : 'Muon 1 $θ_{\mu}$, Muon 2 $θ_{\mu_2}$',
    'et' : 'Muon 1 $η_{\mu_1}$, Muon 2 $η_{\mu_2}$',
    'bl' : 'Proton 1 $ξ_{p_1}$, proton 2 $ξ_{p_2}$'
}

ee = {
    'id' : 'ee',
    'p_' : 'Electron',
    'se' : 'Electron pair energy $E_{ee}$ [GeV]',
    'sm' : 'Electron pair mass $M_{ee}$ [GeV]',
    'sl' : 'Electron pair relative energy loss $ξ_{ee}$',
    'pe' : 'Electron 1 energy $E_{e_1}$, electron 2 energy $E_{e_2}$ [GeV]',
    'tm' : 'Electron 1 $p_{T_{e_1}}$, electron 2 $p_{T_{e_2}}$ [GeV]',
    'th' : 'Electron 1 $θ_{e_1}$, electron 2 $θ_{e_2}$',
    'et' : 'Electron 1 $η_{e_1}$, electron 2 $η_{e_2}$',
    'bl' : 'Proton 1 $ξ_{p_1}$, proton 2 $ξ_{p_2}$'
}

alp = {
    'id' : 'alp',
    'p_' : 'Photon',
    'se' : 'Axion-Like Particle energy $E_{ALP}$ [GeV]',
    'sm' : 'Axion-Like Particle mass $M_{ALP}$ [GeV]',
    'sl' : 'Axion-Like Particle relative energy loss $ξ_{ALP}$',
    'pe' : 'Photon 1 energy $E_{\gamma_1}$, photon 2 energy $E_{\gamma_2}$ [GeV]',
    'tm' : 'Photon 1 $p_{T_{\gamma_1}}$, photon 2 $p_{T_{\gamma_2}}$ [GeV]',
    'th' : 'Photon 1 $θ_{\gamma_1}$, photon 2 $θ_{\gamma_2}$',
    'et' : 'Photon 1 $η_{\gamma_1}$, photon 2 $η_{\gamma_2}$',
    'bl' : 'Proton 1 $ξ_{p_1}$, proton 2 $ξ_{p_2}$'
}