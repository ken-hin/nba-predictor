from nba_api.stats.endpoints import playercareerstats
import pandas as pandas


class Player:
  def __init__(self, play_id):
        self.play_id = play_id
        self.player = playercareerstats.PlayerCareerStats(player_id=play_id)

  def print_stats(self):
        play_df = self.player.get_data_frames()[0]
        print(self.player.expected_data)
        print(play_df)

# json
# career.get_json()

# dictionary
# career.get_dict()
