import astropy.units as u
import numpy as np
import gala.potential as gp
import gala.dynamics as gd
from gala.dynamics import mockstream as ms
from gala.units import galactic

import matplotlib.pyplot as plt
plt.ion()

# Following tutorial https://gala.adrian.pw/en/latest/dynamics/mockstreams.html

# Milky Way potential
pot = gp.BovyMWPotential2014()
H = gp.Hamiltonian(pot)

# Progenitor coordinates
# Example, eventually want to think about how we will sample over positions and velocities 
prog_w0 = gd.PhaseSpacePosition(pos=[10, 0, 0.] * u.kpc,
                                vel=[0, 170, 0.] * u.km/u.s)

# Distribution function - determines how particles are stripped from progenitor
df = ms.FardalStreamDF()

# Will also sample over prog masses
prog_mass = 2.5E4 * u.Msun

# Generate stream
gen = ms.MockStreamGenerator(df, H)

# Run stream
# Maybe sample over disruption times - default model releases particles every timestep, not realistic disruption rate
stream, prog = gen.run(prog_w0, prog_mass,
                       dt=1 * u.Myr, n_steps=1000)


# Plot stream
stream.plot(['x', 'y'])  