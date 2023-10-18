f = open('test.txt')

numbers = f.readlines()
rf = open('result.txt', 'w')
n = 10000000
bit = [0 for i in range(10000001)]
for number in numbers:
    bit[int(number)] = 1
for number in range(0, 10000001):
    if (bit[number] == 1):
        rf.writelines(str(number) + '\n')
    else:
        print(number)
rf.close()