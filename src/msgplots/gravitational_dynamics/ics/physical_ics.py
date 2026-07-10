
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


def generate_jupiter_io_system():
    """
    Ephemeris Pasadena, USA, Horizons

    JPL Ephemeris, Pasadena, USA, Horizons System

        * Start time        : A.D. 2026-Jan-01 00:00:00.0000 TDB
        * Stop  time        : A.D. 2026-Jan-01 00:01:00.0000 TDB
        * Coordinate Center : Solar System Barycenter
    """
    system = Particles(2)

    system[0].name = 'Jupiter'
    system[0].mass = 1898.6e24 | au.kg
    system[0].radius = 6371.01 | au.km
    system[0].x = -2.538781102425539e8 | au.km
    system[0].y = 7.365225847926259e8 | au.km
    system[0].z = 2.626628058868796e6 | au.km
    system[0].vx = -1.250707427525374e1 | au.kms
    system[0].vy = -3.638417682823274 | au.kms
    system[0].vz = 2.949797151579847e-1 | au.kms

    system[1].name = 'Io'
    system[1].mass = 893193797311089e8 | au.kg
    system[1].radius = 1821.6 | au.km
    system[1].x = -2.535070263728397e8 | au.km
    system[1].y = 7.363212379813337e8 | au.km
    system[1].z = 2.624656018151939e6 | au.km
    system[1].vx = -4.195592326222561 | au.kms
    system[1].vy = 1.153726914561471e1 | au.kms
    system[1].vz = 9.564081722803852e-1 | au.kms

    system.move_to_center()

    return system


def generate_jupiter_io_system_td():
    """
    Ephemeris Pasadena, USA, Horizons

    JPL Ephemeris, Pasadena, USA, Horizons System

        * Start time        : A.D. 2026-Jan-01 00:00:00.0000 TDB
        * Stop  time        : A.D. 2026-Jan-01 00:01:00.0000 TDB
        * Coordinate Center : Solar System Barycenter

    Jupiter:
    kf from: Dong Lai 2021 Planet. Sci. J. 2 122 DOI 10.3847/PSJ/ac013b
    xi from: https://doi.org/10.1016/j.icarus.2011.09.016
    spin vector from: https://radiojove.gsfc.nasa.gov/education/jupiter/basics/jfacts.htm

    Io:
    kf from https://doi.org/10.1016/j.icarus.2025.116567
    xi from Schubert et al. 2004
    spin vector from https://doi.org/10.1016/j.icarus.2012.05.020 and ephemeris

    spin vectors were calculated from LOD, OBL, PSI using
    the ``Tidymess.convert_spin_vectors_to_inertial()`` method.

    tau values are arbitrary for both bodies.
    """
    system = generate_jupiter_io_system()

    system[0].kf = 0.565
    system[0].xi = 0.2629
    system[0].tau = 0 | au.s
    system[0].wx = 0.0 | 1 / au.s
    system[0].wy = -9.60092648806e-6 | 1 / au.s
    system[0].wz = 0.000175573560178 | 1 / au.s
    system[0].a_mb = 0

    system[1].kf = 0.125
    system[1].xi = 0.378
    system[1].tau = 0 | au.s
    system[1].wx = 0.0 | 1 / au.s
    system[1].wy = -1.43416864277e-9 | 1 / au.s
    system[1].wz = 4.10859051537e-5 | 1 / au.s
    system[1].a_mb = 0

    return system


def generate_earth_moon_system(self):
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
