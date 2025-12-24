# Discord-to-Insta-Bot
Simple Discord Bot to make posting for multiple people on one Instagram account easier

With the Instabot you can post videos, images and albums to instagram from discord if you have the **InstabotPoster** role

## Why?
If you want to share an instagram account with friends without giving out login informations and wanting people to know who posted what, this can make it easier to share that account

## How it works
with the message "ib- post {Caption}" you can post photos in **JPEG** fromat and videos in **MP4** format

If you use this source code you should change account Logins to the Instagram account at **Line 34** and add the token of the discord bot at the last line (**Line 128**)

When Posting stuff it will use the discord username to show who created the post and the message in the command as the caption

## Possible changes
- [ ] Use Different Python Libraries or FFMPEG to change different formats to supported formats *(PNG -> JPEG or WEBM -> MP4)*
- [ ] Use Threads to not worry about disconnecting and reconnecting discord bot *(Mentioned in **LINE 54**)*
