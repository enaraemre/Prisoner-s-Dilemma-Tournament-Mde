from tour import Tour

def main():
    useraction = ''
    playercount = []
    while useraction != 'q':
        useraction = input('Please choose contest from A to C or (enter a-b-c) or enter (m) to continue manual.(enter q to quit):')
        playercount.clear()
        if useraction == 'a':
            playercount = [5, 5, 5, 5, 5, 5, 0]
            Tour(playercount)
        elif useraction == 'b':
            playercount = [5, 5, 3, 2, 0, 0, 15]
            Tour(playercount)
        elif useraction == 'c':
            playercount = [1, 5, 20, 1, 1, 2, 0]
            Tour(playercount)
        elif useraction == 'm':
            playercount.append(int(input("Please enter Cooperator count:")))
            playercount.append(int(input("Please enter Defector count:")))
            playercount.append(int(input("Please enter Tit for Tat count:")))
            playercount.append(int(input("Please enter Spiteful count:")))
            playercount.append(int(input("Please enter Naive Prober count:")))
            playercount.append(int(input("Please enter Tit for 2 Tats count:")))
            playercount.append(int(input("Please enter Random Player count:")))
            Tour(playercount)


        elif useraction == 'q':
            break
        else:
            print('Unknown input')

main()

