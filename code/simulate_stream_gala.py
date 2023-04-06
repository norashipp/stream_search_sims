import astropy.units as u
import astropy.coordinates as coord
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

# Distribution function - determines how particles are stripped from progenitor
df = ms.FardalStreamDF()

# Progenitor coordinates
# Example, eventually want to think about how we will sample over positions and velocities
prog_w0 = gd.PhaseSpacePosition(pos=[10, 0, 0.] * u.kpc,
                                vel=[0, 170, 0.] * u.km / u.s)

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

# convert to ra, dec
stream_c = stream.to_coord_frame(coord.ICRS)
prog_c = prog.to_coord_frame(coord.ICRS)

# Next steps:
# -  Mock observations: sample isochrone, convolve with DES photometric uncertainties
# -  Inject into DES data (or DECaLS DR10): apply isochrone selection, bin into healpix, add to maps
# -  Decide sampling: over progenitor coordinates, masses, stripping times, isochrone parameters
# -  Decide on stripping model (every time step?)