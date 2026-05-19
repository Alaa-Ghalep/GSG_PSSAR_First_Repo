
import pandas as pd


DF1=pd.read_csv('raw_data/student_coffee_crisis.csv')
print ("Data Frame For csv File : ");
print (DF1.head());

DF2 = pd.read_excel('raw_data/student_coffee_crisis.xlsx')
print ("Data Frame For xlsx File : ");
print("Excel:", DF2.head())

DF3 = pd.read_json('raw_data/student_coffee_crisis.json')
print ("Data Frame For json File : ");
print("JSON:", DF3.head())

DF4 = pd.read_parquet('raw_data/student_coffee_crisis.parquet')
print ("Data Frame For parquet File : ");
print("Parquet:", DF4.head())

# Parquet info 
print("\n" + "=" * 50)
print("Parquet Info:")
print("=" * 50)
print(f"Raw Number : {DF4.shape[0]}")
print(f"Columns Number : {DF4.shape[1]}")
print(f"Columns Names : {list(DF4.columns)}")
print("\n" + "=" * 50)
print(DF4.describe())