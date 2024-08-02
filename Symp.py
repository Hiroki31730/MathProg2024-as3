import numpy as np
import pandas as pd



def Symp(x, y):
    x_array = np.array(x)
    y_array = np.array(y)
    y_array = -y_array
    xy_array = np.vstack([x_array, y_array])
    index_x = []
    column_x = []
    
    variable_line = x_array.shape[0]
    variable_row = x_array.shape[1]-1
    
    
    for x in range(variable_line+variable_row):
        if x+1 <= variable_row:
            column_x.append("x"+ str(x+1))
        
        elif x+1 > variable_row:
            index_x.append("x" + str(x+1))
            if x+1 == variable_line+variable_row:
                column_x.append("Cons")
                index_x.append("Z")
            
        
    df = pd.DataFrame(xy_array, index=index_x,columns=column_x)
    
    print(df)
    print()
    
    df_copy = df.copy()
    
    while not np.all(np.array(df.loc["Z"]) >= 0):
        
        min_column = df.loc["Z"].idxmin() # 最も小さいカラムをとる
    
        
        min_column_index = df.columns.get_loc(min_column) # カラムが何番目かを取得
        
        
        min_colval = df[min_column][:-1] # 最も小さい要素をとる
        num = df["Cons"][:-1] #　定数をとる
        
        
        new_num = np.array(num/min_colval) # 定数を最小の数で割ったものをとる
        
        
        new_num_min_idx = np.argmin(new_num) # new_numで最も小さい要素の配列番号をとる
        
        
        PE_index = index_x[new_num_min_idx] # インデックスリストから参照して、最も小さい要素のインデックスをとる
        
        
        PE_line = df.loc[PE_index] # 最も小さい要素の行要素を抜き出す
        
        
        PE = df[min_column][new_num_min_idx] # PEを指定する。
        
        
        New_PE_line = PE_line/PE # PEの行要素をPEでわる
        
        #print(PE_index)
        
        
        df.loc[PE_index] = New_PE_line
        
        #print(df_copy)
        #print(df)
        
        
        
        for y in range(df.shape[0]):
            if new_num_min_idx == y:
                continue
            else:
                #print(df.iloc[y])
                #print(df[min_column])
                df.iloc[y] = np.array(df.iloc[y]) -  (np.array(New_PE_line) * df[min_column][y])
                #print(df.iloc[y])
        
        
        
        new_index_x = index_x.copy()        
        new_column_x = column_x.copy()
        
        
        new_index_x[new_num_min_idx] = column_x[min_column_index]
        new_column_x[min_column_index] = index_x[new_num_min_idx]
        
        index_x = new_index_x.copy()
        column_x = new_column_x.copy()
        
        
        df.index = new_index_x
        df.columns = new_column_x
        
        min_column = df.loc["Z"].idxmin() # 最も小さいカラムをとる
        if np.all(np.array(df[min_column]) <= 0) == True:
            print("最適解は存在しない")
            exit()
        
        print(df)
        
        break
        
        

        
        
        
        
        
        
        
    
    
    
    
    
            
    

        
    
    
    
    

x = ([1, -1, 2, 8],
     [2, -3, -1, 1])
y = (1, 1, 1, 0)

Symp(x, y)
