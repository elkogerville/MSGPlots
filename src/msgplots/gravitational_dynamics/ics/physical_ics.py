
from amuse.datamodel import Particle, Particles
from amuse.units import (
    constants as c,
    nbody_system as ns,
    units as au
)

def generate_earth_moon_initial_conditions(self):
    """
    Earth and moon initial conditions taken from JPL Ephemeris.

    JPL Ephemeris, Pasadena, USA, Horizons System

        * Start time        : A.D. 2026-Jan-01 00:00:00.0000 TDB
        * Stop  time        : A.D. 2026-Jan-01 00:01:00.0000 TDB
        * Coordinate Center : Solar System Barycenter
    """
    p = Particles(2)

    p[0].name = 'Earth'
    p[0].mass = 5.97219e24 | au.kg
    p[0].radius = 6371.01 | au.km
    p[0].xi = 0.3308
    p[0].kf = 0.933
    p[0].tau = 60. | au.s
    p[0].wx = 0.0 | au.rad/au.s
    p[0].wy = 0.0 | au.rad/au.s
    p[0].wz = 0.0 | au.rad/au.s
    p[0].x = -2.653100241556548E+07 | au.km
    p[0].y = 1.439468995740296E+08 | au.km
    p[0].z = 1.080681311843544E+04 | au.km
    p[0].vx = -2.977650610770464E+01 | au.kms
    p[0].vy = -5.395962660572101E+00 | au.kms
    p[0].vz = 1.753836198843395E-04 | au.kms

    p[1].name = 'Moon'
    p[1].mass = 7.349e22 | au.kg
    p[1].radius = 1737.53 | au.km
    p[1].xi = 0.394
    p[1].kf = 0.4
    p[1].tau = 60. | au.s
    p[1].wx = 0.0 | au.rad/au.s
    p[1].wy = 0.0 | au.rad/au.s
    p[1].wz = 0.0 | au.rad/au.s
    p[1].x = -2.638667668807356E+07 | au.km
    p[1].y = 1.442762954049252E+08 | au.km
    p[1].z = 4.255978946162760E+04 | au.km
    p[1].vx = -3.078082024537686E+01 | au.kms
    p[1].vy = -4.975097451815738E+00 | au.kms
    p[1].vz = 5.760594917691098E-03 | au.kms

    p.move_to_center()

    return p
