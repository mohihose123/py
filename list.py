# ایجاد لیست
my_list = []

# اضافه کردن عناصر به لیست
my_list.append(10)
my_list.append(20)
my_list.append(30)

print("لیست:", my_list)

# درج در یک موقعیت مشخص
my_list.insert(1, 15)   # درج 15 در اندیس 1
print("بعد از درج:", my_list)

# حذف یک مقدار
my_list.remove(20)
print("بعد از حذف مقدار 20:", my_list)

# حذف از ابتدا
my_list.pop(0)
print("بعد از حذف از ابتدا:", my_list)
