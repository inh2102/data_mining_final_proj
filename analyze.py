import pandas as pd 

df = pd.read_csv('Indicators_of_Anxiety_or_Depression_Based_on_Reported_Frequency_of_Symptoms_During_Last_7_Days.csv')

df = df[df['Indicator'] == 'Symptoms of Anxiety Disorder or Depressive Disorder']

df.drop(['Quartile Range', 'Confidence Interval', 'High CI', 'Low CI', 
	     'Time Period Start Date', 'Time Period End Date'], axis=1, inplace=True)

df.to_csv('data_2.csv')

df = pd.read_csv('data_2.csv')

df_states = df[df['State'] != 'United States']
df_states.drop('Unnamed: 0', axis=1, inplace=True)
df_states = df_states[df_states['Value'].notna()]
df_states.to_csv('data_3_states.csv')

df_gender = df[(df['State'] == 'United States') & ((df['Subgroup'] == 'Male') | (df['Subgroup'] == 'Female'))]
df_gender.drop('Unnamed: 0', axis=1, inplace=True)
df_gender = df_gender[df_gender['Value'].notna()]
df_gender.to_csv('data_3_gender.csv')

df_states = pd.read_csv('data_3_states.csv')
df_gender = pd.read_csv('data_3_gender.csv')

states = list(set(df_states['State'].values.tolist()))

df_states_agg = pd.DataFrame({}, columns=['State', 'Value'])

for i, state in enumerate(states):
	state_mean = df_states[df_states['State'] == state]['Value'].mean()
	df_states_agg.loc[i] = [state, round(state_mean, 3)]

df_states_agg.to_csv('data_4_states_agg.csv')

genders = list(set(df_gender['Subgroup'].values.tolist()))

df_gender_agg = pd.DataFrame({}, columns=['Gender', 'Value'])

for j, gender in enumerate(genders):
	gender_mean = df_gender[df_gender['Subgroup'] == gender]['Value'].mean()
	df_gender_agg.loc[j] = [gender, round(gender_mean, 3)]

df_gender_agg.to_csv('data_4_gender_agg.csv')




