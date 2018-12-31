from bootstrap import Bootstrap
from inputhandler import InputHandler

def main():
    game = Bootstrap().initialise()
    input_handler = InputHandler(game)
    state_machine = game.get('state-machine')


    while state_machine.player_health > 0:
        new_location = input_handler.get_next_location()
        state_machine.set_location('player', new_location)

        update_player_health(state_machine)

    print('Dead')

def update_player_health(state_machine):
    if state_machine.player_location == state_machine.enemy_location:
        state_machine.set_health('player', 0)

if __name__ == "__main__":
    main()