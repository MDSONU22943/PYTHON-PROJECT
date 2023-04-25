from instabot import Bot
bot=Bot()
bot.login(username="so_nukh_an",password="sonucecbilaspur2020")
'''bot.follow("wscubetechindia")
bot.unfollow("wscubetechindia")
bot.upload_photo("path of photo")

bot.send_message("i love python",["rv_goswami_2","wscubetechindia"])     '''
followers=bot.get_user_followers("so_nukh_an")
for follower in followers:
    print(bot.get_user_info(follower))


followings=bot.get_user_following("so_nukh_an")
for following in followings:
    print(bot.get_user_info(following))


