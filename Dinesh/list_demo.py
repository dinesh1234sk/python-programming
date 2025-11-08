my_list=["apple","banana","cherry"]
print(my_list)
numbers=[10,20,30,40]
print(numbers)
mixed=["hello",99,3.14,True]
print(mixed)
empty_list=[]
print(len(empty_list))
fruits=["apple","banana","cherry","mango"]
first_item=fruits[0]
print("first item",first_item)
third_item=fruits[2]
print("third item:",third_item)
last_item=fruits[3]
print("last item:",last_item)
last_item_alt=fruits[-1]
print("last item using negative index:",last_item_alt)
fruits=["apple","banana","cherry","mango"]
fruits[1]="blueberry"
print(fruits)
fruits[-1]="kiwi"
print(fruits)
fruits=[]
fruits.append("apple")
fruits.append("banana")
fruits.append("cherry")
print(fruits)
fruits.insert(1,"orange")
print(fruits)
fruits.extend(["mango","kiwi"])
print(fruits)