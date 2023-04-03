with open("demo.txt") as file:

    for line_ in file:
        splits = line_.split("")
        if len(splits)==0:
            break
        print(splits)