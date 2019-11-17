# Bloons-TD-5-Network-Protocol
Reverse engineering the network protocol of Bloons TD 5. My goal is to create a custom game client. 

Feel free to contribute to this project. Install a Windows Packet Inspector. I've used Microsoft Network Monitor.
Open the game inside your browser and analyze the traffic sent to, and from, the server.

There is a matchmaking server, and a game server. The matchmaking server creates your match request, finds a buddy or enemey to play with, and sends you the details of the game server to use.

Messages are sent seperated by comma's. The first digits are the command, followed by arguments.
For example: 9, 1337, MohinderQ, 100

9 means User Joined, followed by the char_id, char_name, and char_lvl

#Network protocol

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
