import random
random_integer=random.randint(1,10)
print("\nYou've only 10 chances to guess the integer.\nYou have a perfect score of 10 if you guess right at first trial.\nOtherwise your score reduces by 1 as you try.")
count=0
score=10
while count < 10:
    count+=1
    guess=int(input("Enter number in the range of 1 and 10:"))
    if random_integer == guess:
            print("Congratulations!!!You did it in",count,"try(s)",f"You scored {(score-count)+1} over 10")
            break;
    elif random_integer>5:
        print("Hint:Number is between 5 and 11")
    elif random_integer<=5:
        print("Hint:Number is between 0 and 6")
if count >=10:
    print(f"\nThe number is {random_integer}")
    print("Better luck next time")
    print(f'You scored {score-count} over 10')


