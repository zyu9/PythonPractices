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

def print_lol (the_list):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
    else:
        print(each_item)

print_lol(movies)



