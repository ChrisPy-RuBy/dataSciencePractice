flash = ['jay garrick', 'barry allen', 'wally west', 'bart allen']

for person in flash:
  print (person)


superspeed = iter(flash)

print (next(superspeed))
print (next(superspeed))
print (next(superspeed))
print (next(superspeed))


small_value = iter(range(3))

print(next(small_value))
print(next(small_value))
print(next(small_value))

for x in range(3):
  print(x)

googol = iter(range(10 ** 100))

print(next(googol)) 
print(next(googol)) 
print(next(googol)) 
print(next(googol)) 
print(next(googol)) 
