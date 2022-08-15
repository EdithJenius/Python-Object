import pandas as pd
import numpy as np
df1 = pd.DataFrame(np.arange(12).reshape((3,4)),columns=['a','b','c','d'])
df2 = pd.DataFrame(np.arange(12,24).reshape((3,4)),columns=['a','b','c','d'])
df3 = pd.DataFrame(np.arange(24,36).reshape((3,4)),columns=['a','b','c','d'])
print(df1)
print(df2)
print(df3)
df4 = pd.concat([df1,df2,df3],axis=0)#纵向合并
df4 = pd.concat([df1,df2,df3],axis=0,ignore_index=True)#纵向合并，不考虑原来的index
print(df4)
#横向合并
df5 = pd.concat([df1,df2,df3],axis=1)
#合并两个表，缺少的部分填充NaN
df1 = pd.DataFrame(np.arange(12).reshape((3,4)),columns=['a','b','c','f'])
df2 = pd.DataFrame(np.arange(12,24).reshape((3,4)),columns=['a','b','d','e'])
print(df1)
print(df2)
df6 = pd.concat([df1,df2],join='outer',ignore_index=True)
print(df6)
#合并两个表，缺少的部分去掉
df7 = pd.concat([df1,df2],join='inner',ignore_index=True)
print(df7)
