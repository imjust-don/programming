

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