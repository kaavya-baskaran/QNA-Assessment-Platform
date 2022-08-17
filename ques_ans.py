question=[":1. How many months do we have in a year?",
          "2. How many days do we have in a week?",
          "3. How many days are there in a year?"]
answers=[['1)16','2)19','3)17','4)12'],['1)6','2)9','3)7','4)0'],['1)668','2)990','3)365','4)0']]

dic={1:4,2:3,3:3}
mark=0
name=input("Name :")
reg_no=int(input("Reg No :"))
print()

for i in range(len(question)):
     print(question[i],"\t\tNeed 50:50 options? press 5")
     for j in range(4):
         print(answers[i][j])
     
     ans=int(input())
     print()
     if(ans==5):
         print(dic[i+1])
         if dic[i+1]%2==0:
             for k in range(1,5):
                 if(k%2 == 0):
                     print(answers[i][k-1])

         else:
             for k in range(1,5):
                 if(k%2 != 0):
                     print(answers[i][k-1])
         ans=int(input())
         
         if ans==dic[i+1]:
             mark+=0.5
         else:
             mark-=1
                
             
             
     elif(ans==dic[i+1]):
         mark+=1
     else:
         mark-=1           #NEGATIVE MARKING

print("marks :",mark,"/",len(question))





    





































