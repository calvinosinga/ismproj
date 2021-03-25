import h5py as hp
import matplotlib.pyplot as plt
import matplotlib as mpl
import os
import numpy as np
home = os.getenv("HOME")
path = home+'/ismproj/'
pyrofiles = os.listdir(path+'output/')
count = 0
for p in pyrofiles:
    f = hp.File(path+'output/'+p,'r')
    state = f['state']
    dens = state['density/data'][:]
    dens = np.rot90(dens)
    plt.imshow(dens)
    plt.title('density')
    plt.xlabel('x-position')
    plt.ylabel('y-position')
    plt.colorbar()
    plt.savefig(path+'plots/frame_%03d.png'%count, bbox_inches='tight', pad_inches=0.2)
    plt.clf()
    count += 1    
