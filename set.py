# create an empty set
s = set()

#add values 
s.add(0)
s.add(2)
s.add(4)
s.add(6)
# in set no element appears more than once
s.add(4)
s.remove(0)
print(s) # {2, 4, 6}
print(f"The set has {len(s)} elements")