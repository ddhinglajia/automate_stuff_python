def comma(someList):
    for i in range(len(someList)-1):
        print (someList[i] + ', ' , end='')
        if i == len(someList)-3:
            print (someList[i+1] + ' and ' +someList[i+2])
            break

spam = ['apples', 'bananas', 'tofu', 'cats']

comma(spam)
