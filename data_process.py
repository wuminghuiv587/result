import pandas as pd


print("processing train_Data")
train_1_data = pd.read_excel('/tf/temporary/trainvalue1.xlsx')
#train_1_data = train_1_data[:3]
print("train_1_data.shape=",train_1_data.shape)
train_2_data = pd.read_excel('/tf/temporary/trainvalue2.xlsx')
#train_2_data = train_2_data[:3]
print("train_2_data.shape=",train_2_data.shape)
train_data_result = pd.concat([train_1_data,train_2_data],axis=1)
print("train_data_shape=",train_data_result.shape)
train_data_result.to_excel('/tf/result/trainvalue.xlsx', index=False)
print("train_data_concat successed")

print("processing train_df")
train_1_df = pd.read_excel('/tf/temporary/traindf1.xlsx')
#train_1_data = train_1_data[:3]
print("train_1_df.shape=",train_1_df.shape)
train_2_df = pd.read_excel('/tf/temporary/traindf2.xlsx')
#train_2_data = train_2_data[:3]
print("train_2_df.shape=",train_2_df.shape)
train_df_result = pd.concat([train_1_df,train_2_df],axis=1)
print("train_df_shape=",train_df_result.shape)
train_df_result.to_excel('/tf/result/traindf.xlsx', index=False)
print("train_df_concat successed")

print("processing test_Data")
test_1_data = pd.read_excel('/tf/temporary/test+value1.xlsx')
#train_1_data = train_1_data[:3]
print("test_1_data.shape=",test_1_data.shape)
test_2_data = pd.read_excel('/tf/temporary/test+value2.xlsx')
#train_2_data = train_2_data[:3]
print("test_2_data.shape=",test_2_data.shape)
test_data_result = pd.concat([test_1_data,test_2_data],axis=1)
print("test_data_shape=",test_data_result.shape)
test_data_result.to_excel('/tf/result/test+value.xlsx', index=False)
print("test_data_concat successed")
