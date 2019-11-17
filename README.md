# Bloons-TD-5-Network-Protocol
Reverse engineering the network protocol of Bloons TD 5. My goal is to create a custom game client. 

Feel free to contribute to this project. Install a Windows Packet Inspector. I've used Microsoft Network Monitor.
Open the game inside your browser and analyze the traffic sent to, and from, the server.

There is a matchmaking server, and a game server. The matchmaking server creates your match request, finds a buddy or enemey to play with, and sends you the details of the game server to use.

Messages are sent seperated by comma's. The first digits are the command, followed by arguments.
For example: 9, 1337, MohinderQ, 100

9 means User Joined, followed by the char_id, char_name, and char_lvl

# IP's

The matchmaking server runs on ext-matchmaker-aws.btd5coopweb.scalr.ws:5577.

# Start a quick match

A socket can be used to create a connection to the matchmaking server. The server wants you to identify yourself. You can do so via the `17 command`. The matchmaking server will respond with `18`. 

The connection has been set, and the matchmaker server now knows which player you are. 
A quick match can then be started using the `12` command. The server will respond with a `13` command when an user is found. For some reason you have to respond with only `15`. Then the IP and Port can be grabbed from the `13` command, aswell as the other users character id. This character is later needed when contacting the game server.

```
self.send("101,{},13504721,Skudjemoer,none,-1,0".format(self.enemy_id))
```

If the other users character id is not mentioned in the `101` command the game server will stop responding. When the above command has been send to the game server, the connection has been set and the game will start.

When talking to the game server every message will start with `106,` followed by the arguments. I think `106,` stands for a message about the game state. 

# Network protocol

1 => Match Found 

1, IP, PORT, PORT, CHAR_ID, CHAR_NAME, CHAR_LVL, MAP_NAME, MODE, MAP_REVERSE

13 => Match Found 

13, IP, PORT, PORT, CHAR_ID, CHAR_NAME, CHAR_LVL, MAP_NAME, ?, ?, ?

4 => Game Created

4, IP, PORT, PORT

9 => User joined? 

9, CHAR_ID, CHAR_NAME, CHAR_LVL

6 => Not sure

2 => Join Room 

2, ROOM_NAME


11 => IM ALIVE?? (UNSURE)

14 => ??

15 => IM HERE??

12 => QUICK MATCH

 MATCH SETTINGS:
 BEGINNER:INTERMEDIATE:ADVANCED:EXPERT:EASY:MEDIUM:HARD
 12, 1:1:0:0:1:1:0

17 => Identify yourself at gameserver

17,?,CHAR_ID,CHAR_NAME,CHAR_LVL,?

101 => Identification of match 

101, ENEMY_ID, CHAR_ID, CHAR_NAME, none, -1, 0

102 => Identification of enemy 

102, ENEMY_ID, ENEMY_NAME, none, -1, 0

107 => User left? 

201 => Tower is build 

'201', '-1.000', '-1', '2147483647', 'DartMonkey', '404', '71', '-1.571', '0', '1698552449'
