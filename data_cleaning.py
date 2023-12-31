# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 20:08:03 2023

@author: HP
"""

import pandas as pd

df = pd.read_csv('glassdoor_jobs.csv')

# salary parsing


df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['employee_provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary:' in x.lower() else 0)

df = df[df['Salary Estimate'] != '-1']

salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])

minus_Kd = salary.apply(lambda x: x.replace('K','').replace('$',''))

min_hr = minus_Kd.apply(lambda x : x.lower().replace('per hour','').replace('employer provided salary:',''))

df['min_salary'] = min_hr.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = min_hr.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df.min_salary+df.max_salary)/2

# company name text only

df['compant_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating'] < 0 else x['Company Name'][:-3], axis = 1)
# state field
df['job_state'] = df['Location'].apply(lambda x:x.split(',')[1])

# run below line for getting counts
df.job_state.value_counts()

# run below line to get columns of data frame
df.columns
df['same_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis = 1)

#age of company
df['age'] = df.Founded.apply(lambda x: x if x< 1 else 2023 - x)

# parsing of job description (python, etc.)

# df['Job Description'] = 

#python
df['python_yn'] = df['Job Description'].apply(lambda x:1 if 'python' in x.lower() else 0)

# r_studio
df['r_studio_yn'] = df['Job Description'].apply(lambda x:1 if 'r_studio' in x.lower() else 0)

# spark
df['spark_yn'] = df['Job Description'].apply(lambda x:1 if 'spark' in x.lower() else 0)

# aws
df['aws_yn'] = df['Job Description'].apply(lambda x:1 if 'aws' in x.lower() else 0)


# excel
df['excel_yn'] = df['Job Description'].apply(lambda x:1 if 'excel' in x.lower() else 0)



df.aws_yn.value_counts()

df_out = df.drop(['Unnamed: 0'],axis =1)

df_out.to_csv('salary_data_cleaned.csv',index = False)

pd.read_csv('salary_data_cleaned.csv')


