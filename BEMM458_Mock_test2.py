#######################################################################################################################################################
# 
# Name: Proawsaeng Katcharoen
# SID: 740094448
# Exam Date: 28 March 2025
# Module: BEMM458 Programming for Business Analytics
# Github link for this assignment: https://github.com/UniversityExeterBusinessSchool/mock-test-2-proawsaeng-katc.git
#
#######################################################################################################################################################
# Instruction 1. Read each question carefully and complete the scripts as instructed.

# Instruction 2. Only ethical and minimal use of AI is allowed. You may use AI to get advice on tool usage or language syntax, 
#                but not to generate code. Clearly indicate how and where you used AI.

# Instruction 3. Include comments explaining the logic of your code and the output as a comment below the code.

# Instruction 4. Commit to Git and upload to ELE once you finish.

#######################################################################################################################################################

# Question 1 - Loops and Lists
# You are given a list of numbers representing weekly sales in units.
weekly_sales = [120, 85, 100, 90, 110, 95, 130]

# Write a for loop that iterates through the list and prints whether each week's sales were above or below the average sales for the period.
# Calculate and print the average sales.

# Find average sales
i=0
avg_sales=0
for i in weekly_sales:
    avg_sales = avg_sales + i

avg_sales = avg_sales/len(weekly_sales)
print(avg_sales) #104.28571428571429

# for loop to find which week's sales were above or below the average

j = 0
for j in range(len(weekly_sales)):
    if  weekly_sales[j] < avg_sales:
        print("Week: ", j, " is below average")
    else:
        print("Week: ", j, " is above average")

#Week:  0  is above average
#Week:  1  is below average
#Week:  2  is below average
#Week:  3  is below average
#Week:  4  is above average
#Week:  5  is below average
#Week:  6  is above average


#######################################################################################################################################################

# Question 2 - String Manipulation
# A customer feedback string is provided:
customer_feedback = """The product was good but could be improved. I especially appreciated the customer support and fast response times."""

# Find the first and last occurrence of the words 'good' and 'improved' in the feedback using string methods.
# Store each position in a list as a tuple (start, end) for both words and print the list.


# define the target words
my_list = ['good', 'improved']

#for storing start and end location
my_coordinates = []

for i in my_list:
    start_loc = customer_feedback.find(i)
    wordlen = len(i)
    end_loc = start_loc + wordlen

    my_coordinates.append((start_loc,end_loc))

print(my_coordinates) #[(16, 20), (34, 42)]


#######################################################################################################################################################

# Question 3 - Functions for Business Metrics
# Define functions to calculate the following metrics, and call each function with sample values (use your student ID digits for customization).

# 1. Net Profit Margin: Calculate as (Net Profit / Revenue) * 100.
# 2. Customer Acquisition Cost (CAC): Calculate as (Total Marketing Cost / New Customers Acquired).
# 3. Net Promoter Score (NPS): Calculate as (Promoters - Detractors) / Total Respondents * 100.
# 4. Return on Investment (ROI): Calculate as (Net Gain from Investment / Investment Cost) * 100.

def NetProfitMargin(netprofit, revenue):
    return (netprofit/revenue) * 100


def Cac(totalmarketingcost, newcustomers):
    return (totalmarketingcost/newcustomers)


def Nps(promoters, detractors, totalrespon):
    return((promoters-detractors)/totalrespon*100)

def Roi(netgain, investcost):
    return((netgain/investcost)*100)

# test function (StudendID: 740094448)
print(NetProfitMargin(7400, 94448))
print(Cac(74009,448))
print(Nps(74,94,400))
print(Roi(74009,4448))

#######################################################################################################################################################

# Question 4 - Data Analysis with Pandas
# Using a dictionary sales_data, create a DataFrame from this dictionary, and display the DataFrame.
# Write code to calculate and print the cumulative monthly sales up to each month.
import pandas as pd

sales_data = {'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'], 'Sales': [200, 220, 210, 240, 250]}

#create and display dataframe
df = pd.DataFrame(sales_data)
print(df)

#cumulative monthly sales
cumulative_sales = []
total = 0

for i in range(len(df['Sales'])):
    total += df['Sales'][i]
    cumulative_sales.append(total)

#cumulative sales
print(cumulative_sales) #[200, 420, 630, 870, 1120]

#add new column to df for cumulative sales
df['Cumulative Sales'] = cumulative_sales
print(df)

#######################################################################################################################################################

# Question 5 - Linear Regression for Forecasting
# Using the dataset below, create a linear regression model to predict the demand for given prices.
# Predict the demand if the company sets the price at £26. Show a scatter plot of the data points and plot the regression line.

# Price (£): 15, 18, 20, 22, 25, 27, 30
# Demand (Units): 200, 180, 170, 160, 150, 140, 130

import matplotlib.pyplot as plt
import statsmodels.api as sm

#make dataframe to store data
data = pd.DataFrame({"Price":[15, 18, 20, 22, 25, 27, 30], "Demand":[200, 180, 170, 160, 150, 140, 130]})

#values for plot
x = data['Price']
y = data['Demand']

model = sm.OLS(y,sm.add_constant(x))
result = model.fit()

x_pre = sm.add_constant(x)
y_pre = result.predict(x_pre)

#values for prediction
newprice = pd.DataFrame({"Price":[26]})
newprice_cons = sm.add_constant(newprice, has_constant='add')
predictdemand = result.predict(newprice_cons)

plt.scatter(x, y, color='blue', label='Actual Data')
plt.plot(x, y_pre, color='red', label='Regression Line')
plt.scatter(26, predictdemand.iloc[0], color='green', label='Predicted at £26')

plt.xlabel('Price (£)')
plt.ylabel('Demand (Units)')
plt.title('Linear Regression: Price vs Demand')
plt.legend()
plt.grid(True)
plt.show()


#######################################################################################################################################################

# Question 6 - Error Handling
# You are given a dictionary of prices for different products.
prices = {'A': 50, 'B': 75, 'C': 'unknown', 'D': 30}

# Write a function to calculate the total price of all items, handling any non-numeric values by skipping them.
# Include error handling in your function and explain where and why it’s needed.

#function for calculating total price

def TotalPrice(price):
    total = 0
    for key, value in prices.items():
        if type(value) not in (int, float): #Error Handling is here to skip other datatype that's not numeric
            continue
        total += value
    
    return total

print(TotalPrice(prices))

#######################################################################################################################################################

# Question 7 - Plotting and Visualization
# Generate 50 random numbers between 1 and 500, then:
# Plot a histogram to visualize the distribution of these numbers.
# Add appropriate labels for the x-axis and y-axis, and include a title for the histogram.

import random

numbers = [random.randint(1,500) for i in range(50)]

#print(len(numbers))

plt.hist(numbers)
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Distribution of 50 random numbers')
plt.show()

#######################################################################################################################################################

# Question 8 - List Comprehensions
# Given a list of integers representing order quantities.
quantities = [5, 12, 9, 15, 7, 10]

# Use a list comprehension to create a new list that doubles each quantity that is 10 or more.
# Print the original and the new lists.

#######################################################################################################################################################

# Question 9 - Dictionary Manipulation
# Using the dictionary below, filter out the products with a rating of less than 4 and create a new dictionary with the remaining products.
ratings = {'product_A': 4, 'product_B': 5, 'product_C': 3, 'product_D': 2, 'product_E': 5}

#######################################################################################################################################################

# Question 10 - Debugging and Correcting Code
# The following code intends to calculate the average of a list of numbers, but it contains errors:
values = [10, 20, 30, 40, 50]
total = 0
for i in values:
    total = total + i
average = total / len(values)
print("The average is" + average)

# Identify and correct the errors in the code.
# Comment on each error and explain your fixes.

#######################################################################################################################################################
