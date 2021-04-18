import pandas as pd

# Read data frames
combined_df = pd.read_csv('combined_sample.csv')
grouped_state_df = pd.read_csv('grouped_df_state.csv')
grouped_state_df['num_depressed'] = 0
grouped_state_df['ratio_depressed'] = 0

grouped_gender_df = pd.read_csv('grouped_df_gender.csv')
grouped_gender_df['num_depressed'] = 0
grouped_gender_df['ratio_depressed'] = 0

# Get states and genders
states = list(set(combined_df['state'].values.tolist()))
genders = list(set(combined_df['gender'].values.tolist()))

# Grouped State
for state in states:
	combined_state_df = combined_df[combined_df['state'] == state]

	num_depressed = len(combined_state_df[combined_state_df['depressed'] == 1])
	num_nondepressed = len(combined_state_df[combined_state_df['depressed'] == 0])
	assert num_depressed + num_nondepressed == len(combined_state_df)

	grouped_state_df.loc[grouped_state_df['state'] == state, 'num_depressed'] = num_depressed
	grouped_state_df.loc[grouped_state_df['state'] == state, 'ratio_depressed'] = round(num_depressed / len(combined_state_df), 4)

# Grouped Gender
for gender in genders:
	if str(gender) == 'nan':
		continue
	combined_gender_df = combined_df[combined_df['gender'] == gender]

	num_depressed = len(combined_gender_df[combined_gender_df['depressed'] == 1])
	num_nondepressed = len(combined_gender_df[combined_gender_df['depressed'] == 0])
	assert num_depressed + num_nondepressed == len(combined_gender_df)

	grouped_gender_df.loc[grouped_gender_df['gender'] == gender, 'num_depressed'] = num_depressed
	grouped_gender_df.loc[grouped_gender_df['gender'] == gender, 'ratio_depressed'] = round(num_depressed / len(combined_gender_df), 4)

# File saving
grouped_state_df.to_csv('grouped_df_state_final.csv')
grouped_gender_df.to_csv('grouped_df_gender_final.csv')

