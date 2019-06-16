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


## Author
Tomáš Chobola, 2019
