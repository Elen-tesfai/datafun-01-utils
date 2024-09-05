''' ITERATION 1

Module: Elen Analytics - Reusable Module for My Data Analytics Projects

This module provides a simple, reusable foundation for my analytics projects. 
When we work hard to write useful code, we want it to be reusable.
A good byline could be used in every Python analytics project we do.

Process:

We don't write code from top to bottom; instead, we often write it from the outside in.
Here's what a first draft of my utils_case.py might look like:

1. I start with this docstring at the very beginning.
   I use it to clarify the purpose of my Python file and organize my thoughts.
   
2. I'll declare a global variable for my byline string and just set it to some simple text.

3. I'll declare a main() function for my module. When I run this script, I can use main() to test my byline.

4. I'll add the boilerplate conditional execution code so I only run the main() function when 
   this script is executed directly (but not when I import it into another file).

I'll test it in an online interpreter to ensure this version runs correctly before continuing.
'''

#####################################
# Declare a global variable named byline.
#####################################

byline: str = 'Elen Analytics: Delivering Professional Insights'
def get_byline() -> str:
    return byline
#####################################
# Define a main() function for this module.
#####################################

# Create a function named main.
# A function is a block of code that performs a specific task.
# This function will simply print the byline to the console.
# Add a type hint to indicate that this function doesn't return anything when called 
# (that is, it has a Python type of None).
# It doesn't need any additional information passed in, 
# so there's nothing needed inside the parentheses.
# Everything afer the colon (:) must be indented (usually 4 spaces)

def main() -> None:
    '''Print the byline to the console when this function is called.'''
    print(get_byline())

#####################################
# Conditional Execution - Only call main () when executing this module as a script.
#####################################

if __name__ == '__main__':
    main()
    
''' ITERATION 2 
Module: Elen Analytics: Delivering Professional Insights

This module provides a simple, reusable foundation for my analytics projects. 
When we work hard to write useful code, we want it to be reusable.
A good byline could be used in every Python analytics project we do.
Process:
Second iteration adds a function to return a string via byline.
I’ll create a function named get_byline().
It’ll return by line to whatever calls the get_byline() function.
I’ll update the main() function to use the new get_byline() function 

Same conditional boilerplate at the end.
I’ll test this version before adding more code that show:
-	My ability to declare variables of different types
-	My ability to use python to calculate basic descriptive statistics'''
#####################################
# Declare a global variable named byline.
#####################################

byline: str ='Elen Analytics: Delivering Professional Insights'

def get_byline() -> str:
    '''Return a byline for the project.'''
    return byline
    
#####################################
# Define a main () function for this module.
#####################################

# Main function calls get_byline() to retrieve the byline.
def main () -> None:
    '''Print the byline to the console when this function is called.'''
    print(get_byline())

#####################################
# Conditional Execution - Only call main () when executing this module as a script.
#####################################

if __name__ == '__main__':
    main ()    
''' ITERATION 3
  Module: 'Elen Analytics: Delivering Professional Insights'
 
 This module proves a simple, reusable foundation for my analytics projects

Process:
Declare additional variables to show skills with different data types.
'''
#####################################
# Declare global variables - keep byline at the end
# We will use this information in a smarter byline
#####################################

# Boolean variable to indicate if the company has international clients
has_international_clients: bool = True

# Integer variable for the number of years in operation
years_in_operation: int = 10 
    
# List of strings representing the skills offered by the company
skills_offered: list = ["Data Analysis", "Machine Learning", "Business Intelligence"]

# List of floats representing individual client satisfaction scores
client_satisfaction_scores: list = [4.8, 4.6, 4.9, 5.0, 4.7]

#####################################
# Declare a global variable named byline
# Make it a multiline f-string to show our information
#####################################

byline: str = f"""

-----------------------------------------------------------
Elen Analytics: Delivering Professional Insights
----------------------------------------------------------

Has International Clients: {has_international_clients}
Years in Operation:        {years_in_operation}
Skills Offered:            {skills_offered }
Client Satisfaction Scores: {client_satisfaction_scores}
"""
#####################################
# Define the get_byline() function
#####################################  

def get_byline() -> str:
    '''Return a buline for my analytics projects.'''
    return byline
    
#########################################
# Define a main() function for this module.
#########################################

def main() -> None:
    '''Print results of get_byline() when main() is called.'''
    print(get_byline())
