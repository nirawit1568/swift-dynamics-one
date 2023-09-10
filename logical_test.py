
"""
เขียนโปรแกรมหาจำนวนเลข 0 ที่อยู่ติดกันหลังสุดของค่า factorial ด้วย Python โดยห้ามใช้ math.factorial 
เช่น 7! = 5040 มีเลข 0 ต่อท้าย 1 ตัว, 10! = 3628800 มีเลข 0 ต่อท้าย 2 ตัว

"""
def factorial_recursive(n):
    if n < 0:
        return None
    elif n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)

def count_trailing_zeros(num):
    count = 0
    for digit in reversed(str(num)):
        if digit == '0':
            count += 1
        else:
            break 

    return count

n = 10
result = factorial_recursive(n)
zero = count_trailing_zeros(result)
print(f"result is {zero}")