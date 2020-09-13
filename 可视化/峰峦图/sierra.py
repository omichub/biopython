import matplotlib.pyplot as plt
import joypy
import numpy as np
import pandas as pd


colors = ['#791E94', '#58C9B9', '#519D9E', '#D1B6E1']
data = pd.read_csv('sample_data.csv')
fig, axs = joypy.joyplot(data, by="project", fill=True, legend=True, alpha=.8,
                         range_style='own', xlabelsize=22, ylabelsize=22,
                         grid='both', linewidth=.8, linecolor='k', figsize=(12, 6), color=colors,
                         )

ax = plt.gca()
ax.set_xlim(left=0, right=7)
ax.set_xticks(np.arange(7))
ax.set_xticklabels( ['1', '2', '3', '4', '5', '6','7'])
ax.text(.5,
        1.1,
        "expression comparison",
        transform=ax.transAxes,
        ha='center',
        va='center',
        fontsize=25,
        color='black')
ax.text(.5, 1.03, "3 projects, 4 samples for each project", transform=ax.transAxes,
        ha='center', va='center', fontsize=15, color='black')
ax.text(.90, -.11, '\nBioPython teaching examples, do not represent real research', transform=ax.transAxes,
        ha='center', va='center', fontsize=12, color='black')
plt.savefig(r'sierra.png',
            width=7, height=5, dpi=900, bbox_inches='tight')
