
from amuse.datamodel import Particles
from amuse.io import read_set_from_file, write_set_to_file


def savepoint(obj, time=None) -> Particles:
    """
    Add a model time savepoint to a particleset. Savepoint
    time accessible via the `get_timestep` method.

    Equivalent to `particles.savepoint(time)`. Always
    returns a copy of `obj`.

    Parameters
    ----------
    obj : Particles | AmuseCommunityCode
        Either provide an amuse `Particles`
        instance and a `time`, or provide
        an amuse code instance with
        `model_time` and `particles` attributes.
        Is a copy of `obj`.
    time :  float | ScalarQuantity
        Time to save.

    Returns
    -------
    Particles :
        Particleset with a `get_timestep` attribute.

    Examples
    --------
    >>> savepoint = add_savepoint(particle, time=1|u.s)
    >>> savepoint.get_timestep()
    1 | u.s
    """
    if isinstance(obj, Particles):
        particles = obj
    elif hasattr(obj, 'particles'):
        particles = obj.particles
        if not time:
            time = getattr(obj, 'model_time', None)
    else:
        raise ValueError(
        'specify at least a code instance with a particles attribute or '
        'a Particle set!'
    )

    return particles.savepoint(time) if time else particles


def write_set_2_file(
    set,
    filename,
    time = None,
    format='amuse',
    **format_specific_keyword_arguments
):
    """
    Write a set to the given file in the given format.

    :argument filename: name of the file to write the data to
    :argument format: name of a registered format or
        a :class:`FileFormatProcessor` subclass (must be a
        class and not an instance)

    All other keywords are set as attributes on the fileformat processor. To
    determine the supported options for a processor call
    :func:`get_options_for_format`
    """
    return write_set_to_file(
        savepoint(set, time),
        filename=filename,
        format=format,
        **format_specific_keyword_arguments
    )
