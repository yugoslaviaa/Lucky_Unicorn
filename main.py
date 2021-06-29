# Integer checking function
def intchecker(question,low, high): 
  valid = False 
  while not valid: 
    error = f"Whoops! Please enter an integer between {low} and {high}"
    try: 
      response = int(input(question.format(low, high)))
      if low <= response <= high: 
        return response
      else: 
        print(error)
        print()

    except ValueError: 
      print(error)


# Main routine
user_balance = intchecker("How much money would you like to play with? ", 1, 10)
