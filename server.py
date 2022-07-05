import os
import random

import cherrypy

"""
This is a simple Battlesnake server written in Python.
For instructions see https://github.com/BattlesnakeOfficial/starter-snake-python/README.md
"""
# https://github.com/sayantani11/BattleSnake

class Battlesnake(object):
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def index(self):
        # This function is called when you register your Battlesnake on play.battlesnake.com
        # It controls your Battlesnake appearance and author permissions.
        # TIP: If you open your Battlesnake URL in browser you should see this data
        return {
            "apiversion": "1",
            "author": "theportablegeek",  # TODO: Your Battlesnake Username
            "color": "#D2B48C",  # TODO: Personalize
            "head": "trans-rights-scarf",  # TODO: Personalize
            "tail": "rbc-necktie",  # TODO: Personalize
        }

    @cherrypy.expose
    @cherrypy.tools.json_in()
    def start(self):
        # This function is called everytime your snake is entered into a game.
        # cherrypy.request.json contains information about the game that's about to be played.
        data = cherrypy.request.json

        print("START")
        return "ok"

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def move(self):
        # This function is called on every turn of a game. It's how your snake decides where to move.
        # Valid moves are "up", "down", "left", or "right".
        # TODO: Use the information in cherrypy.request.json to decide your next move.
        data = cherrypy.request.json

# https://github.com/efhiggins3/battlesnake/blob/master/server.py
# https://github.com/SimonSchmitke/battlesnakes/blob/main/server.py

        boardHeight = data['board']['height']-1
        boardWidth = data['board']['width']-1
        
        headX = data['you']['head']['x']
        headY = data['you']['head']['y']

        # foodX = data['you']['head']['x']
        # foodY = data['you']['head']['y']

        # # Where my snake came from
        # neckX = data["you"]["body"][1]["x"]
        # neckY = data["you"]["body"][1]["y"]

        # Choose a random direction to move in
        possible_moves = ["up", "down", "left", "right"]

      #  # Avoid walls
      #   if headX == boardWidth:
      #     possible_moves.remove("right")
      #   if headY == 0:
      #     possible_moves.remove("down")
      #   if headX == 0:
      #     possible_moves.remove("left")
      #   if headY == boardHeight:
      #     possible_moves.remove("up")

      #   # Avoid turning back on myself
      #   if headY == neckY - 1:
      #     possible_moves.remove("up")
      #   if headY == neckY + 1:
      #     possible_moves.remove("down")
      #   if headX == neckX - 1:
      #     possible_moves.remove("right")
      #   if headX == neckX + 1:
      #     possible_moves.remove("left")

      #   move = random.choice(possible_moves)

      
        if headX == 0 and headY != boardHeight:
            move = "up"
        if headY == 0 and headX != 0:
            move = "left"
        if headX == boardWidth and headY != 0:
            move = "down"
        if headY == boardHeight and headX != boardWidth:
            move = "right"
        # else: 

        # # Avoid running into any piece of the body
        # new_x = my_x + move_values[move]["x"]
        # new_y = my_y + move_values[move]["y"]

        # for seg in data["you"]["body"]:
        #   if seg["x"] == new_x and seg["y"] == new_y:
        #     possible_moves.remove(move)
        #     # Pull a new move
        #     move = random.choice(possible_moves)


          
        print(f"MOVE: {move}")
        return {"move": move}

    @cherrypy.expose
    @cherrypy.tools.json_in()
    def end(self):
        # This function is called when a game your snake was in ends.
        # It's purely for informational purposes, you don't have to make any decisions here.
        data = cherrypy.request.json

        print("END")
        return "ok"


if __name__ == "__main__":
    server = Battlesnake()
    cherrypy.config.update({"server.socket_host": "0.0.0.0"})
    cherrypy.config.update(
        {"server.socket_port": int(os.environ.get("PORT", "8080")),}
    )
    print("Starting Battlesnake Server...")
    cherrypy.quickstart(server)
