# A-B_Data_Testing
A/B Testing Data Analysis Project
This project analyzes A/B test results using Python, focusing on calculating conversion rates and conducting statistical tests to determine if there is a significant difference between two groups (A and B) in a sample dataset. This kind of analysis is commonly used in business settings to make data-driven decisions about product changes, user experience improvements, or marketing strategies.

Project Overview
In this project:

I use a fictional dataset stored in ab_test_data.txt, which contains information about users in two groups (A and B).
The analysis calculates the conversion rate for each group and performs a t-test to determine if the difference in conversion rates is statistically significant.
Data
The data file, ab_test_data.txt, contains the following columns:
UserID: Unique identifier for each user.
Group: Specifies the group each user is in (A for the control group, B for the test group).
Converted: 1 if the user completed the desired action (e.g., made a purchase, booked a ride), 0 otherwise.
