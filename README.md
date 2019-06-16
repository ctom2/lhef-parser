# Les Houches Event File parser

Simple LHEF parser written in Python that can be used without ROOT.

The events are read into memory as shown on the diagram.

```
Process
├── Init
└── Events
    ├── Event(0)
    │   └── Particles
    │       ├── Particle(0)
    │       ├── Particle(1)
    │       ...
    │       └── Particle(x)
    ├── Event(1)
    │   └── Particles
    │       ├── Particle(0)
    │       ├── Particle(1)
    │       ...
    │       └── Particle(x)
    ├── Event(2)
    │   └── Particles
    │       ├── Particle(0)
    │       ├── Particle(1)
    │       ...
    │       └── Particle(x)
    ...
    └── Event(n)
        └── Particles
            ├── Particle(0)
            ├── Particle(1)
            ...
            └── Particle(x)
```

For creating histograms the package includes method `CreateHistogram`. The method requires five parameters:\
`process` - class Process that is returned by the `ReadLHEF` function\
`particles` - particles used for creating the distribution, passed as list (e.g. [3,4])\
`unit` - unit used for creating the distribution, passed as string ('px', 'py', 'pz', 'E', 'M')\
`prexif` - unit conversion, parameter is passed as string ('eV', 'keV', 'MeV', ...)\
`bins` - number of bins

## Author
Tomáš Chobola, 2019
