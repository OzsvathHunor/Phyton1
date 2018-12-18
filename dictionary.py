some_dictionary = {"happiness": "state of feeling happy", "luck": "a random event with a positive effect"}

cities_dict = {1000: "Ljubljana", 8000: "Novo mesto", 2000: "Maribor"} # 1000 az kulcs melynek erteke Ljubljana

cars = {"clio": "renault", "m3": "bmw", "micra": "nissan", "i8": "bmw"}

for x in cars:
    print x + " " + cars[x] #a sorrend nem szamit a dictionarynal
print

cars["1310"] = "dacia"
for x in cars:
    print x + " " + cars[x]

print
print "Welcome to the TODO task management program."

todo_dict = {}

while True:
    task = raw_input("Please enter a TODO task: ")
    status = raw_input("Was the task completed yet? (yes/no) ")
    print "Your task is: " + task

    if status == "yes":
        todo_dict[task] = True  # this is how we add a key-value pair into a dict
    else:
        todo_dict[task] = False

    new = raw_input("Would you like to enter new task? (yes/no) ")

    if new == "no":
        break

print "All tasks: %s" % todo_dict

print "END"