import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
count_of_friends=len(friends)
random_index=random.randint(0,count_of_friends-1)
print("The one to pay today will be : " +friends[random_index])
