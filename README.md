## Final Project, Applied Data Mining

# Summary / Abstract:

> Due to our concerns about mental health in light of the COVID-19 pandemic, we seek to study the manifestation of expressing specific ideations on social media. In this project, we track the frequency of tweets demonstrating depression or anxiety with specific regard to tweeters’ gender, U.S. state of residency, and word usage. To properly classify depressed or anxious tweets, we primarily use a corpus of Facebook comments labeled as such by NIH researchers to train a Random Forest model using tf-idf for classification. We use this classification model to predict whether or not our sample’s 10,000 collected tweets are depressed/anxious (or not); and we study the relationship between this label, gender, and U.S. state. Finally, we use CDC data on self-reported levels of anxiety and depression by state and gender to mine our data, observe whether reported anxiety or depression maps onto tweeted anxiety or depression by gender and states, and identify outlier values with large differences between CDC and Twitter data sources. We find that females and males display the opposite behaviors and sentiments online as compared to what one would expect from reported anxiety or depression levels. We do not see a relationship as strong and distinct within states; we cannot say with confidence that the reported anxiety or depression was reflected in sentiment from the tweets within those states. More research is needed to explore such a relationship, and in the future, we would approach the problem using newer natural language processing techniques or domain-specific psycholinguistic methods, using the one with highest accuracy. > 
> 

# Implementation / Replication:

To replicate our paper, refer to the following files:

- plot_tweet_and_cdc_scores.R for plots of CDC anxiety/depression scores and of ratio of depressed/anxious tweets
- y for y
- z for z
