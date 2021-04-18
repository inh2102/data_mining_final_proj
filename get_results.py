import pandas as pd
from scipy.stats.stats import pearsonr

# Read data frames
cdc_states_df = pd.read_csv('data_4_states_agg.csv')
tweet_states_df = pd.read_csv('grouped_df_state_final.csv')

cdc_genders_df = pd.read_csv('data_4_gender_agg.csv')
tweet_genders_df = pd.read_csv('grouped_df_gender_final.csv')

# States Correlation
states = list(set(cdc_states_df['State'].values.tolist()))
states_ = list(set(tweet_states_df['state'].values.tolist()))
states = list(set(states) & set(states_))
print('Found %d States!' % len(states))

states_names, states_v, states_r = [], [], []
for i, state in enumerate(states):
	v = cdc_states_df[cdc_states_df['State'] == state]['Value'].values.tolist()[0]
	r = tweet_states_df[tweet_states_df['state'] == state]['ratio_depressed'].values.tolist()[0]

	states_names.append(state)
	states_v.append(v)
	states_r.append(r)

coeff, p_value = pearsonr(states_v, states_r)[0], pearsonr(states_v, states_r)[1]

print('[STATES] Pearson Correlation Coefficient: ', coeff)
print('[STATES] p-value: ', p_value)

# Gender Correlation
genders = list(set(cdc_genders_df['Gender'].values.tolist()))
genders = [gender.lower() for gender in genders]
genders_ = list(set(tweet_genders_df['gender'].values.tolist()))
genders_ = [str(gender_).lower() for gender_ in genders_]

genders = list(set(genders) & set(genders_))
print('Found %d Genders!' % len(genders))

genders_names, genders_v, genders_r = [], [], []
for i, gender in enumerate(genders):
	if str(gender) == 'nan':
		continue

	v = cdc_genders_df[cdc_genders_df['Gender'] == gender.capitalize()]['Value'].values.tolist()[0]
	r = tweet_genders_df[tweet_genders_df['gender'] == gender]['ratio_depressed'].values.tolist()[0]

	genders_names.append(gender)
	genders_v.append(v)
	genders_r.append(r)

coeff, p_value = pearsonr(genders_v, genders_r)[0], pearsonr(genders_v, genders_r)[1]

print('[GENDERS] Pearson Correlation Coefficient: ', coeff)
print('[GENDERS] p-value: ', p_value)

