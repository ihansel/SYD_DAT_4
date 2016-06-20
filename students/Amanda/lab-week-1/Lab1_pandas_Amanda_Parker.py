import pandas as pd

pd.read_table('u.user')
# read 'u.user' into 'users'
user_cols = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
users = pd.read_table('u.user', sep='|', header=None, names=user_cols, index_col='user_id', dtype={'zip_code':str})

# examine the users data
#users                   # print the first 30 and last 30 rows
#type(users)             # DataFrame
#users.head()            # print the first 5 rows
#users.head(10)          # print the first 10 rows
#users.tail()            # print the last 5 rows
#users.index             # "the index" (aka "the labels")
#users.columns           # column names (which is "an index")
#users.dtypes            # data types of each column
users.shape             # number of rows and columns
users.values            # underlying numpy array
users.info()            # concise summary (including memory usage)

# select a column
#users['gender']         # select one column
#type(users['gender'])   # Series
users.gender            # select one column using the DataFrame attribute

# summarize (describe) the data
#users.describe()                    # describe all numeric columns
#users.describe(include=['object'])  # describe all object columns (can include multiple types)
#users.describe(include='all')       # describe all columns
#users.gender.describe()             # describe a single column
users.age.mean()                    # only calculate the mean

# count the number of occurrences of each value
#users.occupation.value_counts()     # most useful for categorical variables
users.age.value_counts()        # can also be used with numeric variables

####### EXCERCISE 1
# read drinks.csv into a DataFrame called 'drinks'
drinks = pd.read_table('drinks.csv', sep=',')
drinks = pd.read_csv('drinks.csv')              # assumes separator is comma
# print the head and the tail
drinks.head()
drinks.tail()
# examine the default index, data types, and shape
drinks.index
drinks.dtypes
drinks.shape
# print the 'beer_servings' Series
drinks['beer_servings']
drinks.beer_servings
# calculate the average 'beer_servings' for the entire dataset
drinks.describe()                   # summarize all numeric columns
drinks.beer_servings.describe()     # summarize only the 'beer_servings' Series
drinks.beer_servings.mean()         # only calculate the mean
# count the number of occurrences of each 'continent' value and see if it looks correct
drinks.continent.value_counts()

####### FILTERING AND SORTING
# logical filtering: only show users with age < 20
young_bool = users.age < 20         # create a Series of booleans...
users[young_bool]                   # ...and use that Series to filter rows
users[users.age < 20]               # or, combine into a single step
users[users.age < 20].occupation    # select one column from the filtered results
users[users.age < 20].occupation.value_counts()     # value_counts of resulting Series

# logical filtering with multiple conditions
users[(users.age < 20) & (users.gender=='M')]       # ampersand for AND condition
users[(users.age < 20) | (users.age > 60)]          # pipe for OR condition
users[users.occupation.isin(['doctor', 'lawyer'])]  # alternative to multiple OR conditions

# sorting
users.age.sort()                   # sort a column
users.sort('age')                   # sort a DataFrame by a single column
users.sort('age', ascending=False)  # use descending order instead
users.sort(['occupation', 'age'])   # sort by multiple columns

###### EXCERCISE 2
# filter DataFrame to only include European countries
drinks[drinks.continent=='EU']
# filter DataFrame to only include European countries with wine_servings > 300
drinks[(drinks.continent=='EU') & (drinks.wine_servings>300)]
# calculate the average 'beer_servings' for all of Europe
drinks[(drinks.continent=='EU')].beer_servings.mean()
# determine which 10 countries have the highest total_litres_of_pure_alcohol
top10 = drinks.sort('total_litres_of_pure_alcohol', ascending=False)
top10.country.head(10)
# rename the column 'beer_servings' to 'beer'
drinks_cols = ['country', 'beer', 'spirit_servings', 'wine_servings', 'total_litres_of_pure_alcohol','continent']
drinks.columns = drinks_cols
# add a new column as a function of existing columns, total_servings = beer + wine + spirits
total = drinks.beer + drinks.wine_servings + drinks.spirit_servings
drinks['total_servings']=total
# remove the column you just added
del drinks['total_servings']

###### HANDLING MISSING VALUES
# missing values are usually excluded by default
drinks.continent.value_counts()              # excludes missing values
drinks.continent.value_counts(dropna=False)  # includes missing values

# find missing values in a Series
drinks.continent.isnull()           # True if missing, False if not missing
drinks.continent.isnull().sum()     # count the missing values
drinks.continent.notnull()          # True if not missing, False if missing
drinks[drinks.continent.notnull()]  # only show rows where continent is not missing

# side note: understanding axes
drinks.sum(axis=0)      # sums "down" the 0 axis (rows)
drinks.sum()            # axis=0 is the default
drinks.sum(axis=1)      # sums "across" the 1 axis (columns)

# find missing values in a DataFrame
drinks.isnull()             # DataFrame of booleans
drinks.isnull().sum()       # count the missing values in each column

# fill in missing values
drinks.continent.fillna(value='NA')                 # fill in missing values with 'NA'
drinks.continent.fillna(value='NA', inplace=True)   # modifies 'drinks' in-place

# turn off the missing value filter

###### MERGING DATA
# read 'u.item' into 'movies'
movie_cols = ['movie_id', 'title']
movies = pd.read_table('u.item', sep='|', header=None, names=movie_cols, usecols=[0, 1])

# read 'u.data' into 'ratings'
rating_cols = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('u.data', sep='\t', header=None, names=rating_cols)

# merge 'movies' and 'ratings' (inner join on 'movie_id')
movie_ratings = pd.merge(movies, ratings)
movies.shape
ratings.shape
movie_ratings.shape

#### HOMEWORK 1
# for each occupation in 'users', count the number of occurrences
users.occupation.value_counts()
# for each occupation, calculate the mean age
import numpy as np
users.groupby('occupation').agg({'age': [np.mean]})
# for each occupation, calculate the minimum and maximum ages
users.groupby('occupation').agg({'age': [np.min, np.max]})
# for each combination of occupation and gender, calculate the mean age
pivoted = users.pivot_table(index=['occupation'],columns=['gender'], values={'age': [np.mean]},fill_value=0)
# randomly sample a DataFrame
users.sample(1)
# detect duplicate users
users[users.duplicated()]



