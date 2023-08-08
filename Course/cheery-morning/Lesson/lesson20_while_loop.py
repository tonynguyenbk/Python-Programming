# n = 1
# while n <= 5:
#     print(n)
#     n += 1

# n = 20
# while n >= 1:
#     print(n)
#     n -= 1

# a, b = 10, 20
# while a <= b:
#     print(a)
#     a += 1

# n = 5
# i = 1
# while i <= n:
#     print(i)
#     continue # quay tro lai vong lap while moi
#     i += 1

# n = 5
# i = 1
# while i <= n:
#     print(i)
#     if i == 3:
#         break   # thoat khoi vong lap
#     i += 1

# Yeu cau nguoi dung nhap so duong, nhap so am hoac so 0 thi bat nhap lai:
# while True:
#     n = int(input("Nhap n: "))
#     if n > 0:
#         break

# Tinh tong chu so, dem so chu so, tong c/s chan/le, c/s ngto, 
# so thuan nghich, so loc phat, so hoan hao,...
# n = 1234
# cnt = 0
# sum3 = 0
# while n != 0:
#     sum3 += n % 10
#     cnt += 1
#     n //= 10
# print("So cac c/s cua n: ", cnt)
# print("Tong cac c/s cua n la: ", sum3)

# Dao nguoc 1 so
# n = 1234 # => 4321
# lat = 0
# while n != 0:
#     lat = lat * 10 + n % 10
#     n //= 10
# print(lat)

# # Do dai 1 so sau khi chuyen thanh xau ky tu
# n = 12345
# print(len(str(n)))