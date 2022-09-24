from sklearn.feature_extraction import DictVectorizer
from sklearn import linear_model
import pandas as pd


our_home = {
    'Year_Built:': 1954, 
    'Condition': 'A', 
    'Story_Height:': 1, 
    'Finished_Rooms:': 5, 
    'Legal_Acres:': .270087, 
    'Bedrooms': 3, 
    'Extra_Finished_Rooms:': 2, 
    '1st_Floor_Construction': 'Wood Frame', 
    '1st_Floor_Base_Area:': 1050, 
    'Upper_Floor_Base_Area:': 0,
    'Number_of_Full_Baths:': 1, 
    'Number_of_Half_Baths:': 1,  
    'Numbers_of_Garages': 1, 
    'Number_of_Attached_Carports:': 0
    }


train_set = pd.read_csv(r'path_to_train_set\train_set.csv', delimiter='|')

train_predict = train_set['sale_price'].to_numpy()

train_set.drop(train_set[['sale_price']], axis=1, inplace=True)

train_dict = train_set.to_dict('records')


vec = DictVectorizer(sparse=False)

transformed = vec.fit_transform(train_dict)

model = linear_model.LinearRegression()

model.fit(transformed, train_predict)

print(model.predict(vec.transform(our_home)))

