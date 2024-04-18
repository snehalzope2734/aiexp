pip install pyDatalog
from pyDatalog import pyDatalog

# Define the PyDatalog program
pyDatalog.create_terms('factorial, N')

# Define the factorial rule recursively
factorial[N] = N * factorial[N-1]
factorial[1] = 1

# Query to calculate factorial
result = factorial[N] == 120

# Print the result
print(result)
