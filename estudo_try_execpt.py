n_dislike = 3
numbers = range(4)

for n in numbers:
    if n != n_dislike:
        print(f"I have no feeling fot the number {n}")
    else:
        raise Exception ("I hate that number")
