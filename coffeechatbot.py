# The cafe is selling everything for $4.50!

# Define your functions
def coffee_bot():
  print("Welcome to the cafe!")
  drink_type = get_drink_type()
  size = get_size()
  drink = size + drink_type 
  print("So your drink will be" + drink)
  name = input("Can I get a name? ")
  print("So that's a" + drink +  " for " + name + "\nThat'll be that $4.50!")
def print_message():
  print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")
def get_size():
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
  if res == 'a' or res == 'Small' or res == 'small' or res == 'A':
    return ' Small'
  elif res == 'b' or res == 'Medium' or res == 'medium' or res == "B":
    return ' Medium'
  elif res == 'c' or res == 'Large' or res == 'large' or res == 'C':
    return ' Large'
  else:
    print_message()
    return get_size()
def print_message():
  print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")
def get_drink_type():
  res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n[d] Americano \n[e] Frappucino \n> ')
  if res == 'a' or res == 'Brewed Coffee' or res == 'brewed coffee' or res == 'A':
    return ' Brewed Coffee'
  elif res == 'b' or res == 'Mocha' or res == 'mocha' or res == 'B':
    return ' Mocha'
  elif res == 'c' or res == 'Latte' or res == 'latte' or res == 'C':
    return order_latte()
  elif res == 'd' or res == 'Americano' or res == 'americano' or res == 'D': 
    return order_americano()
  elif res == 'e' or res == 'frappucino' or res == 'Frappucino' or res == 'E' or res == 'frappe' or res == 'Frappe':
    return order_frappe()
  else:
    print_message()
    return get_drink_type()
def order_latte():
 res = input('And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n> ')
 if res == 'a' or res == 'A' or res == '2% milk' or res == '2% Milk':
   return ' latte'
 elif res == 'b' or res == 'B' or res == 'Non-fat milk' or res == 'non-fat milk' or res == 'Non-Fat Milk' or res == 'non-fat Milk':
   return ' non-fat latte' 
 elif res == 'c' or res == 'C' or res == 'soy milk' or res == 'Soy milk' or res == 'Soy Milk':
   return ' soy latte'
 else:
   print_message()
   return order_latte()
def order_americano():
  res = input('And what kind of Americano would you like? \n[a] Black \n[b] With sugar \n> ')
  if res == 'a' or res == 'A' or res == 'black' or res == 'Black':
    return ' Black Americano'
  elif res == 'b' or res == 'B' or res == 'with sugar' or res == 'With sugar' or res == 'with Sugar' or res == 'With Sugar' or res == 'sugar' or res == 'Sugar':
    return ' Americano with sugar'
  else:
    print_message()
    return order_americano()
def order_frappe():
  res = input("Would you like any extra toppings for your Frappe? \n[a] Caramel sauce \n[b] Chocolate sauce \n[c] Whipped cream \n[d] Oreo bits \n[e] Lotus bits \n> ")
  if res == 'a' or res == 'A' or res == 'caramel sauce' or res == 'Caramel sauce' or res == 'caramel Sauce' or res == 'Caramel Sauce' or res == 'caramel' or res == 'Caramel':
   return ' Caramel sauce frappucino'
  elif res == 'b' or res == 'B' or res == 'chocolate sauce' or res == 'Chocolate sauce' or res == 'chocolate Sauce' or res == 'Chocolate Sauce' or res == 'chocolate' or res == 'Chocolate':
   return ' Chocolate sauce frappucino'
  elif res == 'c' or res == 'C' or res == 'whipped cream' or res == 'Whipped cream'or res == 'whipped Cream' or res == 'Whipped Cream' or res == 'cream' or res == 'Cream':
    return ' Whipped cream frappucino'
  elif res == 'd' or res == 'D' or res == 'oreo bits' or res == 'Oreo bits' or res == 'oreo Bits' or res == 'Oreo Bits' or res == 'oreo' or res == 'Oreo':
    return ' Frappucino with Oreo bits'
  elif res == 'e' or res == 'E' or res == 'lotus bits' or res == 'Lotus bits' or res == 'lotus Bits' or res =='Lotus Bits' or res == 'lotus' or res == 'Lotus':
    return ' Frappucino with Lotus bits'
  else:
    print_message()
    return order_frappe()

# Call coffee_bot()!

coffee_bot()


