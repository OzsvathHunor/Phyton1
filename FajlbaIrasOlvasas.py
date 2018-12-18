todo_file = open("todo.txt", "w+")  # open the TXT file (or create a new one)

print "Completed tasks:"
todo_file.write("Completed tasks:\n")  # write into the TXT file
for item in todo_dict:
    if todo_dict[item] == True:
        print "- " + item
        todo_file.write("- " + item + "\n")  # add task into the TXT file

todo_file.write("\n")

print "Incomplete tasks:"
todo_file.write("Incomplete tasks:\n")  # write into the TXT file
for item in todo_dict:
    if todo_dict[item] == False:
        print "- " + item
        todo_file.write("- " + item + "\n")  # add task into the TXT file

todo_file.close()  # close the TXT file