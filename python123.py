# #python
# a = int(input())
# b = int(input())
# c = int(input())
# if a+b > c and b+c > a and c+a > b:
#     print("Đây là 3 cạnh của một tam giác")
# else:
#     print("Đây không phải là 3 cạnh của một tam giác")


# user = input("Nhập vào đây username của bạn: ")
# if user == 'admin':
#     print("Nhập vào mật khẩu của bạn dưới đây")
# else:
#     print("Username của bạn không chính xác")
# mat_khau = str(input('Mật khẩu: '))
# if mat_khau == '123456@Abc':
#     print("Welcome")
# else:
#     print("Mật khẩu của bạn không chính xác")


#bài 2

# a = int(input('nhập vào điểm toán:'))
# b = int(input('nhập vào điểm văn:'))
# c = int(input('nhập vào điểm anh:'))
# tb = (a+b+c)/3
# if tb < 5:
#     print('không đạt')
# elif tb >= 5 and tb < 7:
#     print('đạt')
# elif tb >= 7 and tb < 8:
#     print('khá')
# elif tb >= 8:
#     print('tốt')

# can_nang = float(input('Mời người dùng nhập vào cân nặng theo kilogram: '))
# chieu_cao = float(input('Mời người dùng nhập vào chiều cao theo mét: '))
# BMI = can_nang / chieu_cao**2
# if BMI < 16:
#     print("Gầy cấp độ III")
# elif BMI < 17:
#     print("Gầy cấp độ II")
# elif BMI < 18.5:
#     print("Gầy cấp độ I")
# elif BMI < 25:
#     print("Bình thường")
# elif BMI < 30:
#     print("Thừa cân")
# elif BMI < 35:
#     print("Béo phì cấp độ I")
# elif BMI < 40:
#     print("Béo phì cấp độ II")
# else:
#     print("Béo phì cấp độ III")




# n = 10
# sum = 0 
# i = 1
# while i <= n:
#     sum += i
#     i += 1
#     print(sum)



# numbers = [1,2,3,4,5,6,7,8,9]
# sum = 0 
# for val in numbers:
#     if val % 2 == 0:
#         sum += val 
# print(sum)



# for i in range(1,10,2):
#     print(i,end=', ')


# fruits = ['apple','banana','cherry']
# for x in fruits:
#     if x == 'banana':
#         pass

# break, continue, pass

# num_list = [1,2,3]
# alpha_list = ['a','b','c']
# for number in num_list:
#     print(number)
#     for letter in alpha_list:
#         print(letter)


# sum = 0 
# for i in range(3,101): 
#     if i % 3 == 0:
#         sum += 1
# print(sum)


sum = 0 
for i in range(0,51):
    if i % 2 == 0:
        sum += 1
print(sum)


