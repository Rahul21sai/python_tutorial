#else in for and while loop
#else in this is excuted after the all iterations are completed inn for loop
for i in range(0,5):
    print(i)
    if i==4:
        break#else is not going to print because the loop is completed
        
else:
    print("soory no i")
