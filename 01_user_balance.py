"""Component 1 of Lucky Unicorn
Get amount user wants to play with
Created by Shaun Reynolds
28/06/21"""

# Integer checking function
def intchecker(question, low, high): 
  valid = False 
  while not valid: 
    error = f"Whoops! Please enter an integer between {low} and {high}: "
    try: 
      response = int(input(f"Please enter an integer between {low} and {high}: ")))
      if low <= response <= high: 
        return response
      else: 
        print(error)
        print()

    except ValueError: 
      print(error)


# Main routine
user_balance = integer_checker("How much money would you like to play with? ", 1, 10)
