# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Тыпидор")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "Привет, я Тыпидор. Ты лох, кто вообще визуальные новеллы создает?"

    e "Ты долбоеб чтоли блять? Пиздец, иди учи блять хуйню свою, еблан"
    hide eileen happy

    scene end
    pause
    # This ends the game.

    return
