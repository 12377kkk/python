# import numpy as np

# # arr1=np.array(45)
# # arr2=np.array([10,20,30])
# # arr3=np.array([[10,20,30],[40,50,60]])
# # arr4=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

# # print(arr1.ndim)
# # print(arr2.ndim)
# # print(arr3.ndim)
# # print(arr4.ndim)


# # 
# # arr= np.array([[1,2,3,4,5],[6,7,8,9,10]])
# # print("2nd element on 2st row:",arr[1,1]) #ar[row,col]
# # arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
# # print(arr[0,1,2])

# # arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
# # print([arr[0:2,1:4]])
# # arr=np.array(['apple','banana','cherry','mango'])
# # print(arr.dtype)

# # 
# arr=np.array([1,2,3,4,5])
# x=arr.copy()
# y=arr.view()

# print(x.base)
# print(y.base)


# df = pd.read_csv('data.csv')

# print(df.to_string())
# a=[1,7,2]
# myvar=pd.Series(a, index=['x','y','z'])
# print(myvar)
# print(myvar['y'])

# data={
#     "calories":[420,380,390],
#     "duration":[50,40,45]
# }
# df=pd.DataFrame(data, index=["day1", "day2","day3"])
# print(df.loc["day2"])
# import pandas as pd

# df = pd.read_csv("C:\\Users\\user\\Desktop\\data.csv")
# x=df["Calories"].mean()
# df.fillna({"Calories":x},inplace=True)
# print(df.to_string())

import pandas as pd 
df1= pd.read_csv("C:\\Users\\user\\Desktop\\LORR.csv")
print(df1)

df2=pd.read_csv("C:\\Users\\user\\Desktop\\LOTR2.csv")
print(df2)
merge_df= df1.merge(df2)
print(merge_df) 

print("hello world")