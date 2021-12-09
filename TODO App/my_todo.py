import  todo

def main():
    run = 1
    todo.create_table()

    while run:
        print("\n")
        print("1. Inser Task in todo list \n"
              "2. View data from todo list \n"
              "3. Delete task from todo list \n"
              "4. Exit \n")

        x = int(input("Choose any of the above option"))

        if x==1:
            task = str(input("Enter your todo: "))
            todo.data_entry(task)
        elif x==2:
            todo.printData()
        elif x==3:
            indexToDelete = int(input("Enter the number of task to be deleted"))
            todo.data_delete(indexToDelete)
        elif x==4:
            run=0
        else:
            print("Please choose valid option")

    todo.closeCursor()

if __name__ == '__main__': main()