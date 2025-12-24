# Discord-to-Insta-Bot
Simple Discord Bot to make posting for multiple people on one Instagram account easier

With the Instabot you can post videos, images and albums to instagram from discord if you have the **InstabotPoster** role

## Why?
If you want to share an instagram account with friends without giving out login informations and wanting people to know who posted what, this can make it easier to share that account

## How it works
with the message "ib- post {Caption}" you can post photos in **JPEG** fromat and videos in **MP4** format

If you use this source code you should change account Logins to the Instagram account at **LINE 34** and add the token of the discord bot at the last line (**LINE 128**)

When Posting stuff it will use the discord username to show who created the post and the message in the command as the caption

## How to customise the bot
- Most outward stuff like pfp, name, e.t.c can be changed on instagram or the discord api website
- If you want to change the discord role name that is used for verifying who can post, in **LINE 57** you can change it (role = discord.utils.get(ctx.guild.roles, name="NEW NAME"))
- If you want to change the boilerplate caption "new post by {user}", in **Line 40** you can change it, the template is: 'caption' \n {boilerplate} {username}
- you can change the discord statuses at **LINE 28** by adding or removing words in the **cycle([])** function
- Prefix changes (ib-) can be done by changing **LINE 20** specifically: *command_prefix="PREFIX "*

## Possible changes
- [ ] Use Different Python Libraries or FFMPEG to change different formats to supported formats *(PNG -> JPEG or WEBM -> MP4)*
- [ ] Use Threads to not worry about disconnecting and reconnecting discord bot *(Mentioned in **LINE 54**)*

> This Project has been not been tested for a few months as i do not have the original Instagram account anymore (deleted it myself)

> Using Instagram bots may be against Instagrams TOS, This was only for educational purposes for me to connect 2 social media apps together
