import ulula as ul
import pyro as pyro
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import os
home = os.getenv("HOME")
raytay = pyro.Pyro("compressible")
parameters = {'driver.tmax':5, 'io.dt_out':0.05, 'driver.max_steps':10000, 'io.basename':home+'/ismproj/output/pyro_','vis.store_images':0}
raytay.initialize_problem(problem_name="rt",inputs_file="inputs.rt", inputs_dict=parameters)
raytay.run_sim()
