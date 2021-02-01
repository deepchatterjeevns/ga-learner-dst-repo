### Project Overview

 **Problem Statement**

We are working in the Amazon company as a Data Scientist. We want to focus on customer reviews of our Alexa product. So our aim is to classify the unhappy customers based on the features 'rating', 'date', 'variation', 'verified_reviews' and 'feedback'.

The dataset has details of 3150 house entries with the following 5 features:

- Feature	- Description
- rating	- Product ratings (1/2/3/4/5)
- date	- Rating date
- variation	- Product type
- verified_reviews	- Reviews given by customer
- feedback	- Feedback given by customer (0/1)


### Learnings from the project

 After completing this project, I have a better understanding of how to carryout sentiment analysis. In this project, I have applied the following concepts.

- Train-Test Split
- Poster Stemmer
- Text Cleaning
- Random Forest Classifier
- Metrics for Classification


### Approach taken to solve the problem

 My approach was to:

1. Load the train data and visualize Product Ratings vs Feedback and Product Variation vs Feedback.
2. Cleaning and preparing the corpus of data for analysis using regex, tokenization, stemming.
3. Instantiating count vectorizer and then specifying Independent and Dependent variables followed by splitting the data further into Train and Validation datasets.
4. Sampling the training datasets and then fitting Random Forest Classifier algorithm on the training dataset and predicting on the test dataset.
5. Using Accuracy Score and Precision to evaluate our prediction.
6. Using SMOTE form imblearn package to oversample the minority class.
7. Repeated steps 4 and 5 to find the Accuracy Score and Precision.
8. Used the model having highest Accuracy Score and Precision to predict the test data before submission,