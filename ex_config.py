# FOR SELF HOST
# EDIT THIS FILE AND RENAME TO config.py TO MAKE THIS BOT WORKING
# FILL THESE VALUES ACCORDINGLY.

from HellConfig.config import Config


class Development(Config):
    # get these values from my.telegram.org.
    
    APP_ID = 27440220  # 666666 is a placeholder. Fill your 6 digit api id
    
    API_HASH = "598a62c944bf3a1f72e79d129f957ef4"  # replace this with your api hash
    
    BOT_TOKEN = "5756049480:AAGlZNsOPgUByySd1YF7OsB13_Oyfjh1Y4g"  # Create a bot from @BotFather and paste the token here
    
    BOT_LIBRARY = "telethon"  # fill 'pyrogram' if you want pyrogram version of hellbot else leave it as it is.

    DB_URI = "mongodb+srv://toaa:toaa69@cluster0.eduoooo.mongodb.net/?retryWrites=true&w=majority"  # A postgresql database url from elephantsql

    HELLBOT_SESSION = "1BVtsOG8Buz7wYwrzm6_hr5RvHeTggal3RfdjjedRnmU0jwrCb_svTqZdKq_DB8F1WkOlqtxBv6mfiaLsX4GCNrRbuW9TYOR4fPLC4nZUsGMS8iy6C2qvTEApayMcKBq_HffL4x2_0dTZ27uTxzBQ1VeS_dUDJGiejEtMlcznrbrAfUCJpwUuer80ea49AlBXWUUfXT6p42Jkhny1tsT6mJ07PdPJwjcqmk1OMGMH1NyKzZNyORE9eDPHlqJON6vM29wDJkz9t5k6y4EF8PZzpqjHDAIBTrU3VAZ64ErzHAMsGf0Hp7Jx4buhn6NOrYIWa9v_PnyNu6oKqaZW3z1Rff-mGigBO8U="  # telethon or pyrogram string according to BOT_LIBRARY

    HANDLER = "."  # Custom Command Handler

    SUDO_HANDLER = "!"  # Custom Command Handler for sudo users.


# end of required config
# hellbot
