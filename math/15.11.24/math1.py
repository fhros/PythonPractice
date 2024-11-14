import numpy as np
import matplotlib.pyplot as plt

angles_degrees = [30, 45, 60, 90, 120, 150, 180, 270]
angles_radians = np.radians(angles_degrees)

fig, ax = plt.subplots(figsize=(6, 6))
ax.plot(np.cos(np.linspace(0, 2 * np.pi, 100)), np.sin(np.linspace(0, 2 * np.pi, 100)))

for angle_deg, angle_rad in zip(angles_degrees, angles_radians):
    x, y = np.cos(angle_rad), np.sin(angle_rad)
    ax.plot(x, y, 'o', label=f'{angle_deg}°')
    ax.text(x * 1.1, y * 1.1, f'{angle_deg}°', ha='center', va='center')

ax.set_aspect('equal', 'box')
plt.xlabel("kosini")
plt.ylabel("sini")
plt.title("yksikköympyrä")
plt.grid(True)
plt.show()
