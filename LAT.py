import argparse
import os
from datetime import datetime
from LAT_reader import ReadLHEF
from LAT_getter import LAT_getter
from LAT_plotmaker import PlotData, PlotDataDouble

# LHEF ANALYSER TOOL

parser = argparse.ArgumentParser(description='LHEF Analyser Tool')
parser.add_argument('file', metavar='PATH', help='LHEF file path')

parser.add_argument('--save', dest='save', action='store_true', default=False, help='saves the generated plots')
parser.add_argument('--makeplots', dest='make_plots', action='store_true', help='creates all plots')

parser.add_argument('-se', 
                    dest='system_energy', action='store_true', help='plots the system\'s energy')
parser.add_argument('-sm',
                    dest='system_mass', action='store_true', help='plots the system\'s mass')
parser.add_argument('-sl',
                    dest='system_loss', action='store_true', help='plots the system\'s relative energy loss')
parser.add_argument('-pe',
                    dest='particles_energy', action='store_true', help='plots the product\'s energy')
parser.add_argument('-tm',
                    dest='transverse_momentum', action='store_true', help='plots the product\'s transverse momentum')
parser.add_argument('-th',
                    dest='theta', action='store_true', help='plots the product\'s theta distribution')
parser.add_argument('-et',
                    dest='eta', action='store_true', help='plots the product\'s eta distribution')
parser.add_argument('-bl',
                    dest='beam_loss', action='store_true', help='plots the beam relative energy loss distribution')

parser.add_argument('--acoplanarity',
                    dest='acoplanarity', action='store_true', help='plots the acoplanarity')
parser.add_argument('--rapidity',
                    dest='y', action='store_true', default=False, 
                    help='use rapidity instead of pseudorapidity in relative energy loss calculation')

# ========================================================

args = parser.parse_args()

p = ReadLHEF(args.file)
g = LAT_getter(p)

# getting the labels and bins configuration
labels, bins = g.Control()

# if the plots are going to be saved, the filename is initialized
file_start = ''
if args.save:
    if args.make_plots:
        fdate = datetime.today().strftime(labels['id'] + '_%Y_%m_%d_%H_%M_%S/')
        os.mkdir(fdate)
        file_start = fdate + labels['id']
    else:
        file_start = labels['id']

# ========================================================

PASS = False

if args.make_plots:
    PASS = True

if args.system_energy or PASS:
    PlotData(
        g.Energy(2), labels['se'], bins['se'], args.save, file_start + '_se.pdf')

if args.system_mass or PASS:
    PlotData(
        g.Mass(2), labels['sm'], bins['sm'], args.save, file_start + '_sm.pdf')

if args.system_loss or PASS:
    a, c = map(list,zip(*g.SystemLoss(args.y)))

    PlotDataDouble(
        a, c, labels['p_'], labels['sl'], bins['sl'], args.save, file_start + '_sl.pdf', True)

if args.particles_energy or PASS:
    PlotDataDouble(
        g.Energy(3), g.Energy(4), labels['p_'], labels['pe'], bins['pe'], args.save, file_start + '_pe.pdf')

if args.transverse_momentum or PASS:
    PlotDataDouble(
        g.TransverseMomentum(3), g.TransverseMomentum(4), labels['p_'], labels['tm'], bins['tm'], args.save, file_start + '_tm.pdf')

if args.theta or PASS:
    PlotDataDouble(
        g.Theta(3), g.Theta(4), labels['p_'], labels['th'], bins['th'], args.save, file_start + '_th.pdf', False, True)

if args.eta or PASS:
    PlotDataDouble(
        g.Eta(3), g.Eta(4), labels['p_'], labels['et'], bins['et'], args.save, file_start + '_et.pdf', False, True)

if args.beam_loss or PASS:
    PlotDataDouble(
        g.ProtonLoss(0), g.ProtonLoss(1), labels['p_'], labels['bl'], bins['bl'], args.save, file_start + '_bl.pdf')

if args.acoplanarity:
    print('Not implemented yet!')
