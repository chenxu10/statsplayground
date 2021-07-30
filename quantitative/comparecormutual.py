import numpy as np
import pandas as pd
from sklearn.metrics import mutual_info_score
from scipy.stats import pearsonr

a = np.array([1,2,3,4,5,6])
b = 2 * a

print(mutual_info_score(a,b))
print(pearsonr(a,b))




