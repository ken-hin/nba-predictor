import player as pl

if __name__ == '__main__':
    player_id = int(input('Enter player ID: '))

    new_player = pl.Player(player_id)
    new_player.print_stats()
