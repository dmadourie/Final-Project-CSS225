from turtle import done

username = input("What is your name?")
print("Hello", username, "I hope you are ready, because it is going to be wild!")
print("This game involves mystery of someone who's moved in next to someone who isn't as normal as others")
# Chapter 1
# In the small town of Greenport, New York, a new person moves in next door to someone
# who seems out of the ordinary.
answer = input("You see someone has moved in next door, would you go say hi or stay home?").lower().strip()
if answer == "say hi":
    answer = input("You wave at neighbor through the window")
if answer == "stay home":
    print("Game over")
else:
    print("Good way to meet people!")


# Chapter 2
answer = input("After introducing yourself, do you go home or stay and talk?")
if answer == "go home":
    answer = input("Well nice to meet you, I gotta finish unpacking!")
if answer == "stay and talk":
    print("Ask about what the neighborhood is like.")
else:
    print("This place isn't bad after all as I thought it would.")
# Chapter 3
# After talking with the new neighbor, she is shocked at how nice and sweet she is.
answer = input("After the good talk, would you go and hug her or don't hug her?")
if answer == "hug":
    answer = input("Thank you for being so nice to me.")
    if answer == "Don't hug":
        print(done)

    else:
        print("This friendship went so fast with just a hug, I'm shocked!")
# Chapter 4
# After deciding whether or not to hug the neighbor, the user falls to the ground
# After being hugged very tightly to the point where she can't breathe.
answer = input("After deciding to hug the neighbor, do you try to pull away or fall to the ground?")
if answer == "pull away":
    answer = input("RUN!")
    if answer == "fall to the ground":
        print("Ouch! You hurt me! Why did u hug me so tight?!")
    else:
        print("Instead of hugs, a light hand shake would've been better.")

answer = input("You wake up, confused, do you find information or look around for someone?")
if answer == "find information":
    answer = input("Ask around about where you are and what happened to you.")
    if answer == "look around for someone":
        print("Where am I? What happened, and where is my stuff? The crazy neighbor?")
    else:
        print("You've ended up in the middle of nowhere. Game over! Thanks for playing!")
    exit()
