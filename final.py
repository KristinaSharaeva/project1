import pandas as pd
from sklearn.preprocessing import OneHotEncoder

lst = ['robot'] * 10
lst += ['human'] * 10
import random
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

encoder = OneHotEncoder(sparse=False)
one_hot = encoder.fit_transform(data[['whoAmI']])

columns = encoder.get_feature_names_out(['whoAmI'])
data_one_hot = pd.DataFrame(one_hot, columns=columns)

data = pd.concat([data, data_one_hot], axis=1)

print(data.head())