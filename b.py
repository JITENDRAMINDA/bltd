from pyrogram import Client, Filters,Emoji
from pyrogram.errors import FloodWait
import time
app = Client("my_acc",854941,"bf9632f82af99dc8c3b934ab48d54780")
s = -1001262096355
d = -1001316388816
@app.on_message(Filters.chat(s) & Filters.text & ~Filters.edited)
def forward(client,Message):
 f = False
 words = ['dekho','TRUST','join','fix','😱','😳','👆','👇','☝️','https://','😂','🤔','pass','chase','link','suno','member','❓','loss','audio','open',"report",'paid','contact','baazigar','market','load','whatsapp','book','bhai','🐴','only','chut','tennis','teen','lavde','chutiya','bc','kya','line','LUND','WICKET LU','?','loda','telegram','chor',"kama","lakh",' id','स',"kitna"]
 for word in words:
  if word.casefold() in Message.text.casefold():
   f = True
 if not f:
  if "🎾" in Message.text:
   mes = client.send_message(d,"<b>" + ' '.join(Message.text.replace("🖲","🇨🇭").replace("📟","📮").replace("🇩🇪","🇮🇶").replace("🇦🇲","🇮🇶").split("🎾")[:-1]) + "🎾" + "</b>",parse_mode= "html")
  else:
   mes = client.send_message(d, Message.text.markdown.replace("🖲","🇨🇭").replace("📟","📮").replace("🇩🇪","🇮🇶").replace("🇦🇲","🇮🇶")) 
  files = open("sure.txt" , "a")
  files.write(" " + str(Message.message_id) +  " " + str(mes.message_id))
  files.close()
@app.on_message(Filters.chat(s) & Filters.text & Filters.edited)
def forward(client,Message):
 file = open("sure.txt" , "r")
 lines = file.readlines()
 file.close()
 for line in lines:
  x = line.split()
  id = str(Message.message_id)
  if id in x:
   try:
    if "🎾" in Message.text:
     client.edit_message_text(d,int(x[x.index(id)+1]),"<b>" + ' '.join(Message.text.replace("🖲","🇨🇭").replace("📟","📮").replace("🇩🇪","🇮🇶").replace("🇦🇲","🇮🇶").split("🎾")[:-1]) + "</b>" + "🎾",parse_mode="html")
    else:
     client.edit_message_text(d,int(x[x.index(id)+1]),Message.text.markdown.replace("🖲","🇨🇭").replace("📟","📮").replace("🇩🇪","🇮🇶").replace("🇦🇲","🇮🇶")) 
   except FloodWait as e:
    time.sleep(e.x)
@app.on_deleted_messages(Filters.chat(s))
def main(client, messages):
 for v in messages:
  file = open("sure.txt" , "r")
  lines = file.readlines()
  file.close()
  for line in lines:
   x = line.split()
   id = str(v.message_id )
   if id in x:
    try:
     client.delete_messages(d,int(x[x.index(id)+1]))
    except FloodWait as e:
     time.sleep(e.x)
@app.on_message(Filters.command("c"))
def main(client, message):
 with open("sure.txt" , "w") as files:
  files.write("")
  files.close()
  message.reply("Done") 
app.run()
