import pandas as pd
import numpy as np

index = pd.date_range(start=pd.Timestamp('2024-05-01'), 
                         end=pd.Timestamp('2024-05-31'), 
                         freq='D')

data = np.random.randn(len(index))

series = pd.Series(data=data, index=index)

print(series)
