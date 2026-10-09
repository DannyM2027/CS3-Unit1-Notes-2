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
    print(my_classes[1] = "apcomp")
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

    coloros_a = ["blue," "turq" "bblue" "red"]
    coloros_b = ["blue," "orange" "yellow" "brown"]

    colors_a.extend(coloros_b)
    print(coloros_a)

    count = coloros_a.index("orange")
    count = coloros_a.count("blue")
    print({count})
    coloros_a(coloros_a.index("turq"))] = "green"

if __name__ == "__main__":
    main()
