

import requests , zipfile 
import io  
import pandas as pd 
import os
# print(os.getcwd())

url = 'https://github.com/Hernan4444/MyAnimeList-Database/archive/refs/heads/master.zip'


# file = requests.get(url , stream=True)


# zip_file = zipfile.ZipFile(io.BytesIO(file.content))

# zip_file.extractall( 'download_file') 



# anime_data = pd.read_csv('download_file/MyAnimeList-Database-master/data/anime.csv') ; 

# print(anime_data.loc[0])




# want to crate to dataframfe for join with fakde data and have a col id 


dt1 = pd.DataFrame({
    'id' : [1,2,3,4,5 , 6] ,
    'name' : ['a','b','c','d','e' , 'f'] , 
    'age' : [10,20,30,40,50 , 60] 
})

dt2 = pd.DataFrame({
    'id' : [1,2,3,4,5],
    'gender' : ['m','f','m','f','m'] ,
    'country' : ['usa','france','italy','spain','germany'] 
}) 


# print(pd.merge(dt1 , dt2 , on='id')) ; 
# print(pd.concat([dt1 , dt2] , ignore_index=True)) ;

#now we try to delette a row and a column form dt1

# dt1.drop(index=0 , inplace=True).reset_index()
# dt1.drop(dt1[dt1['id'] == 1].index , inplace=True) ; 
# print(dt1)
# dt1.drop( 'age' , axis=1 , inplace=True )
# print(dt1)


#now we try with doplecate data frame 


# dt3 = pd.DataFrame({
#     'id' : [1,2,3,4,5 , 6] ,
#     'name' : ['a','b','c','d','a','f'] , 
#     'age' : [10,20,30,40,50 , 60] 
# })


# dt3.drop_duplicates(subset=['name'], inplace=True)
# print(dt3)



#try to test map in pandas


# dt6 = pd.DataFrame({
#     'id' : [1,2,3,4,5 ,6] , 
#     'name' : ['a','b','c','d','e' , 'f'] ,
#     'age' : [10,20,30,40,50 , 60] , 
#     'gender' : ['m','f','m','f','m' ,'h']
# })



# dt6['gender'] = dt6['gender'].map(lambda x: 'Male' if x == 'm' else ( 'Female' if x == 'f' else 'Unknown' ) ) ; 

# print(dt6)


# ages = [5, 15, 25, 35]
# bins = [0, 18, 100]

dt7 = pd.DataFrame({
    'id' : [1,2,3,4,5 ,6] , 
    'name' : ['a','b','c','d','e' , 'f'] ,
    'age' : [10,20,18,40,50,60]
})


print(pd.cut(dt7['age'] , bins=[0,18,100]).value_counts() )


def extract_anime_data(anime_data) :
  return anime_data.groupby('Type')['Score'].mean().sort_values( ascending=False) ; 















