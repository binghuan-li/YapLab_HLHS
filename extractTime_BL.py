#!/usr/bin/env python

# the script extracts the time from vol_test 
# with 3 complete cycles, i.e. ramp, systole[1-3]
# diastole[1-3]

import pandas as pd
import matplotlib.pyplot as plt

# set precision
pd.set_option('precision', 15)

# read file, delimeter is a space
df = pd.read_csv('Volume.out',sep=" ",quoting=3, skiprows=3,
                 names=['Step','Time-step', 'Volume'], index_col=False) 

#ignore the first row, convert datatype to float
df = df.iloc[1:]
df = df.astype(float)

# plot and save
plot = df.plot('Time-step', 'Volume')
plt.savefig('ExtractTime.pdf')

# 0.3 is a trial number but makes sure the value in its range
df_100 = df[df['Time-step'] < 0.3]
df_100_max = df_100.loc[df['Volume'] == df_100['Volume'].max(), ['Time-step']].reset_index(drop=True)
print(df_100_max)

# 0.3 - 0.7 is the second range
df_200 = df.loc[(df['Time-step'] >= 0.3) & (df['Time-step'] <= 0.7)]
df_200_max = df_200.loc[df['Volume'] == df_200['Volume'].max(), ['Time-step']].reset_index(drop=True)
df_200_min = df_200.loc[df['Volume'] == df_200['Volume'].min(), ['Time-step']].reset_index(drop=True)
print(df_200_min)
print(df_200_max)

df_300 = df.loc[(df['Time-step'] >= 0.7) & (df['Time-step'] <= 1.1)]
df_300_max = df_300.loc[df['Volume'] == df_300['Volume'].max(), ['Time-step']].reset_index(drop=True)
df_300_min = df_300.loc[df['Volume'] == df_300['Volume'].min(), ['Time-step']].reset_index(drop=True)
print(df_300_min)
print(df_300_max)

df_400 = df.loc[(df['Time-step'] >= 1.1) & (df['Time-step'] <= 1.5)]
df_400_max = df_400.loc[df['Volume'] == df_400['Volume'].max(), ['Time-step']].reset_index(drop=True)
df_400_min = df_400.loc[df['Volume'] == df_400['Volume'].min(), ['Time-step']].reset_index(drop=True)
print(df_400_min)
print(df_400_max)

# calculate 
ramp = df_100_max['Time-step']/100
systole1 = (df_200_min['Time-step'] - df_100_max['Time-step'])/200
diastole1 = (df_200_max['Time-step']-df_200_min['Time-step'])/200
systole2 = (df_300_min['Time-step'] - df_200_max['Time-step'])/200
diastole2 = (df_300_max['Time-step']-df_300_min['Time-step'])/200
systole3 = (df_400_min['Time-step'] - df_300_max['Time-step'])/200
diastole3 = (df_400_max['Time-step']-df_400_min['Time-step'])/200

# print the result 
print('ramp:')
print(ramp)
print('systole 1:')
print(systole1)
print('diastole 1:')
print(diastole1)
print('sysrtole 2:')
print(systole2)
print('diastole 2:')
print(diastole2)
print('systole 3:')
print(systole3)
print('diastole 3:')
print(diastole3)

# reshapre to a table, save to .txt
result = ramp.append(systole1.append(diastole1.append(systole2.append(diastole2.append(systole3.append(diastole3)))))).reset_index(drop=False)

result[''] = ["ramp" , "systole1" , "diastole1" ,"systole2","diastole2","systole3", "diastole3"]

result.to_csv(r'./ExtractTime.txt', header=None, index=None, sep=' ', mode='a')




