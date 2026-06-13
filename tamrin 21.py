def factorial_iterative(n):
    if n < 0:
        return "فاکتوریل برای اعداد منفی تعریف نشده است."
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

while True:
    try:
        num_str = input("عددی را وارد کنید (برای خروج -1 را وارد کنید): ")
        num = int(num_str)

        if num == -1:
            print("برنامه پایان یافت.")
            break
        else:
            print(f"فاکتوریل {num} (ترتیبی): {factorial_iterative(num)}")

    except ValueError:
        print("ورودی نامعتبر است. لطفاً یک عدد صحیح وارد کنید.")
    except Exception as e:
        print(f"خطایی رخ داد: {e}")



