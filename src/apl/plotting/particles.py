from typing import Literal

from amuse.datamodel import Particles
from amuse.units import units as au
from matplotlib.axes import Axes
from matplotlib.collections import PathCollection
import matplotlib.pyplot as plt
from matplotlib.typing import ColorType
from visualastro.core.numerical_utils import to_list
from visualastro.plotting.core.axes import get_ax, set_axis_labels

from apl.core.units import amuse_quantity_2_astropy


def plot_particles(
    particles: Particles | list[Particles],
    ax: Axes | None = None,
    unit = au.au,
    zdir: Literal['z', 'y', 'x'] = 'z',
    s: float = 1.0,
    **kwargs
) -> list[PathCollection]:
    particles = to_list(particles)
    position = [p.position for p in particles]
    ax = get_ax(ax)
    artists = []

    ax1, ax2 = {
        'x': (1, 2),
        'y': (0, 2),
        'z': (0, 1),
    }.get(zdir, (0, 1))
    xlabel, ylabel = {
        'x': ('Y', 'Z'),
        'y': ('X', 'Z'),
        'z': ('X', 'Y'),
    }.get(zdir, ('X', 'Y'))

    for pos in position:
        artists.append(
            ax.scatter(
                get_value(pos[:,ax1], unit=unit),
                get_value(pos[:,ax2], unit=unit),
                s=s, **kwargs
            )
        )
    x_astropy = [amuse_quantity_2_astropy(getattr(p, xlabel.lower()), unit=unit) for p in particles]
    y_astropy = [amuse_quantity_2_astropy(getattr(p, ylabel.lower()), unit=unit) for p in particles]
    set_axis_labels(x_astropy, y_astropy, ax=ax, xlabel=xlabel, ylabel=ylabel)

    return artists


def plot_xyz(
    particles: Particles | list[Particles],
    color: ColorType = 'darkslateblue',
    s: float = 1.0,
    **kwargs
) -> list[PathCollection]:
    fig, ax = plt.subplots(1, 3, figsize=(10, 10/3), layout='constrained')

    sc1 = plot_particles(particles, ax=ax[0], zdir='z', s=s, color=color, **kwargs)
    sc2 = plot_particles(particles, ax=ax[1], zdir='x', s=s, color=color, **kwargs)
    sc3 = plot_particles(particles, ax=ax[2], zdir='y', s=s, color=color, **kwargs)

    return sc1 + sc2 + sc3


def get_value(array, unit=None):
    if hasattr(array, 'number'):
        if unit:
            array = array.as_quantity_in(unit)
        return array.number
    return array
