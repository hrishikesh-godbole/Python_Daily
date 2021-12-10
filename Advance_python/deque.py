# import string
import collections
# print(string.ascii_lowercase)
import string


def main():
    myDeque = collections.deque(string.ascii_lowercase)
    # print("Number of elements are: ",str(len(myDeque)))
    # for i in myDeque:
    #     print(i, end=',')

    #removing element from right side of the queue
    myDeque.pop()
    print(myDeque)

    #removing element from left side of the queue
    myDeque.popleft()
    print(myDeque)

    #append an element in the left
    myDeque.appendleft(121)
    print(myDeque)

    #rotate the queue
    myDeque.rotate(10)
    print(myDeque)

if __name__ == '__main__':
    main()
