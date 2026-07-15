from amuse.datamodel import Particles
from amuse.units import nbody_system as ns


def generate_figure8_system():
    """
    Figure 8 system initial conditions courtesy of
    Dr. Tjarda Boekholt.
    """
    figure8 = Particles(3)
    figure8[0].name = 'Star1'
    figure8[0].mass = 1 | ns.mass
    figure8[0].radius = 5e-2 | ns.length
    figure8[0].x = 0 | ns.length
    figure8[0].y = 0 | ns.length
    figure8[0].z = 0 | ns.length
    figure8[0].vx = -0.93240737 | ns.speed
    figure8[0].vy = -0.86473146 | ns.speed
    figure8[0].vz = 0 | ns.speed
    figure8[0].xi = 0.07
    figure8[0].kf = 0.02
    figure8[0].tau = 1e-2 | ns.time
    figure8[0].wx = 0 | 1 / ns.time
    figure8[0].wy = 0 | 1 / ns.time
    figure8[0].wz = 0 | 1 / ns.time

    figure8[1].name = 'Star2'
    figure8[1].mass = 1 | ns.mass
    figure8[1].radius = 5e-2 | ns.length
    figure8[1].x = 0.9700436 | ns.length
    figure8[1].y = -0.24308753 | ns.length
    figure8[1].z = 0 | ns.length
    figure8[1].vx = 0.466203685 | ns.speed
    figure8[1].vy = 0.43236573 | ns.speed
    figure8[1].vz = 0 | ns.speed
    figure8[1].xi = 0.07
    figure8[1].kf = 0.02
    figure8[1].tau = 1e-2 | ns.time
    figure8[1].wx = 0 | 1 / ns.time
    figure8[1].wy = 0 | 1 / ns.time
    figure8[1].wz = 0 | 1 / ns.time

    figure8[2].name = 'Star3'
    figure8[2].mass = 1 | ns.mass
    figure8[2].radius = 5e-2 | ns.length
    figure8[2].x = -0.9700436 | ns.length
    figure8[2].y = 0.24308753 | ns.length
    figure8[2].z = 0 | ns.length
    figure8[2].vx = 0.466203685 | ns.speed
    figure8[2].vy = 0.43236573 | ns.speed
    figure8[2].vz = 0 | ns.speed
    figure8[2].xi = 0.07
    figure8[2].kf = 0.02
    figure8[2].tau = 1e-2 | ns.time
    figure8[2].wx = 0 | 1 / ns.time
    figure8[2].wy = 0 | 1 / ns.time
    figure8[2].wz = 0 | 1 / ns.time

    return figure8


def generate_pythagorean_system():
    """
    Generate 3 particles in a pythagorean triangle configuration.
    Initial conditions courtesty of Dr. Alessandro Trani.
    """
    p = Particles(3)

    p[0].mass = 3 | ns.mass
    p[0].radius = 0 | ns.length
    p[0].x = 1 | ns.length
    p[0].y = 3 | ns.length
    p[0].z = 0 | ns.length
    p[0].vx = 0 | ns.speed
    p[0].vy = 0 | ns.speed
    p[0].vz = 0 | ns.speed
    p[0].wx = 0 | 1 / ns.time
    p[0].wy = 0 | 1 / ns.time
    p[0].wz = 0 | 1 / ns.time

    p[1].mass = 4 | ns.mass
    p[1].radius = 0 | ns.length
    p[1].x = -2 | ns.length
    p[1].y = -1 | ns.length
    p[1].z = 0 | ns.length
    p[1].vx = 0 | ns.speed
    p[1].vy = 0 | ns.speed
    p[1].vz = 0 | ns.speed
    p[1].wx = 0 | 1 / ns.time
    p[1].wy = 0 | 1 / ns.time
    p[1].wz = 0 | 1 / ns.time

    p[2].mass = 5 | ns.mass
    p[2].radius = 0 | ns.length
    p[2].x = 1 | ns.length
    p[2].y = -1 | ns.length
    p[2].z = 0 | ns.length
    p[2].vx = 0 | ns.speed
    p[2].vy = 0 | ns.speed
    p[2].vz = 0 | ns.speed
    p[2].wx = 0 | 1 / ns.time
    p[2].wy = 0 | 1 / ns.time
    p[2].wz = 0 | 1 / ns.time

    return p
