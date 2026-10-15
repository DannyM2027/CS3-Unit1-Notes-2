# lists a data collectuin tgats ordered and mutabale
def main():
    my_list = []
    my_other_list = list()

    my_classes = ["math", "post", "physics"]

    print(len(my_classes))
    #we can indez using name [x]
    # last element lenlist-1
    print(my_classes[2])
    print(my_classes[len(my_classes)-1])
    print(my_list[0])
    print(my_classes)

    print(my_classes.index("journ"))
    my_classes.append("journ")

    my_classes.insert(8, "biology")
    print(my_classes)


    print(my_classes.pop())
    print(my_classes)

    my_classes.sort()
    print(my_classes)

    numList = [6, -4, 3, 9]
    numList.sort()
    print(numList)

    my_classes.sort(reverse=True)
    sorted_classes = sorted(my_classes)
    print(sorted_classes)

    colors_a = ["blue," "turq" "bblue" "red"]
    colors_b = ["blue," "orange" "yellow" "brown"]

    colors_a.extend(colors_b)
    print(colors_a)

    count = colors_a.index("orange")
    count = colors_a.count("blue")
    print({count})
    colors_a(colors_a.index("turq")) == "green"

    colors_a.remove("green")
    print(colors_a)

    repeats = ["book", "pencil", "book", "folder", "robot", "pen," "pencil"]
    print(repeats.index("pencil"))

    temp = repeats
    while "pencil" in temp:
        print(temp.index("pencil"))
        temp = temp[temp.index("pencil") +1:]

    print(repeats)
    repeats.remove("pencil")
    print(repeats)

    # we can use .pop(index)
    print(repeats.pop(4))

    # tuples

    my_tuple = (2, 5, 8)
    print(my_tuple)

    if 5 in my_tuple:
        print(my_tuple.index(5))

if __name__ == "__main__":
    main()
