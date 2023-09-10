
"""
เขียนโปรแกรมหา index ของตัวเลขที่มีค่ามากที่สุดใน Array ด้วยภาษา python 
เช่น [1,2,1,3,5,6,4] ลำดับที่มีค่ามากที่สุด คือ index = 5 โดยไม่ให้ใช้ฟังก์ชั่นที่มีอยู่แล้ว ให้ใช้แค่ลูปกับการเช็คเงื่อนไข

"""

def find_largest_index(numbers):
    max_index = 0
    max_value = numbers[0]

    for i in range(1, len(numbers)):
        if numbers[i] > max_value:
            max_value = numbers[i]
            max_index = i

    return max_index

numbers = [1, 2, 1, 3, 5, 6, 4]
if len(numbers) < 1:
    raise ValueError("The list is empty")
largest_index = find_largest_index(numbers)
print(f"The largest number is {numbers[largest_index]} at index {largest_index}")