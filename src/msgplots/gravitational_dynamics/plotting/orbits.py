
from amuse.datamodel import Particles
from amuse.ext.orbital_elements import orbital_elements
from amuse.units import constants as c, units as au
from visualastro.core.numerical_utils import to_list


def get_elements(p: Particles):
    """
    Compute orbital parameters from a binary particle system.

    Parameters
    ----------
    p : amuse.datamodel.Particles
        Binary system stored in a `Particles` dataclass.

    Returns
    -------
    mass1 :
        Mass of first body.
    mass2 :
        Mass of second body.
    semimajor_axis :
        Semimajor axis of the system.
    eccentricity :
        Eccentricity of the system.
    true_anomaly :
        Cosine of the true anomaly.
    inclination :
        Cosine of the orbital inclination.
    longitude_of_the_ascending_node :
        Cosine of the longitude of the ascending node.
    argument of periapsis :
        Cosine of the argument of the periapsis.
    """
    if len(p) != 2:
        raise ValueError(f'Input should be a binary system! Got: N={len(p)}')
    p_si = p.copy()
    p_si.position = p_si.position.as_quantity_in(au.m)
    p_si.velocity = p_si.velocity.as_quantity_in(au.m / au.s)
    p_si.mass = p_si.mass.as_quantity_in(au.kg)

    return orbital_elements(p_si, G=c.G)


def get_semimajor_axes(
    plist: Particles | list[Particles],
    unit=au.au
):
    """
    Compute semimajor axis for a list of particle sets.

    Parameters
    ----------
    plist : Particles or list of Particles
        List of Particle(s) to compute semimajor axis.
    unit : amuse.units
        Unit of returned semimajor axes.

    Returns
    -------
    smas : VectorQuantity
        `VectorQuantity` array of semimajor axes
        in the units of `unit`.
    """
    plist = to_list(plist)
    smas = [] | au.au
    for p in plist:
        results = get_elements(p)
        smas.append(results[2].as_quantity_in(unit))

    return smas
