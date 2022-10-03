# in this problem, you will practice building the function shown in class
# by splitting each calculation up into separate variables, using the
# previous variable in the subsequent calculation.
# use the print function under the variables to make sure they're right


principal = 1000  # initial amount to be deposited
rate = 1  # interest rate applied to deposit (will be divided by 100)
n = 10  # number of years to compound deposit

# your equation should be functionally the same as this:
# final = principal * ((1 + (rate / 100)) ** n)
# hint: look at the amount of variables, and do not delete anything
# in the variable declarations, only add operators, numbers, or other variables.
# the first one has been done for you

# write your variables here:
rt = rate / 100
rtn1 = rt
rtn1_sqrd = rtn1
final = principal

# final should be around 1105
print(final)

# ----------------------------------------------------------------------------------------------------------------------

# now, build the logistic growth formula using the variables below:
r = 0.7
N = 150
K = 300

# write the equation here, using the variable names:
# hint: growth should be around 53; print it to check
growth = None

print(growth)
