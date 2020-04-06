# file tools
import os
import sys

# plotting tools
import plotly
import plotly.graph_objects as go
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt

# Core
import numpy as np

###### Data ######
# Frome https://plotly.com/python/line-charts/
title = 'Main Source for News'
labels = ['Television', 'Newspaper', 'Internet', 'Radio']
colors = ['#1f77b4',  # muted blue
          '#ff7f0e',  # safety orange
          '#2ca02c',  # cooked asparagus green
          '#d62728',  # brick red
          ]

mode_size = [8, 8, 12, 8]
line_size = [2, 2, 4, 2]

x_data = np.vstack((np.arange(2001, 2014),)*4)

y_data = np.array([
                   [74, 82, 80, 74, 73, 72, 74, 70, 70, 66, 66, 69],
                   [45, 42, 50, 46, 36, 36, 34, 35, 32, 31, 31, 28],
                   [13, 14, 20, 24, 20, 24, 24, 40, 35, 41, 43, 50],
                   [18, 21, 18, 21, 16, 14, 13, 18, 17, 16, 19, 23],
                   ])

###### Init plot / subplots ######
# mpl
fig_mpl, ax = plt.subplots()

# plotly
fig_plo = plotly.subplots.make_subplots(rows=1, cols=1)

###### add data ######

for i in range(0, 4):
    # mpl
    ax.plot(x_data[i][:-1], y_data[i], color=colors[i], linewidth=line_size[i], label=labels[i])
    
    # plotly
    fig_plo.add_trace(go.Scatter(x=x_data[i], y=y_data[i], mode='lines',
                             name=labels[i],
                             line=dict(color=colors[i], width=line_size[i]),
                             connectgaps=True,
                             ))


##### ##### ##### ##### ##### ##### ##### ##### ##### #####
###### ###### Stlye below ###### ###### ###### ###### #####
##### ##### ##### ##### ##### ##### ##### ##### ##### #####

###### Font ######
# mpl
font = {'size': 12, 'family': 'serif', 'serif': ['Times']}
matplotlib.rc('font', **font)
matplotlib.rc('text', usetex=True)

# plotly
fig_plo.update_layout(font=dict(
                            family="Times New Roman, Times, serif",
                            size=24,
                            color="black"
                            ),
                  )

###### axis lines & fun ######
# mpl
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# plotly
fig_plo.update_xaxes(title_text="Year", linecolor='black', # account for white background
                     row=1, col=1, zeroline=True, zerolinecolor='rgba(0,0,0,.5)', zerolinewidth=1,)
fig_plo.update_yaxes(title_text="Market Share", linecolor='black', # account for white background
                     row=1, col=1, zeroline=True, zerolinecolor='rgba(0,0,0,.5)', zerolinewidth=1,)




###### resolution  & additions ######
# mpl
ax.legend()
# no resolution tool until saving :(

# plotly
fig_plo.update_layout(showlegend=True,)
fig_plo.update_layout(width=1000,
                  height=1000,)

###### background color ######
# mpl
ax.set_facecolor((1, 1, 1))

# plotly
fig_plo.update_layout(plot_bgcolor='white',)

###### saving ######
# mpl
plt.show()
plt.savefig(os.getcwd()+"plop_mpl.pdf", dpi=300)

# plotly
# advanced for saving
fig_plo.update_layout(legend_orientation="h",
                  legend=dict(x=.6, y=0.07,
                              bgcolor='rgba(205, 223, 212, .4)',
                              bordercolor="Black",
                              ),
                  plot_bgcolor='white',
                  width=1600,
                  height=1000,
                  margin=dict(r=10, l=10, b=10, t=10),
                  )

fig_plo.write_image(os.getcwd()+"plot_plotly.pdf")
fig_plo.show()

