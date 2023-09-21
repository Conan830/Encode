#    Copyright (c) 2021 Danish_00
#    Improved By @Zylern

from decouple import config

try:
    APP_ID = "8440502"
    API_HASH = "e77474ae3075f4000d3418c5a5a3a112"
    BOT_TOKEN = "6313365364:AAGNYx53Iuw8opE8hj_Y_G0oqLAyVbSJuVI"
    DEV = "1315975369"
    OWNER = "1315975369"
    ffmpegcode = ["-preset faster -c:v libx265 -s 854x480 -x265-params 'bframes=8:psy-rd=1:ref=3:aq-mode=3:aq-strength=0.8:deblock=1,1' -metadata 'title=Encoded By TGVid-Comp (https://github.com/Zylern/TGVid-Comp)' -pix_fmt yuv420p -crf 30 -c:a libopus -b:a 32k -c:s copy -map 0 -ac 2 -ab 32k -vbr 2 -level 3.1 -threads 1"]
    THUMBNAIL = "https://telegra.ph/file/c63c3bcf7512f14750c9e.jpg"
except Exception as e:
    print("Environment vars Missing! Exiting App.")
    print(str(e))
    exit(1)
