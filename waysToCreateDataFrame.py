import pandas as pd

'''
A pandas Dataframe can be created using various inputs like
Lists
Dict
Series
Numpy ndarrays
Another Dataframe
'''

#Empty DataFrame
df = pd.DataFrame()
print(df)

#using Lists (df can be created using single list or list of lists)
data = [1,2,3,4,5]
df = pd.DataFrame(data)
df = pd.DataFrame(data,index=['a','b','c','d','e'])
print(df)

data = [['Alex',10],['Bob',20],['susane',19]]
df = pd.DataFrame(data)
df = pd.DataFrame(data,columns = ['name','age'],dtype=float)
print(df)

#Using Dict
data = {'Name':['arun','karthik','shiva','Mohan'],'Age':[15,16,17,18]}
df = pd.DataFrame(data,index=['Rank1','Rank2','Rank3','Rank4'])
print(df)


data = [{'a':10,'b':20},{'a':15,'b':16,'c':17}]
df = pd.DataFrame(data,columns=['a','b'])
print(df)

#Using Series
data = {'one':pd.Series([1,2,3,4],index=['a','b','c','d']),'two':pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])}
df=pd.DataFrame(data)
print(df)
#Column Selection
print(df['one'])
#Adding New Column
df['three'] = pd.Series([10,20],index=['a','b'])
print(df)
#Adding new column using Existing Columns
df['four']=df['one']+df['three']
print(df)
#column Deletion
del df['one']
print(df)
#Row Selection
print(df.loc['a'])
print(df.iloc[2])
#slice rows (Multiple rows can be selected with :)
print(df[2:4])

#Addition of rows
df = pd.DataFrame([[1,2],[3,4]],columns=['a','b'])
df2 = pd.DataFrame([[5,6],[7,8]],columns=['c','d'])
df = df.append(df2)
print(df)
#delete rows
df = df.drop(0)
print(df)