# Hack WashU Rolebot

This is Hack WashU's automatic verification bot. Given a list of users in a file called `users.txt` separated by newlines,
this bot automatically removes a role on join.

This lets you assume anybody joining a server is unverified until proven otherwise. This is very useful for events (like Hack WashU!)
where you need to verify large numbers of users in a short amount of time.

**Please read over the code!** It has specific channel & role IDs that need swapping out. Your bot ID is received from a .env file with the variable name `TOKEN`.

You'll need to change three variables:

- The role you want to remove (called `unverified`)
- The admin channel where messages should be sent when automatic verification fails
- A log channel to send messages on successful verification

To run:

```python
pip install discord.py          # install dependencies
python app.js                   # run the app
```

This app requires both the members and guilds intents.