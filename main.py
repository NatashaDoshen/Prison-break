from collections import Counter

prison1 = [1, 1, 0, 0, 0, 1, 0]

#free the prisoner from the cell
prison1.pop(0)
print(prison1)

#freed prisoners
for i in range (len(prison1 )):
  freed_prisoners = Counter(prison1)
  print("the number of freed prisoners is", freed_prisoners[0])

#locked cells become unlocked and unlocked become locked
for i in range (len(prison1 )):     
  if prison1[i] ==1:
    prison1[i]=0
    print(prison1)
  elif  prison1[i] ==0:
        prison1[i]=1
        print( prison1)

  "\n"
  

prison2 = [0, 0, 1, 1, 1, 0, 1] 

#free the prisoner from the cell
prison2.pop(2)
print("\n", prison2)  

#freed prisoners
for i in range (len(prison2 )):
  freed_prisoners = Counter(prison2)
  print("the number of freed prisoners is", freed_prisoners[0])


#locked cells become unlocked and unlocked become locked
for i in range (len(prison2 )):     
  if prison2[i] ==1:
    prison2[i]=0
    print(prison2)
  elif  prison2[i] ==0:
        prison2[i]=1
        print(prison2)
        
"\n"

prison3 = [1, 1, 0, 0, 0, 1, 0]

#free the prisoner from the cell
prison3.pop(2)
print("\n", prison3)  

#freed prisoners
for i in range (len(prison3 )):
  freed_prisoners = Counter(prison3)
  print("the number of freed prisoners is", freed_prisoners[0])


#locked cells become unlocked and unlocked become locked
for i in range (len(prison3 )):     
  if prison3[i] ==1:
    prison3[i]=0
    print(prison3)
  elif  prison3[i] ==0:
        prison3[i]=1
        print(prison3)
        
"\n"

prison4 = [0, 0, 1, 1, 1, 0, 1]
#free the prisoner from the cell
prison4.pop(6)
print("\n", prison4)  

#freed prisoners
for i in range (len(prison4 )):
  freed_prisoners = Counter(prison4)
  print("the number of freed prisoners is", freed_prisoners[0])


#locked cells become unlocked and unlocked become locked
for i in range (len(prison4 )):     
  if prison4[i] ==1:
    prison4[i]=0
    print(prison4)
  elif  prison4[i] ==0:
        prison4[i]=1
        print(prison4)
   
  
Breaking prisoners out of a unique prison using lists, logic, and loops.

For this task, you are required to use the trinket IDE below to create a program that determines the number of freed prisoners in the unique prison arrangement described below.

A prison can be represented as a list of cells. Each cell contains exactly one prisoner. A 1 represents an unlocked cell and a 0 represents a locked cell.

[1, 1, 0, 0, 0, 1, 0]
Copy
Starting inside the leftmost cell, you are tasked with seeing how many prisoners you can set free, with a catch. Each time you free a prisoner, the locked cells become unlocked, and the unlocked cells become locked again. You can only move from left to right and not go back.

So, if we use the example above:

[1, 1, 0, 0, 0, 1, 0]
# You free the prisoner in the 1st cell
# The locked cells 3rd, 4th, 5th and 7th become unlocked and the unlocked cells 1st, 2nd and 6th become locked

[0, 0, 1, 1, 1, 0, 1] 
# You free the prisoner in the 3rd cell (2nd one locked).
# The locked cell 1st, 2nd and 6th become unlocked and the unlocked cells 3rd, 4th, 5th and 7th become locked

[1, 1, 0, 0, 0, 1, 0]
# You free the prisoner in the 6th cell (3rd, 4th and 5th locked).
# The locked cells 3rd, 4th, 5th and 7th become unlocked and the unlocked cells 1st, 2nd and 6th become locked

[0, 0, 1, 1, 1, 0, 1]
# You free the prisoner in the 7th cell - and you are done!
Copy
Here, we have set free 4 prisoners in total.
Create a program that, given this unique prison arrangement, returns the number of freed prisoners.

Examples
freed_prisoners([1, 1, 0, 0, 0, 1, 0]) ??? 4

freed_prisoners([1, 1, 1]) ??? 1

freed_prisoners([0, 0, 0]) ??? 0

freed_prisoners([0, 1, 1, 1]) ??? 1
 Notes
You must free a prisoner in order for the locks to switch. So in the second example where the input is [1, 1, 1] after you release the first prisoner, the locks change to [0, 0, 0]. Since all cells are locked, you can release no more prisoners.
You always start within the leftmost element in the list (the first prison cell). If all the prison cells to your right are zeroes, you cannot free any more prisoners.

