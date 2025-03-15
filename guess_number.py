from random import randint as rd

# computer generated numbers
def generated_numbers(number):
    lists_of_guess = []
    active = True
    while active:
        guess = int(input("Enter a nnumber; "))
        lists_of_guess.append(guess)
        to_quit = input("Enter 'exit' to quit ").lower()
        if to_quit == "exit":
            break
        if guess > number:
            print("number too high")
        elif guess < number:
            print ("number too  low")
        else:
            print ("CONGRATULATION")
            print(f"You made the following guess: {lists_of_guess}")
            print (f"the correct number is: {number} ")
            active = False
computer_generated_nums = rd(1, 100)
print(generated_numbers(computer_generated_nums))
