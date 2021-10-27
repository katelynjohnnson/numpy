## Numpy Exercise 2
import numpy as np

## This array documnets the last 5 sales for each of Superstore's four cash registers. 
salesArray = np.array([[150.68,207.99,107.88,58.99,60.59],[20.89,98.99,258.62,19.76,101.59],[70.66,190.10,134.54,200.14,15.59],[10.52,201.59,140.55,13.99,45.98]])

## Step 1: Print the total sales for the store.
print("-----------------------------------------------   STEP ONE   -----------------------------------------------")
total = salesArray.sum()
print("Total sale of store: ", total)

## Step 2: What was Superstore's smallest and largest sale? Print them.
print("-----------------------------------------------   STEP TWO   -----------------------------------------------")
largest = np.max(salesArray)
smallest = np.min(salesArray)
print('Largest sale of superstore: ', largest)
print('Smallest sale of the superstore: ', smallest)

## Step 3: Print an array that will show which sales are greater than or equal to $100.
print("-----------------------------------------------   STEP THREE  -----------------------------------------------")
print('Values bigger than $100 = ', salesArray[salesArray>=100])

## Step 4: Print the total sales for each register.
print("-----------------------------------------------   STEP FOUR   -----------------------------------------------")
sale_each = np.sum(salesArray, axis = 1)
for i in range (len(sale_each)):
    print('Register', i+1, 'sale: ',sale_each[i])

## Step 5: Superstore is a cashless store and needs to calculate their owed credit card fees. Each sale is subject to a 2% credit card fee.
#           Using the salesArray, create a new array that stores the 2% fee for each sale and register. Print the array and then print the total fees.
print("-----------------------------------------------   STEP FIVE  -----------------------------------------------")
credit = []
for i in range(len(salesArray)):
    x = []
    for j in range(len(salesArray[0])):
        c = 0.02 * salesArray[i][j]
        c = (round(c,2))

        x.append(c)
    credit.append(x)

total_fee = sum(map(sum, credit))
for i in credit:
    print(i)
print('total fee: ', round(total_fee, 2))

## Step 6: Using your fee array and salesArray, calculate how much profit Superstore made for each sale after paying credit card fees. Store this in a new array and print it.
print("-----------------------------------------------   STEP SIX  -----------------------------------------------")
profit_arr = []
for i in range(len(credit)):
    y = []
    for j in range(len(credit[0])):
        a = salesArray[i][j] - credit[i][j]
        a = round(a,2)
        y.append(a)
    profit_arr.append(y)
total_profit = sum(map(sum,profit_arr))
for i in profit_arr:
    print(i)
print('Total profit: ', total_profit)

## Step 7: Print the sales only for the second and forth cash register
print("-----------------------------------------------   STEP SEVEN  -----------------------------------------------")
for i in range(1, len(salesArray),2):   
    print(salesArray[i])

## Step 8: Superstore has added a 5th cash register who's data is stored in the array newRegister. Add the new register to the original array. Print the updated salesArray.
print("-----------------------------------------------   STEP EIGHT  -----------------------------------------------")
newRegister = np.array([17.89,13.59,107.89,176.88,56.78])
salesArray = np.concatenate((salesArray, newRegister), axis=0)
for i in salesArray:
    print(i)

## Step 9: Register #3 had an error and recorded it's fourth sale ($200.14) incorrectly. The sale should have been $20.14. Update the array to correct this error.
#           Print the array before and after the update to see the change.
print("-----------------------------------------------   STEP NINE  -----------------------------------------------")
print('before: ')
for i in salesArray:
    print(i)
salesArray[2][3] = 20.14
print('after: ')
for i in salesArray:
    print(i)

