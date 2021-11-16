string = input("ingrese el nombre de la empresa ")
frequency = {}
def counter(string):
    for i in string:
        if i not in frequency:
            frequency[i] = 1
        else:
            frequency[i] += 1

    return frequency

sorted_frequency = (sorted(counter(string).items(), key=lambda x: x[1], reverse=True))

for i in range(3):
    print(sorted_frequency[i])

