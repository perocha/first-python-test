# WHILE loops
index = 1
while index <= 10:
    print (index)
    index += 1

secret_word = "lion"
guess = ""
guess_count = 0
out_of_guesses = False
MAX_TRIES = 3
while guess != secret_word and not(out_of_guesses):
    if guess_count < MAX_TRIES:
        guess = input ("Enter your guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if not(out_of_guesses):
    print ("You win!!")
else:
    print ("Out of guesses.. you lose!")


# FOR loops
my_string = "This is a test"
for letter in my_string:
    print (letter)

friends = ["Jim", "Karen", "Kevin", "Peter"]
print (friends)
for friend in friends:
    print (friend)

for index in range(10):
    print (index)

for index in range(3,9):
    print (index)

for index in range(len(friends)):
    print (friends[index])


def raise_to_power (my_num, my_power):
    result = 1
    for index in range (my_power):
        result = result * my_num
    return result

print (raise_to_power (5, 6))