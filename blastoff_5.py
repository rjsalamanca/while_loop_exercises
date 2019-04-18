import time

print('Waiting 1 second...')
time.sleep(1)

over20 = True

while over20:
    count = int(input('Enter a number to countdown: '))
    if count <= 20:
        over20 = False
        while count >= 0:
            print(count)
            count -= 1
        print('Blast off')
    else:
        print('Enter a number lower or equal to 20')