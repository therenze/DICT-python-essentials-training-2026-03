import operator

# --- INPUT SECTION ---
distance    = 100.0      
time        = 20.0       
velocity    = 10.0
f_velocity  = 30.0       
i_velocity  = 10.0      
mass        = 50.0       
volume      = 5.0        

# --- CALCULATION SECTION ---

# 1. Average Speed [as = distance / time]
avg_speed = operator.truediv(distance, time)

# 2. Acceleration [a = (fvelocity - ivelocity) / time]
v_diff = operator.sub(f_velocity, i_velocity)
acceleration = operator.truediv(v_diff, time)

# 3. Density [density = mass / volume]
density = operator.truediv(mass, volume)

# 4. Force [force = mass * acceleration]
force = operator.mul(mass, acceleration)

# 5. Kinetic Energy [ke = 1/2 * mass * velocity^2]
v_sq = operator.pow(velocity, 2)
m_v_sq = operator.mul(mass, v_sq)
kinetic_energy = operator.mul(0.5, m_v_sq)


# --- PRINTING INPUTED VALUES ---
print(f"\n{'PRINTING INPUTED VALUES':<25}")
print("-" * 60)
print(f"Distance: {distance}")
print(f"Time: {time}")
print(f"Velocity: {velocity}")
print(f"Mass: {mass}")
print(f"Volume: {volume}")

# --- OUTPUT SECTION ---
print(f"\n{'FORMULA':<25} | {'RESULT':<10} | {'DATA TYPE'}")
print("-" * 60)
print(f"Average Speed (as)        | {avg_speed:<10} | {type(avg_speed)}")
print(f"Acceleration (a)          | {acceleration:<10} | {type(acceleration)}")
print(f"Density (d)               | {density:<10} | {type(density)}")
print(f"Force (f)                 | {force:<10} | {type(force)}")
print(f"Kinetic Energy (ke)       | {kinetic_energy:<10} | {type(kinetic_energy)}")