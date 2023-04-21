import pandas as pd


def analyze_demographic_data():

  df = pd.read_csv('adult.data.csv')

  race_nbr = df['race'].value_counts()

  men_avg = round(df[df['sex'] == 'Male']['age'].mean(), 1)

  bach_percentage = round(
    df[df['education'] == 'Bachelors'].shape[0] / df.shape[0] * 100, 1)
  a1 = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
  a2 = df['salary'] == '>50K'
  advanced_education_50k = round((a1 & a2).sum() / a1.sum() * 100, 1)
  lower_education_50k = round((~a1 & a2).sum() / (~a1).sum() * 100, 1)
  min_hours = df['hours-per-week'].min()
  b = df['hours-per-week'] == min_hours
  min_hours_50k = round((a2 & b).sum() / (b).sum() * 100, 1)

  c = (df[a2]['native-country'].value_counts() /
       df['native-country'].value_counts() * 100).sort_values(ascending=False)

  country_50k = c.index[0]
  country_50k_percentage = round(c.iloc[0], 1)

  india_50k_occupation=df[(df['native-country']=='India') & a2]\
                          ['occupation'].value_counts().index[0]

  print('How many people of each race are represented in this dataset: \n',
        race_nbr)
  print('What is the average age of men: ', men_avg)
  print('What is the percentage of people who have a Bachelors degree: ',
        bach_percentage)
  print(
    'What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K: ',
    advanced_education_50k)
  print(
    'What percentage of people without advanced education make more than 50K :',
    lower_education_50k)
  print('What is the minimum number of hours a person works per week: ',
        min_hours)
  print(
    'What percentage of the people who work the minimum number of hours per week have a salary of more than 50K :',
    min_hours_50k)
  print('What country has the highest percentage of people that earn >50K: ',
        country_50k)
  print('what is that percentage: ', country_50k_percentage)
  print(
    'Identify the most popular occupation for those who earn >50K in India :',
    india_50k_occupation)
