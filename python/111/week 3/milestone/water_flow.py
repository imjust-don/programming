

def water_column_height(tower_height, tank_height):
    height = tower_height + ((3 * tank_height)/ 4)
    return height
def pressure_gain_from_water_height(height):
    h = height
    wd = 998.2
    g = 9.80665
    p = (h * wd * g) / 1000
    return p

def pressure_loss_from_pipe(pipe_diameter,
        pipe_length, friction_factor, fluid_velocity):
    f = friction_factor
    L = pipe_length
    x = 998.2
    v = fluid_velocity
    d = pipe_diameter
    answer = -(f * L * x * (v**2))/(2000*d)
    return answer

def pressure_loss_from_fittings(
        fluid_velocity, quantity_fittings):
    p = 998.2
    v = fluid_velocity
    n = quantity_fittings

    answer = (-0.04*p*v**2*n)/2000
    return answer

def reynolds_number(hydraulic_diameter, fluid_velocity):
    p = 998.2
    d = hydraulic_diameter
    v = fluid_velocity
    u = 0.0010016

    r = (p*v*d)/u

    return r

def pressure_loss_from_pipe_reduction(larger_diameter,
        fluid_velocity, reynolds_number, smaller_diameter):
    r = reynolds_number
    D = larger_diameter
    x = smaller_diameter
    p = 998.2
    v = fluid_velocity

    k = (0.1 + (50/r))*((D/x)**4-1)
    answer = (-k*p*v**2)/2000
    return answer


PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)


def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss

    print(f"Pressure at house: {pressure:.1f} kilopascals")


if __name__ == "__main__":
    main()
