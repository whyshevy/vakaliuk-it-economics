import sys

m = []
while True:
    try:
        element = float(input("Enter real number or any key to exit input: "))
    except:
        break
    m.append(element)

minimum = m.index(min(m))
maximum = m.index(max(m))

if minimum + 1 < maximum:
    min_index = minimum
    max_index = maximum
elif maximum + 1 < minimum:
    min_index = maximum
    max_index = minimum
else:
    input("No sum is possible")
    sys.exit("end")

sum = 0
for i in range(min_index + 1, max_index):
    sum += m[i]
for i in range(len(m)):
    if m[i] < 0:
        m[i] += sum

print("Our array now is", m)
input("Press Enter to exit...")
