#%%
from mpl_toolkits.axisartist.parasite_axes import HostAxes, ParasiteAxes
import matplotlib.pyplot as plt
import numpy as np
import re

#parser host.log##########################################
# such as : 0s, type:h264, width:3840, height:2160, fps:1, keyFrameInterval:14, data:103265byte, cpu:3.91%, memory:139mb, bitrates:3000000
file = open('host.txt', 'r')

#to 2 dimesion arrary
linesList = file.readlines()
linesList = [line.strip().split(',') for line in linesList]

times = [int(re.findall(r"\d+\.?\d*",x[0])[0]) for x in linesList]
#print(times)
#title is : h264 width:3840 height:2160 keyFrameInterval:14 bitrates:3000000
title = [x[1] for x in linesList][0][6:]
title = title + [x[2] for x in linesList][0]
title = title + [x[3] for x in linesList][0]
title = title + [x[5] for x in linesList][0]
#print(fps)
data = [int(re.findall(r"\d+\.?\d*",x[6])[0]) for x in linesList]
#print(data)
cpu = [float(re.findall(r"\d+\.?\d*",x[7])[0]) for x in linesList]
#print(cpu)
mem = [int(re.findall(r"\d+\.?\d*",x[8])[0]) for x in linesList]
#print(mem)
title = title + [x[9] for x in linesList][0]
#print(title)
file.close()

#create HostAxes(data) and ParasiteAxes(cpu, memory)##########
#figure define, what is 1?
fig = plt.figure(1) 
#use [left, bottom, weight, height]to define axes，0 <= l,b,w,h <= 1
ax_data = HostAxes(fig, [0, 0, 0.9, 0.9])  

#parasite addtional axes, share x
ax_cpu = ParasiteAxes(ax_data, sharex=ax_data)
ax_mem = ParasiteAxes(ax_data, sharex=ax_data)
#ax_bitrates = ParasiteAxes(ax_data, sharex=ax_data)
#ax_wear = ParasiteAxes(ax_data, sharex=ax_data)

#append axes
ax_data.parasites.append(ax_cpu)
ax_data.parasites.append(ax_mem)
#ax_data.parasites.append(ax_bitrates)
#ax_data.parasites.append(ax_wear)

#invisible right axis of ax_data
ax_data.axis['right'].set_visible(False)
ax_data.axis['top'].set_visible(False)
ax_cpu.axis['right'].set_visible(True)
ax_cpu.axis['right'].major_ticklabels.set_visible(True)
ax_cpu.axis['right'].label.set_visible(True)

#set label for axis
ax_data.set_ylabel('data')
ax_data.set_xlabel('time (s)')
ax_cpu.set_ylabel('cpu')
ax_mem.set_ylabel('memory')
#ax_bitrates.set_ylabel('bitrates')
#ax_wear.set_ylabel('Wear')

#new axsi line 
load_axisline = ax_mem.get_grid_helper().new_fixed_axis
#cp_axisline = ax_bitrates.get_grid_helper().new_fixed_axis
#wear_axisline = ax_wear.get_grid_helper().new_fixed_axis

#axsi line padding on the right
ax_mem.axis['right2'] = load_axisline(loc='right', axes=ax_mem, offset=(40,0))
#ax_bitrates.axis['right3'] = cp_axisline(loc='right', axes=ax_bitrates, offset=(80,0))
#ax_wear.axis['right4'] = wear_axisline(loc='right', axes=ax_wear, offset=(120,0))

#add host axes to fig
fig.add_axes(ax_data)

#plot fig####################################
#curve_data, = ax_data.plot(times, data, label="data", color='green')
width = 0.9
curve_data = ax_data.bar(range(len(times)), list(map(float,data)), width,
                label="data", alpha = .5, color = 'g')
curve_cpu, = ax_cpu.plot(times, cpu, label="cpu", color='red')
curve_mem, = ax_mem.plot(times, mem, label="memory", color='blue')
#curve_bitrates, = ax_bitrates.plot(times, mem, label="bitrates", color='yellow')
#curve_wear, = ax_wear.plot([0, 1, 2], [25, 18, 9], label="Wear", color='blue')
ax_data.legend()

#axes name and color############################
#ax_data.axis['left'].label.set_color(ax_data.get_color())
ax_cpu.axis['right'].label.set_color('red')
ax_mem.axis['right2'].label.set_color('blue')
#ax_bitrates.axis['right3'].label.set_color('yellow')
#ax_wear.axis['right4'].label.set_color('blue')

ax_cpu.axis['right'].major_ticks.set_color('red')
ax_mem.axis['right2'].major_ticks.set_color('blue')
#ax_bitrates.axis['right3'].major_ticks.set_color('yellow')
#ax_wear.axis['right4'].major_ticks.set_color('blue')

ax_cpu.axis['right'].major_ticklabels.set_color('red')
ax_mem.axis['right2'].major_ticklabels.set_color('blue')
#ax_bitrates.axis['right3'].major_ticklabels.set_color('yellow')
#ax_wear.axis['right4'].major_ticklabels.set_color('blue')

ax_cpu.axis['right'].line.set_color('red')
ax_mem.axis['right2'].line.set_color('blue')
#ax_bitrates.axis['right3'].line.set_color('yellow')
#ax_wear.axis['right4'].line.set_color('blue')

#title
fig.suptitle(title, fontsize=16)

#save png with tight mode#######################
plt.tight_layout()
plt.savefig("win-ss.png",bbox_inches='tight')
#plt.show()

