# máy tính có một con số bí mật
# nhiệm vụ của user là đoán con số đó
# máy tính sẽ thông báo số của user lớn hơn hay nhỏ hơn con số bí mật đến khi user đoán đúng

# random 1 con số x -> nhận vào số user đoán -> so sánh với x -> trả về kq cho user
import random


def guess(x):
    random_number = random.randint(1, x)
    guess_number = 0
    count = 1
    guess_number = int(input(f'Lần {count}: Đoán một số giữa 1 và {x}: '))
    while guess_number != random_number:
        if guess_number < random_number:
            guess_number = int(
                input(f'Lần {count+1}: Số {guess_number} quá nhỏ. Mời bạn đoán lại: '))
            count = count + 1
        elif guess_number > random_number:
            guess_number = int(
                input(f'Lần {count+1}: Số {guess_number} quá lớn. Mời bạn đoán lại: '))
            count = count + 1
    print(
        f'Chúc mừng bạn đã đoán trúng sau {count} lần đoán. Số bí mật là {random_number}')


guess(100)
