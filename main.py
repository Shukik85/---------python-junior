import sys
from MenuBook.menuBook import Menu


def main():
    menu = Menu()
    answer = sys.argv[-1]
    while True:
        if menu.tiket:
            menu.getMenu(answer)
            answer = menu.answer
        else:
            return


if __name__ == "__main__":
    main()
