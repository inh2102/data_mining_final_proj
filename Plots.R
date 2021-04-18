setwd("~/Desktop/dm")
grouped_df_states <- read.csv("grouped_df_state_final.csv", header = T)
cdc_states <- read.csv("data_4_states_agg.csv", header = T)


grouped_df_states <- grouped_df_states[,-1]
cdc_states <- cdc_states[, -1]
colnames(cdc_states) <- c("state", "value")

library(ggplot2)
ggplot(data = cdc_states, 
       mapping = aes(y = Value))


library(usmap)
plot_usmap(regions="states", data = cdc_states, values = "value")+
  labs(title = "Reported Anxiety or Depression by State", "Mean Scores")


cdc_states$scaled <- cdc_states$value/42.515
plot(cdc_states$value, main = "Anxiety or Depression Values by State", 
     ylab = "Anxiety or Depression Scores", ylim = c(28,45))
#legend("bottomright",unique(cdc_states$state),cex=0.5)
#text(cdc_states ~value, labels=cdc_states$state,data=cdc_states, cex=0.9, font=2)


plot(grouped_df_states$ratio_depressed, col = "red", 
     main = "Ratio of Depressed Tweets by State",
     ylab ="Ratio of Depressed Tweets", ylim = c(0,0.9))

setwd("~/Desktop/dm")
gender_tweets <- read.csv("grouped_df_gender_final.csv", header = T)
cdc_gender <- read.csv("data_4_gender_agg.csv", header = T)


gender_tweets <- gender_tweets[,-1]
gender_tweets <- gender_tweets[-3,]

cdc_gender <- cdc_gender[, -1]
colnames(cdc_gender) <- c("state", "value")

barplot(space = 1.2, names.arg = c("Male", "Female"),
  cdc_gender$value, main = "Anxiety or Depression Values by Gender", 
  ylab = "Anxiety or Depression Scores", 
  ylim = c(0,50), col = "darkgreen",
  border = T, xlab =  "Gender")

barplot(space  = 1.2, names.arg = c("Female", "Male"),
        gender_tweets$ratio_depressed, 
        main = "Anxiety or Depression Tweets by Gender", 
        ylab = "Anxiety or Depression Tweet Ratio", 
        col = "lightblue",
        border = T, xlab =  "Gender")

cdc_states$scaled <- cdc_states$value/42.515
plot(cdc_states$scaled, main = "Anxiety or Depression Values by State", 
     ylab = "Anxiety or Depression Scores", ylim = c(-0.1,1))
points(grouped_df_states$ratio_depressed, col = "red")
legend("bottomright", legend = c("Scaled CDC Values", "Tweet Ratio"),
       col = c("black", "red"), pch = 1, cex = 0.5)