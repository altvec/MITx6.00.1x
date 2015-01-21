# Test 1
s = 'btaywugyccgmdrmbguew'
# Output should be
# Longest substring in alphabetical order is: ccgm

longest = ""

for i in range(0, len(s) - 1):
    tmp = s[i]
    for j in range(i, len(s) - 1):
        if s[j] <= s[j + 1]:
            tmp += s[j + 1]
        else:
            break
    if len(tmp) > len(longest):
        longest = tmp

print "Longest substring in alphabetical order is: {}".format(longest)
