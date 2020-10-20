fav_movies = ["The Holy Grail", "The Life of Brian"]

for each_flick in fav_movies:
    print(each_flick)

count = 0
while count < len(fav_movies):
    print(fav_movies[count])
    count = count+1

movies = [
    "The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
    [
        "Graham Chapman",
        ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]
    ]
]

print(movies[4][1][3])

"""
  Multiple-line comment
"""

def print_lol (the_list):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
    else:
        print(each_item)

print_lol(movies)

is_hot = True
is_cold = False
if is_hot:
   print("It's a hot day")
   print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm cloth")
else:
    print("It's a lovely day")
print("Enjoy your day")


price = 1000000
has_good_credit = True
if has_good_credit:
   down_payment = price*0.1
else:
   down_payment = price*0.2
print(f"Down payment: ${down_payment}")

has_high_income = True
has_good_credit = True
has_criminal_record = False
if has_high_income and has_good_credit:
    print("Eligible for loan")
if has_high_income or has_good_credit:
    print("Eligible for loan")
if has_good_credit and not has_criminal_record:
    print("Eligible for loan")
