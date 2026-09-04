#List
#Q1. Create a list of 10 student grades. Print the highest grade, the lowest grade, and the average grade without using pandas

grades = [85, 92, 78, 90, 65, 88, 95, 72, 81, 89]

highest = max(grades)
lowest = min(grades)
average = sum(grades) / len(grades)

print(f"Highest Grade: {highest}")
print(f"Lowest Grade: {lowest}")
print(f"Average Grade: {average:.2f}")

#----------------------------------------------------------------------------------------------------------------------------------------------

#Q2. You have a list of product prices. Add a new price, remove the most expensive price, then sort the remaining prices in descending order. 

prices = [150.0, 450.0, 200.0, 890.0, 310.0]

prices.append(500.0)

prices.remove(max(prices))

prices.sort(reverse=True)

print("Updated prices:", prices)

#----------------------------------------------------------------------------------------------------------------------------------------------

#Q3. Given two lists of employee IDs, create a new list that contains only the IDs that appear in both lists without using set()

list1 = [101, 102, 103, 104, 105]
list2 = [103, 105, 106, 107, 101]

common_ids = []
for emp_id in list1:
    if emp_id in list2 and emp_id not in common_ids:
        common_ids.append(emp_id)

print("Common Employee IDs:", common_ids)

#----------------------------------------------------------------------------------------------------------------------------------------------

#Sets

#Q1. Create two sets of course names and display the common courses between them. 

set1 = {"Python", "Data Science", "SQL", "Machine Learning"}
set2 = {"Web Dev", "SQL", "Python", "Cybersecurity"}

common_courses = set1.intersection(set2)

print("Common Courses:", common_courses)

#--------------------------------------------------------------------------------------------------------------------------

#ََQ2. Given a list containing duplicate customer IDs, convert it to a set and print the unique IDs

customer_ids = [1001, 1002, 1001, 1003, 1002, 1004, 1005]

unique_ids = set(customer_ids)
print("Unique Customer IDs:", unique_ids)

##----------------------------------------------------------------------------------------------------------------------------

