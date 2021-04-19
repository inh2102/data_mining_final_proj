setwd("~/Desktop/dm")
grouped_df_states <- read.csv("grouped_df_state_final.csv", header = T)
cdc_states <- read.csv("data_4_states_agg.csv", header = T)

#Remove empty cols 
grouped_df_states <- grouped_df_states[,-1]
cdc_states <- cdc_states[, -1]
colnames(cdc_states) <- c("state", "value")

#Convert state names to abbreviations in new column
cdc_states$state_ab <- state.abb[match(cdc_states$state,state.name)]

#Scale states 
cdc_states$scaled <- cdc_states$value/42.515

#Plot CDC means by state
plot(cdc_states$value, main = "Anxiety or Depression Values by State", 
     ylab = "Mean Anxiety or Depression Scores", xlab="State (Alphabetical Order)", 
     ylim = c(28,45), cex.lab = 0.8)
text(cdc_states$value, labels=cdc_states$state_ab,data=cdc_states, 
     cex=0.4, font=0.4, pos=3, col = "blue")

#Convert state names to abbreviations in new column
grouped_df_states$state_ab <- state.abb[match(grouped_df_states$state,state.name)]

#Plot depressive/anxious tweet ratio by state  
plot(grouped_df_states$ratio_depressed, col = "red", 
     main = "Ratio of Anxious or Depressed Tweets by State",
     ylab ="Ratio of Anxous or Depressed Tweets", ylim = c(0,0.9), cex.lab = 0.8,
     xlab = "State (Alphabetical Order)")
text(grouped_df_states$ratio_depressed, labels=grouped_df_states$state_ab,
     data=grouped_df_states, 
     cex=0.4, font=0.4, pos=3)


plot(scale(cdc_states$scaled), ylim = c(-3, 3))
points(scale(grouped_df_states$ratio_depressed, center = T, scale =T), col= "red")



setwd("~/Desktop/dm")
gender_tweets <- read.csv("grouped_df_gender_final.csv", header = T)
cdc_gender <- read.csv("data_4_gender_agg.csv", header = T)

#remove empty rows and columns
gender_tweets <- gender_tweets[,-1]
gender_tweets <- gender_tweets[-3,]

cdc_gender <- cdc_gender[, -1]

#format so everything is the same between two datasets.
colnames(cdc_gender) <- c("gender", "value")

#Plot CDC means by gender 
barplot(space = 1.2, names.arg = c("Female", "Male"),
  cdc_gender$value, main = "Anxiety or Depression Values by Gender", 
  ylab = "Anxiety or Depression Scores", 
  ylim = c(0,50), col = "darkgreen",
  border = T, xlab =  "Gender")

#Plot ratio of tweeted anxiety or depression by gender  
tweet_plot_gender <- barplot(space  = 1.2, names.arg = c("Female", "Male"),
        gender_tweets$ratio_depressed, 
        main = "Anxiety or Depression Tweets by Gender", 
        ylab = "Anxiety or Depression Tweet Ratio", 
        col = "lightblue", ylim = c(0, 0.6),
        border = T, xlab =  "Gender")


#Plot the scaled CDC means and the depressive or anxious tweet ratio
cdc_states$scaled <- cdc_states$value/42.515
plot(cdc_states$scaled, main = "Anxiety or Depression Values by State", 
     ylab = "Anxiety or Depression Scores", xlab = "State (Alphabetical Order)",
     ylim = c(-0.1,1.1), cex.lab = 0.8)
points(grouped_df_states$ratio_depressed, col = "red")
text(grouped_df_states$ratio_depressed, labels=grouped_df_states$state_ab,
     data=grouped_df_states, 
     cex=0.4, font=0.4, pos=3)
legend("bottomright", legend = c("Scaled CDC Values", "Tweet Ratio"),
       col = c("black", "red"), pch = 1, cex = 0.6)