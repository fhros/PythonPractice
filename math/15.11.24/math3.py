import numpy as np
import matplotlib.pyplot as plt

angles_degrees = [30, 45, 60, 90, 120, 150, 180, 270]
angles_radians = np.radians(angles_degrees)

x_vals = np.linspace(-3 * np.pi, 3 * np.pi, 1000)
cos_vals = np.cos(x_vals)
sin_vals = np.sin(x_vals)

fig, ax = plt.subplots(figsize=(19.2, 14.4))

ax.plot(x_vals, cos_vals, 'r--', label="cos(x)")
ax.plot(x_vals, sin_vals, 'b-.', label="sin(x)")

for angle_deg, angle_rad in zip(angles_degrees, angles_radians):
    x, y = np.cos(angle_rad), np.sin(angle_rad)
    ax.plot(angle_rad, y, 'go', label=f'{angle_deg}°')
    ax.text(angle_rad, y * 1.1, f'{angle_deg}°', ha='center', va='center')

ticks = np.arange(-3 * np.pi, 3 * np.pi + np.pi/2, np.pi/2)
tick_labels = [r"$-3\pi$", r"$-5\pi/2$", r"$-2\pi$", r"$-3\pi/2$", r"$-\pi$",
               r"$-\pi/2$", r"$0$", r"$\pi/2$", r"$\pi$", r"$3\pi/2$",
               r"$2\pi$", r"$5\pi/2$", r"$3\pi$", r"$7\pi/2$"]

ax.set_xticks(ticks)
ax.set_xticklabels(tick_labels)

ax.axhline(0, color='grey', linewidth=0.5)
ax.axvline(0, color='grey', linewidth=0.5)
ax.set_aspect('equal', 'box')
ax.set_xlim(-3 * np.pi, 3 * np.pi)
ax.set_ylim(-1.5, 1.5)
plt.xlabel("radiaanit")
plt.ylabel("amplitudi")
plt.legend()
plt.title("sini ja cosini käyrät kulma merkinnöillä")
plt.grid(True)
plt.show()
