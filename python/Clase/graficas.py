###seaborn y matplotlib

import collections
from numpy.lib import histograms
import pandas as pd
import numpy as np

import matplotlib as mpl
import seaborn as sns
from seaborn import colors


###histogramas

datos1 = np.random.rand(100)
print( datos1 )

mpl.pyplot.hist( datos1 )
mpl.pyplot.show()

print("pasa")
sns.set_theme()
sns.histplot( datos1 )

datos2 = np.random.rand(80)
mpl.pyplot.hist( datos1, color = "green", alpha=0.3, bins=20, density=True)
mpl.pyplot.hist( datos2, color = "blue", alpha=0.3, bins=20, density=True)
mpl.pyplot.show()

print("_"*30)
#Distribuciones
