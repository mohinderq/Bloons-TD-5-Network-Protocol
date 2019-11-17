from client import Client
from gameclient import GameClient


class MenuClient(Client):

    #GAME_IP AND GAME_HOST
    game_host = None
    game_port = None

    #COMMAND INFORMATION
    CREATE_GAME = '3'
    CONNECTION_ACCEPTED = '18'
    QUICK_MATCH_FOUND = '13'
    GAME_CREATED = '4'
    USER_JOINED_GAME = '9'
    GAME_NOT_FOUND = '8'

    def started(self):
        self.send("17,13042601,13504721,Skudjemoer,65,4")

    def say(self, message, p2, p3=-1):
        if p2 is None:
            p2 = "null"
        self.send(message + "," + self.version + "," + p2 + "," + str(p3))

    def receive(self, message, args):
        self.debug('Receiving {} {}'.format(message, args))
        if message == self.CONNECTION_ACCEPTED:
            self.debug("Connection accepted.")
            self.send("12,1:1:0:0:1:1:1")
        elif message == self.QUICK_MATCH_FOUND:
            self.debug("Opponent found.")
            self.game_host = args[0]
            self.game_port = args[1]
            self.send("15")
            self.create_game_client(self.game_host, int(self.game_port), args[3])
        elif message == self.USER_JOINED_GAME:
            self.debug("User joined your game")
            #self.create_game_client(str(self.game_host), int(self.game_port))

    def create_game_client(self, host, port, enemy_id):
        gameclient = GameClient(host, port, enemy_id)
        gameclient.connect()
        gameclient.start()

    def game_information(self):
        mode = str(self.CREATE_GAME)
        room_name = 'MYCOOLROOM'
        map_name = 'PumpkinPatch'
        level = '2'  # 0 easy, 1 medium, 2 hard
        reverse = '0'
        information = [mode, room_name, map_name, level, reverse]
        return ','.join(information)
