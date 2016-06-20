import pandas as pd

users = pd.read_table('u.user')
user_cols = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
users = pd.read_table('u.user', sep='|', header=None, names=user_cols, index_col='user_id', dtype={'zip_code':str})

# for each occupation in 'users', count the number of occurrences
print users.occupation.value_counts()

# for each occupation, calculate the mean age
print users.groupby('occupation').age.mean()

# for each occupation, calculate the minimum and maximum ages
print users.groupby('occupation').age.agg(['min','max'])

# for each combination of occupation and gender, calculate the mean age
print users.groupby(['occupation', 'gender']).age.mean()

# randomly sample a DataFrame
rand_users = users.sample(frac=0.75, random_state=1)
rand_remain_users = users[~users.index.isin(rand_users)]

# detect duplicate users   
users.drop_duplicates() 
