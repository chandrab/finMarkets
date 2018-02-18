# commond to put all this file var into global space to use in Intepretor
# exec(open("./dfbasics.py").read(), globals())

import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(4,3),columns=['col1','col2','col3'])

# extract one column as new dataframe
df2 = df['col1']

# converts to numpy array
nparr = df.values

# extract column 1 as numpy array npc1
npc1 = nparr[:,0]

# extract column 2
npc2 = nparr[:,1]
