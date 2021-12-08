def main():
    # file = open("anish.txt","w+")
    # for i in range(20):
    #     file.write("this is python code %d \n" %(i))
    # file.close()

    # file = open("anish.txt","r")
    # if file.mode == 'r':
    #     fileContent = file.read()
    #     print(fileContent)


    #Exception handling
    try:
        myFile = open("hrishi.txt","r")
        print("Successfully read!")
    except IOError:
        print("File doesn't exists")



if __name__ == "__main__":
    main()