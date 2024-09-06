my_dict={"алекс": 909567843, "люк": 9808783723}
print(my_dict)
print(my_dict["алекс"])
print(my_dict.get('danil'))
my_dict.update({"Алексей": 909887686,
               'вова': 8909898787})
print(my_dict)
g = my_dict.pop("люк")
print(my_dict)
print(g)

my_set= {1,1,"кот",2,2,3,3,7,7,4,True}
print(my_set)
my_set =set(my_set)
print(my_set)
print(my_set.add(5),my_set.add(9))
print(my_set)
print(my_set.discard(2))
print(my_set)