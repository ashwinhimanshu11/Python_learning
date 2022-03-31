for letter in "giraffe":
    print(letter)

friends = ["Jim", "Kevin", "Toby"]

for friend in friends:
    print(friend)

for index in range(10):
    print(index)

for index in range(3, 10):
    print(index)

for index in range(len(friends)):
    print(friends[index])

for index in range(5):
    if index == 0:
        print(str(index) + "-First Iteration")
    else: 
        print(str(index) + "-Not First")