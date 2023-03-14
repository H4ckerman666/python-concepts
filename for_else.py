search = 2
for i in range(5):
    if search == i:
        print("I'm here!!")
        break
#! else runs if a break doesn't execute in the for loop 
else:
    print("Not found")