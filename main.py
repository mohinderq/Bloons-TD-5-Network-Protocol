from matchmaking import MenuClient

menuclient = MenuClient('ext-matchmaker-aws.btd5coopweb.scalr.ws', 5577)
menuclient.connect()
menuclient.start()
