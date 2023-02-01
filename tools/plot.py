import matplotlib.pyplot as plt
import numpy as np

bb_aug = [[0.984, 0.981, 0.976, 0.971, 0.964, 0.955, 0.946, 0.935, 0.921, 0.914],
[0.977, 0.976, 0.974, 0.973, 0.973, 0.969, 0.966, 0.962, 0.959, 0.957],
[0.992, 0.986, 0.979, 0.969, 0.957, 0.941, 0.927, 0.908, 0.883, 0.870 ],
[0.985, 0.981, 0.977, 0.971, 0.965, 0.955, 0.946, 0.934, 0.920, 0.912]]

bb_no_aug = [[0.942, 0.908, 0.882, 0.854, 0.824, 0.798, 0.776, 0.754, 0.737, 0.713],
[0.989, 0.986, 0.983, 0.979, 0.976, 0.971, 0.966, 0.963, 0.960, 0.949],
[0.896, 0.831, 0.781, 0.727, 0.671, 0.622, 0.579, 0.538, 0.504, 0.460],
[0.940, 0.902, 0.870, 0.835, 0.795, 0.758, 0.724, 0.690, 0.660, 0.620]]


gse_aug = [[0.883, 0.870, 0.854, 0.839, 0.828, 0.813, 0.797, 0.784, 0.769, 0.757],
[0.851, 0.845, 0.838, 0.831, 0.828, 0.820, 0.812, 0.804, 0.792, 0.788],
[0.933, 0.910, 0.882, 0.856, 0.833, 0.807, 0.780, 0.758, 0.737, 0.713],
[0.890, 0.877, 0.859, 0.843, 0.830, 0.813, 0.796, 0.780, 0.764, 0.748]]

gse_no_aug = [[0.887, 0.864, 0.845, 0.823, 0.802, 0.782, 0.762, 0.747, 0.729, 0.711],
[0.850, 0.840, 0.829, 0.816, 0.804, 0.790, 0.778, 0.770, 0.754, 0.743],
[0.942, 0.904, 0.873, 0.838, 0.804, 0.776, 0.742, 0.714, 0.689, 0.658],
[0.894, 0.871, 0.851, 0.827, 0.804, 0.783, 0.760, 0.741, 0.720, 0.698]]


ip_aug = [[0.970, 0.971, 0.972, 0.971, 0.972, 0.971, 0.971, 0.971, 0.970, 0.969] ,
[0.962, 0.962, 0.962, 0.961, 0.962, 0.960, 0.960, 0.960, 0.957, 0.954] ,
[0.980, 0.981, 0.983, 0.982, 0.982, 0.983, 0.984, 0.984, 0.985, 0.985] ,
[0.971, 0.972, 0.972, 0.972, 0.972, 0.971, 0.972, 0.972, 0.971, 0.969]]

ip_no_aug = [[0.890, 0.864, 0.841, 0.818, 0.795, 0.776, 0.755, 0.735, 0.721, 0.700],
[0.972, 0.971, 0.966, 0.964, 0.959, 0.950, 0.954, 0.946, 0.945, 0.926],
[0.804, 0.752, 0.708, 0.663, 0.620, 0.584, 0.539, 0.501, 0.473, 0.437],
[0.880, 0.848, 0.817, 0.785, 0.753, 0.723, 0.688, 0.655, 0.630, 0.594]]


ratios = [i/50.0 for i in range(1,11)]

SMALL_SIZE = 8
MEDIUM_SIZE = 10
BIGGER_SIZE = 16

plt.rc('font', size=BIGGER_SIZE )          # controls default text sizes
plt.rc('axes', titlesize=BIGGER_SIZE )     # fontsize of the axes title
plt.rc('xtick', labelsize=BIGGER_SIZE )    # fontsize of the tick labels
plt.rc('ytick', labelsize=BIGGER_SIZE )    # fontsize of the tick labels
plt.rc('legend', fontsize=BIGGER_SIZE )    # legend fontsize
font1 = {'color':'black','size':18}


plt.plot(ratios, bb_no_aug[0],'o-', label = "W/O Aug.")
plt.plot(ratios, bb_aug[0],'o-', label = "W/ Aug.")
plt.legend()
plt.ylabel('ACC',font1)
plt.xlabel('Corruption Degree',font1)
plt.savefig('./figures/ablation/bb/ACC.pdf')
plt.show()

plt.plot(ratios, bb_no_aug[1], 'o-',label = "W/O Aug.")
plt.plot(ratios, bb_aug[1],'o-',label = "W/ Aug.")
plt.legend()
plt.ylabel('Precision',font1)
plt.xlabel('Corruption Degree',font1)
plt.savefig('./figures/ablation/bb/Precision.pdf')

plt.show()
plt.plot(ratios, bb_no_aug[2], 'o-',label = "W/O Aug.")
plt.plot(ratios, bb_aug[2], 'o-',label = "W/ Aug.")
plt.legend()
plt.ylabel('Recall',font1)
plt.xlabel('Corruption Degree',font1)
plt.savefig('./figures/ablation/bb/Recall.pdf')
plt.show()
plt.plot(ratios, bb_no_aug[3], 'o-',label = "W/O Aug.")
plt.plot(ratios, bb_aug[3],'o-', label = "W/ Aug.")
plt.legend()
plt.ylabel('F1')
plt.xlabel('Corruption Degree')
plt.savefig('./figures/ablation/bb/F1.pdf')
plt.show()