words = input().split()
frequency = {}
counter = 0
for n in words:
    if n in frequency.keys():
        counter +=1
        frequency[n] = counter
        print(frequency)
    else:
        frequency[n] = 1
        print(frequency) 
for n in frequency:
    print(n, frequency[n])
