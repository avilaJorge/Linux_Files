import sys
import mygreeting

answers = []
answers.append('G') # README 0
answers.append('N') # README 1
answers.append('S') # README 2
answers.append('#3') # README 3
answers.append('#4') # README 4
answers.append('#5') # README 5
answers.append('#6') # README 6
answers.append('#7') # README 7
answers.append('#8') # README 8
answers.append('#9') # README 9
answers.append('#10') # README 10


# You can ignore the following code :)

encode = [0, 10, 4, 8, 5, -1, 2, 1, 6, 3, 7, 9, -2] 

for i in encode:
    if (i == -1):
        sys.stdout.write (' ') 
    elif (i == -2):
        sys.stdout.write ('!')
    else:
        sys.stdout.write (answers[i])

print
