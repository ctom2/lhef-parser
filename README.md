# Les Houches Event File Analyser Tool

Simple LHEF parser written in Python that can be used without ROOT was created for [SuperChic](https://superchic.hepforge.org) Monte Carlo generator output file analysis. Its main purpose is to plot energy, mass, relative energy loss, transverse momentum and acoplanarity distributions of the particles participating in the following productions:
* γγ → γγ
* γγ → µµ
* γγ → ee
* Axion-Like Particle production

The histogram production is handled by the following terminal commands:

```
positional arguments:
  PATH            LHEF file path

optional arguments:
  -h, --help      show this help message and exit
  --save          saves the generated plots
  --makeplots     creates all plots
  -se             plots the system's energy
  -sm             plots the system's mass
  -sl             plots the system's relative energy loss
  -pe             plots the product's energy
  -tm             plots the product's transverse momentum
  -th             plots the product's theta distribution
  -et             plots the product's eta distribution
  -bl             plots the beam relative energy loss distribution
  --acoplanarity  plots the acoplanarity
  --rapidity      use rapidity instead of pseudorapidity in relative energy
                  loss calculation
```

## Author
Tomáš Chobola, 2020
