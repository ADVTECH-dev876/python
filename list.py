List Methods
Python has a set of built-in methods that you can use on lists.

Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list


// access list items
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

thislist = ["apple", "banana", "cherry"]
print(thislist[-1]) //cheery

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

//repalce
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]

thislist[1:3] = ["blackcurrant", "watermelon"]

print(thislist)

//add
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
//insert
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])/for loop
print(thislist)


remove
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
/alter emthode
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

/clear
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
/loop
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)/sort/

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)/rev sort

/copy
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

/alternate cpy
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

copy alternate
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

/join
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
/alter
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

alter

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
