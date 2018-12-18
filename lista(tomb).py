allatok = ["lo", "cinege", "varju"]
evszam = [12, 1995, 666]
###

empty_list = []
print empty_list

list_with_items = ["first item", "second item", 34, 12.4]
print list_with_items

var1 = "first variable"
var2 = "second variable"
some_list = [var1, var2]
print some_list
###

print "Welcome to the TODO task management program."

todo_list = []

while True:
    task = raw_input("Please enter a TODO task: ")
    print "Your task is: " + task
    todo_list.append(task)  # this is how we add (append) a variable into a list

    new = raw_input("Would you like to enter new task? (yes/no) ")

    if new == "no":
        break

print "All tasks: %s" % todo_list  # print a list of all tasks
print "END"
###

some_list = ["item 1", "item 2", "item 3"]

for item in some_list:
    print item