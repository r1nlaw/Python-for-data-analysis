import matplotlib.pyplot as plt
import numpy as np

months = ['January', 'February', 'March', 'April', 'May', 'November', 'December']
hornberg = [300, 200, 250, 220, 180, 270, 290]
strick = [280, 170, 240, 230, 190, 300, 310]
huetten = [270, 190, 230, 210, 175, 250, 260]

bar_width = 0.25
r1 = np.arange(len(months))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]

plt.figure(figsize=(8, 6))

plt.bar(r1, hornberg, color='salmon', width=bar_width, edgecolor='grey', label='Hornberg')
plt.bar(r2, strick, color='green', width=bar_width, edgecolor='grey', label='Strick')
plt.bar(r3, huetten, color='skyblue', width=bar_width, edgecolor='grey', label='Huetten')

plt.xlabel('Month', fontsize=12)
plt.ylabel('Monthly Precipitation [mm]', fontsize=12)
plt.title('Monthly Precipitation Comparison', fontsize=16)

plt.xticks([r + bar_width for r in range(len(months))], months)

plt.legend(title='variable', loc='upper right', fontsize=10)

plt.grid(True, axis='y', linestyle='--', alpha=0.7)

plt.show()

print('1')
