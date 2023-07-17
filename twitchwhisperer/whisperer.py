import socket, asyncio

TWITCH_IRC_HOST = 'irc.twitch.tv'
TWITCH_IRC_PORT = 6667

CRLF = "\r\n"

class Whisperer():
    def __init__(self, bot_username: str, twitch_access_token: str):
        self.bot_username = bot_username
        self.twitch_access_token = twitch_access_token
        self.bot_username = self.twitch_access_token.replace('oauth:', '')
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    async def run(self):
        print("Connecting. . . ")
        self.socket.connect((TWITCH_IRC_HOST, TWITCH_IRC_PORT))
        print("Done!")
        # self.socket.sendall(b"Hello, world")

        self.socket.send(f'CAP REQ :twitch.tv/membership twitch.tv/tags twitch.tv/commands'.encode('UTF-8'))
        self.socket.send(f'PASS oauth:{self.twitch_access_token}'.encode('UTF-8'))
        self.socket.send(f'NICK {self.bot_username.lower()}'.encode('UTF-8'))

        data = self.socket.recv(1024)
        print(data)