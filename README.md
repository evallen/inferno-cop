# inferno-cop
Inferno Cop - A Discord Bot that enforces a set of ridiculous rules my friends come up with. 
"Illegal rules" are listed in regex form in `config.py` - these represent messages that aren't allowed on the server. Infrastructure exists to create rules that do not conform to simple regexes, but they would have to be implemented in `message_checker.py`. All punishments are defined in `punish.py`. 

## Installation and Operation
To run this bot:
1. Clone the code into a folder.
2. Create a file called `token.txt` and paste in the bot's token there. It's not included here because it's a secret (it provides access to the server of your choice). To get the token, go to the Discord applications page and view the bot user you've created (if this doesn't make any sense, go [here](https://discordpy.readthedocs.io/en/latest/discord.html) or contact me if you're on a server with me. 
3. Run `inferno_cop.py`.
