import GameMenu
import GameGame

def game_state(screen):
    """
    0 = main menu
    1 = playing
    2 = game over
    """
    current_game_state = 0

    if current_game_state == 0:
        GameMenu.run(screen)
        print('Changed game state')
        current_game_state = 1

    if current_game_state == 1:
        GameGame.run(screen)
