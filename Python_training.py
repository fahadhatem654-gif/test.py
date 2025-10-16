# 

# x = int(input("Enter a number :  "))
# while True :
#     if x < 0  :
#         print("Loop stopped")
#         break
#     elif x > 0 or x == 0 :
#         print("Valid number")
#     x = int(input("Enter a number : "))


# name = input("Enter your name : ")
# while True : 
#     if name == 'stop' :
#         print("Program ended")
#         break
#     else :
#         print(f"Welcome , {name}")
#         name = input("Enter your name : ")
# w

# while True :
#     x = int(input("Enter a number (or 'stop' to end) : "))
#     if x == 'stop':
#         break
# print(f"Numbers entered : {[x]}")    

    # إنشاء قائمة فارغة لتخزين الأرقام
# numbers = []

# while True:
#     x = input("Enter a number (or 'stop' to end): ")
    
#     # تحقق من كلمة الإيقاف
#     if x == 'stop':
#         break
    
#     # حول الإدخال إلى رقم صحيح وأضفه للقائمة
#     # 👇 أضف هنا السطر المناسب لتحويل x إلى int وإضافته إلى numbers

# # بعد انتهاء الحلقة، اطبع كل الأرقام التي تم إدخالها
# print(f"Numbers entered: {numbers}")

# # 👇 أضف هنا حساب مجموع الأرقام الموجبة فقط (اختياري)


# x = input("Enter your age : ")
# while True :
#     if not x.isdigit():
#         print(f"Invalid age , try again")
#         continue
#     x = int(x)

#     if 1 <= x <= 120 :
#         print(f"valid age entered : {x}  ")
#         break
#     else :
#         print("Invalid age , try again")  
        

# while True :
#     x = input("Enter your score : ")

#     if not x.isdigit():
#          print("Invalid Score , try again")
#          continue
        
#     x = int(x)
#     if  0 <= x <= 100 :
#         if  90 <= x <= 100 :
            
#             print(f"Grade A")
#             break
#         elif 80 <= x <= 89 :
#             print(f"Grade B")
#             break
#         elif 70 <= x <= 79 :
#             print(f"Grade C")
#             break
#         elif 60 <= x <= 69 :
#             print(f"Grade D")
#             break
#         elif x < 60 :
#             print(f"Grade F")
#             break  
#     else :
#         print(f"Invalid score")           

while True :
    x = input("Enter a postive number : ")
    if not x.isdigit():
        print("Invalid input , try again")
        continue
    x = int(x)
    if x > 0 : 
        print(f"Number accepted : {x}")
        if x % 2 == 0 :
            print("This is an even number")
        else :
            print("This is an odd number")
            break

         

    
