# twittersentimentscore

This code assigns a sentiment score for a given hashtag input based on the most recent 100 tweets utilising the VADER (Valence Aware Dictionary and sEntiment Reasoner) python library.

The code shows the 100 most recent #htz tweets and assigns a compound score to each tweet (the #htz can be easily changed into any other relevant hashtags). To get an overall compound score from the latest 100 tweets, I took the mean of all the individual compound scores.

## Interpreting the 'Overall Compound Score':

positive sentiment : (compound score >= 0.05)

neutral sentiment : (compound score > -0.05) and (compound score < 0.05)

negative sentiment : (compound score <= -0.05)
