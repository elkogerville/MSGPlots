
from amuse.datamodel import Particles
from amuse.ext.orbital_elements import generate_binaries
from amuse.units import units as au


def generate_HD80606b_system(self):
    """
    Initial conditions for the exoplanet system
    HD80606b. Initial conditions courtesy of
    Dr. Tjarda Boekholt.
    """
    HD80606 = Particles(2)
    star, planet = generate_binaries(
        primary_mass=2.0088092e30 | au.kg,
        secondary_mass=7.7459434e27 | au.kg,
        semi_major_axis=0.455 | au.au,
        eccentricity=0.9330
    )
    HD80606[0].name = 'HD80606'
    HD80606[0].mass = star.mass
    HD80606[0].radius = 702455.0 | au.km
    HD80606[0].x = star.x.as_quantity_in(au.km)
    HD80606[0].y = star.y.as_quantity_in(au.km)
    HD80606[0].z = star.z.as_quantity_in(au.km)
    HD80606[0].vx = star.vx.as_quantity_in(au.kms)
    HD80606[0].vy = star.vy.as_quantity_in(au.kms)
    HD80606[0].vz = star.vz.as_quantity_in(au.kms)
    HD80606[0].wx = 0.0 | 1 / au.s
    HD80606[0].wy = 0.0 | 1 / au.s
    HD80606[0].wz = 2.97188607137e-6 | 1 / au.s

    HD80606[1].name = 'HD80606b'
    HD80606[1].mass = planet.mass
    HD80606[1].radius = 68488.3446 | au.km
    HD80606[1].x = planet.x.as_quantity_in(au.km)
    HD80606[1].y = planet.y.as_quantity_in(au.km)
    HD80606[1].z = planet.z.as_quantity_in(au.km)
    HD80606[1].vx = planet.vx.as_quantity_in(au.kms)
    HD80606[1].vy = planet.vy.as_quantity_in(au.kms)
    HD80606[1].vz = planet.vz.as_quantity_in(au.kms)
    HD80606[1].wx = 0.0 | 1 / au.s
    HD80606[1].wy = 0.0 | 1 / au.s
    HD80606[1].wz = 0.000145444104333 | 1 / au.s

    return HD80606


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
