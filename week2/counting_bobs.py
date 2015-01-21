# Test 1
s = 'mbobqykwbobobobooboboa'
# Output should be:
# Number of times bob occurs is: 5

target = "bob"
total = 0
t_size = len(target)
s_size = len(s)

for i in range(0, s_size - t_size + 1):
    if s[i:i + t_size] == target:
        total += 1

print "Number of times bob occurs is: {}".format(total)
