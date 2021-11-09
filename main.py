#!/usr/bin/python3

import kakuroboard
import time

def main():
    # Menu 
    menu = {}
    menu['1'] = "Generate (and eventually solve) a new board" 
    menu['2'] = "Load and solve a board"
    menu['3'] = "Exit"

    while True:
        options = menu.keys()
        
        # Print menu
        print("Menu:")
        for entry in options: 
            print("\t" + entry, menu[entry])

        selection = input("\nPlease select an option: ") 
        print()
        if selection == '1': 
            print("Generate (and eventually solve) a new board\n")
            rows = int(input("How many rows do you want? "))
            columns = int(input("How many columns do you want? "))
            board = kakuroboard.KakuroBoard(rows, columns)
            board.generate()
            board.showEmptyBoard()
            
            ans = input("Do you want to solve it? [Y/N] ")
            if ans == 'Y':
                print("\n\nThe solution is: ")
                start = time.time()
                board.solve()
                board.showSolutionBoard()
                print("in %.10f seconds" %(time.time()- start))

            ans = input("Do you want to save all data? [Y/N] ")
            if ans == 'Y':
                name = "KakuroBoard-" + time.strftime("%Y%m%d-%H%M%S")
                board.save(name)
        elif selection == '2': 
            print("Load and solve a board\n")
            rows = int(input("How many rows does the board have? "))
            columns = int(input("How many columns does the board have? "))
            board = kakuroboard.KakuroBoard(rows, columns)
            board.load()
            board.showEmptyBoard()

            ans = input("\nIs this the board you want to upload and solve? [Y/N] ")
            if ans in 'Yy':
                print("\n\n The solution is: ")
                start = time.time()
                board.solve()
                board.showSolutionBoard()
                print("in %.10f seconds" %(time.time()- start))
            
            ans = input("Do you want to save all data? [Y/N]")
            if ans in 'Yy':
                name = "KakuroBoard-" + time.strftime("%Y%m%d-%H%M%S")
                board.save(name)

        elif selection == '3':
            print("Exiting ...")
            break
        else:
            print("Unknown option selected!")

if __name__ == "__main__":
    main()