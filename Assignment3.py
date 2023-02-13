import pandas as pd
import numpy as np

cumulative_miles = np.array([0,55,120,180,220])      ##creating numpy array that stores cumulative miles

cumulative_miles = pd.Series(cumulative_miles)       ##convertting into panda

at_end = np.array([cumulative_miles[0]])
for i in range(1, len(cumulative_miles)):
  at_end = np.append(at_end, cumulative_miles[i]-cumulative_miles[i-1])   ##showing miles from one day to another day from cumilative miles 

print("Total miles that you rode each day:")
print(pd.Series(at_end))
