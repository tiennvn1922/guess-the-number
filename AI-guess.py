# user nghĩ 1 con sô, AI sẽ đoán số đó
# AI sẽ hỏi xem số AI đoán lớn hơn hay bé hơn hay bằng với số của user

# Có 2 số low, high, số x = random(low, high)
# low ban đầu = 1, high là sô lớn nhất mà user kêu AI đoán
# nếu x nhỏ hơn user_number, x = random(low+1,high)
# nếu x lớn hơn user_number, x = random(low,high-1)
# điều kiện là low != high, ngược lại số cần đoán là low

import random

low = int(input('Số nhỏ nhất AI có thể đoán là: '))
high = int(input('Số lớn nhất AI có thể đoán là: '))

if low == high:
    print(f'Số bí mật là: {low}')
feedback = ''
while feedback != 'c':
    random_number = random.randint(low, high)
    # print(random_number)
    feedback = input(
        f'Số {random_number} là Quá lón (L) hay Quá nhỏ (N) hay Chính xác (C)? ').lower()
    if feedback == 'l':
        high = random_number + 1
    elif feedback == 'n':
        low = random_number + 1
print(f'Số bí mật là: {random_number}')
