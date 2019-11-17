from client import Client


class GameClient(Client):

    CREATE_GAME = '3'
    CONNECTION_ACCEPTED = '18'
    GAME_CREATED = '4'
    MONEY_REQUEST = '209'

    def __init__(self, server, port, enemy_id):
        super().__init__(server, port)
        self.enemy_id = enemy_id

    def started(self):
        self.send("101,{},13504721,Skudjemoer,none,-1,0".format(self.enemy_id))

    def say(self, message, p2, p3=-1):
        if p2 is None:
            p2 = "null"
        self.send(message + "," + self.version + "," + p2 + "," + str(p3))

    def receive(self, message, args):
        try:
            if args[0] is not '207':
                self.debug('Receiving {} {}'.format(message, args))
        except:
            pass
        if message == '105':
            self.debug("Connection accepted.")
            self.send('109')
        elif message == self.GAME_CREATED:
            self.debug("Game created. Waiting for opponent.")
        elif message == '102':
            self.send('106,219')
        if args:
            if args[0] == self.MONEY_REQUEST:
                self.debug('User asked for money')
                self.send('106,208,100')
        self.ping()

    def ping(self):
        self.send('106,207,146.900,1000,663,74,0')
        self.send('106,222,')
