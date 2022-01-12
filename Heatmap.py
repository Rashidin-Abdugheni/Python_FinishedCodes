
#G:/SMPE_FIGURES/Heatmap-FINALS/SPME-01Heatmap.csv

import pandas as pd
import matplotlib.pyplot as plt
path_to_csv= "G:/SMPE_FIGURES/Heatmap-FINALS/Final1.csv"
df= pd.read_csv(path_to_csv ,index_col=0)
plt.imshow(df,cmap='Greens', interpolation='nearest')
# plt.show()

# libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Create a dataset
#df = pd.DataFrame(np.random.random((10, 10)), columns=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"])

# plot using a color palette
sns.heatmap(df, vmin=0, vmax=0.9)#cmap="PiYG"
#plt.show()

#sns.heatmap(df, cmap="Blues")
#plt.show()

#sns.heatmap(df, cmap="Reds")
#plt.show()

#sns.heatmap(df, cmap="Greens")
#plt.show()