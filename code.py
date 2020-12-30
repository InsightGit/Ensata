from adafruit_magtag.magtag import MagTag

from ensata.screens.main_screen import MainScreen

def main():
    magtag = MagTag(debug=True)

    current_screen = MainScreen(magtag)

    current_screen.init_screen()

    while True:
        current_screen.update()


if __name__ == "__main__":
    main()
