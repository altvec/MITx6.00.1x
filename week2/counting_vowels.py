# Test 
s = 'bovkkweabeywu'
# Output should be
# Number of vovels: 5

vovels = "aeiou"
total = 0
for i in s:
    if i in vovels:
        total += 1
print "Number of vovels: {}".format(total)
