from pyrogram import Client, Filters,Emoji
from pyrogram.errors import FloodWait
import time
from emoji import UNICODE_EMOJI
app = Client(session_name="llx",api_id=814511,api_hash="44462f0f278503255d5cc30941b617a9",bot_token ="765108996:AAGYA2lsT6yw1q5SEx1PXesPWYdwb8RBivc")
d = -1001315425757
s = -1001203491308
g = ["0","1","2","3","4","6","NEED","RUN","CATCH","DROP","BALL","🚾","📟","RAIN","HAWA","WD","WIDE","NB","PLAYING","OVER","WON","WIN","BOTH","CHALU","COVER","START","STOP","ME","+","XI","✔️","GANA","GAANA","TIE","WKT","WICKET","☄️","HIT"]
@app.on_message(Filters.chat(s) & Filters.text & ~Filters.edited)
def forward(client,Message):
 r = s = False
 words = ['dekho','TRUST','join','fix','😱','😳','👆','👇','☝️','https://','😂','🤔','pass','chase','link','suno','member','❓','loss','audio','open',"report",'paid','contact','baazigar','market','load','whatsapp','book','bhai','🐴','only','chut','tennis','teen','lavde','chutiya','bc','kya','line','LUND','WICKET LU','?','loda','telegram','chor',"kama","lakh",' id','स',"kitna"]
 for word in words:
  if word.casefold() in Message.text.casefold():
   return
 for i in Message.text.split(' '):
  if i in UNICODE_EMOJI:
   r = True
  for p in g:
   if p.casefold() in Message.text.casefold():
    s = True
 if r or s:
  if "🎾" in Message.text:
   mes = client.send_message(d,"<b>" + ' '.join(Message.text.replace("🖲","🙇🏼‍♂").replace("📟","🎳").replace("🇩🇪","🇮🇶").replace("🇦🇲","🇮🇶").split("🎾")[:-1]) + "🎾" + "</b>",parse_mode= "html")
  else:
   mes = client.send_message(d, Message.text.markdown.replace("🖲","🙇🏼‍♂").replace("📟","🎳").replace("🇩🇪","🇮🇶").replace("🇦🇲","🇮🇶")) 
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
     client.edit_message_text(d,int(x[x.index(id)+1]),"<b>" + ' '.join(Message.text.replace("🖲","🙇🏼‍♂").replace("📟","🎳").replace("🇩🇪","🇮🇶").replace("🇦🇲","🇮🇶").split("🎾")[:-1]) + "</b>" + "🎾",parse_mode="html")
    else:
     client.edit_message_text(d,int(x[x.index(id)+1]),Message.text.markdown.replace("🖲","🙇🏼‍♂").replace("📟","🎳").replace("🇩🇪","🇮🇶").replace("🇦🇲","🇮🇶")) 
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
@app.on_message(Filters.command("cyy"))
def main(client, message):
 x = "😀😃😄😁😆😅☺️😊😇🙂🙃😉😌😍🥰😘😗😙😚😋😛😝😜🤪🤨🧐🤓😎🤩🥳😏😒😞😔😟😕🙁☹️😣😖😫😩😤😠😡🤬🤯🥵😨🤗🤭🤫🤥😶😐😑😬🙄😯😦😧😮😲😴🤤😪😵🤐🥴🤢🤮🤧😷🤒🤕🤑🤠😈👿🤡💩👻💀☠👽👾🤖🎃😺😸😹😻🤲👐🙌👏🤝👍👎👊✊🤛🤜🤞✌️🤟🤘👌✋🤚🖐🖖👋🤙💪✍🦶🦵💄🦷👅👂👃👣👁👀🧠🗣👤👥👶👧🧒👦👩🧑👨👩‍🦱👨‍🦱👩‍🦰👵🧓👴👲👳‍♀👳‍♂🧕👮‍♀👮‍♂👷‍♀👷‍♂💂‍♀💂‍♂🕵‍♀🕵‍♂👩‍⚕👨‍⚕👩‍🌾👨‍🌾👩‍🍳👨‍🍳👩‍🎓👨‍🎓👩‍🎤👨‍🎤👩‍🏫👨‍🏫👩‍🏭👨‍🏭👩‍💼👨‍💼👩‍🔧👨‍🔧👩‍🔬👨‍🔬👩‍🎨👨‍🎨👩‍🚒👩‍✈️👨‍✈️👩‍🚀👨‍🚀👩‍⚖👨‍⚖👰🤵👸🤴🦸‍♀🦸‍♂🦹‍♀🦹‍♂🤶🎅🧙‍♀🧙‍♂🧝‍♀🧝‍♂🧛‍♀🧛‍♂🧟‍♀🧟‍♂🧞‍♀🧞‍♂🧜‍♀🧜‍♂🧚‍♀🧚‍♂👼🤰🤱🙇‍♀🙇‍♂💁‍♀💁‍♂🙅‍♀🙅‍♂🙆‍♀🙆‍♂🙋‍♀🙋‍♂🤦‍♀🤦‍♂🤷‍♀🤷‍♂🙎‍♀🙎‍♂🙍‍♀🙍‍♂💇‍♀💇‍♂💆‍♀💆‍♂🧖‍♀🧖‍♂💅🤳💃🕺👯‍♀👯‍♂🕴🚶‍♀🚶‍♂🏃‍♀🏃‍♂👫👭👬⌚️📱📲💻⌨🖥🖨🖱🖲🕹🗜💽💾💿📀📼📷📹🎥🎞📞☎️📟📠📺📻🎙🎚🎛🧭⏱⏲⏰🕰⌛️⏳📡🔋🔌💡🔦🕯🧯🛢💸💵💴💶💷💰💳💎⚖🧰🔧🔨⚒🛠⛏🔩⚙🧱⛓🧲🔫💣🧨🔪🗡⚔🛡🚬⚰⚱🏺🔮📿🧿💈⚗🔭🔬🕳💊💉🧬🦠🧫🧪🌡🧹🧺🧻🚽🚰🚿🛁🛀🧼🧽🧴🛎🔑🗝🚪🛋🛏🛌🧸🖼🛍🛒🎁🎈🎏🎀🎊🎉🎎🏮🎐🧧✉️📩📨📧💌📥📤📦🏷📪📫📬📭📮📯📜📃🧾📊📈🗒🗓🗑📇🗃🗳🗄📋📁📂🗂🗞📰📓📚📖🔖🧷🔗📎🖇📐📏🧮📌📍✂️🖊🖋✒️🖌🖍📝✏️🔍🔎🔏🔐🔒🔓❤️🧡💛💚💙💜🖤💔❣💕💞💓💗💖💘💝💟☮✝☪🕉☸✡🔯🕎☯☦🛐⛎♈️♉️♊️🉑☢☣📴📳🈶🈚️🈸🈺🈷✴️🆚🅰🅱🆎🆑🅾🆘❌⭕️🛑⛔️📛🚫💯💢♨️🚷🚯🚳🚱🔞📵🚭‼️⁉️⁉️🔅🔆〽️⚠️🚸🔱⚜🔰♻️✅❇️✳️❎🌐💠Ⓜ️🌀💤🏧🚾♿️🅿️🈳🈂🛂🛃🛄🛅🚹🚺🚼🚻🚮🎦📶🈁🔣ℹ️🔤🔡🔠🆖🆗🆙🆒🆕🆓0⃣1⃣2⃣3⃣4⃣5⃣6⃣7⃣8⃣9⃣🔟🔢#⃣*⃣⏏▶️⏸⏯⏹⏺⏭⏮⏩⏪⏫⏬◀️🔼🔽➡️⬅️⬆️⬇️↗️↘️↙️↖️↔️↔️↪️↩️⤴️⤵️🔀🔁🔂🔄🔃🎵🎶➕➖➗✖️♾💲💱™©®👁‍🗨🔚🔙🔛🔝🔜〰➰➿✔️☑️🔘⚪️⚫️🔴🔵🔺🔻🔸🔹🔶🔷🔳🔲▪️▫️◾️◽️◼️◻️⬛️⬜️🔈🔇🔉🔊🔔🔕📣📢💬💭🗯♠️♣️♥️♦️🃏🎴🀄️🕐🏳🏴🏴‍☠🏁🚩🏳‍🌈🇺🇳🇦🇫🇦🇽🇦🇱🇩🇿🇦🇸🇦🇩🇦🇴🇦🇮🇦🇶🇦🇬🇦🇷🇦🇲🇦🇼🇦🇺🇦🇹🇦🇿🇧🇸🇧🇭🇧🇩🇧🇧🇧🇾🇧🇪🇧🇿🇧🇯🇧🇲🇧🇹🇧🇴🇧🇦🇧🇼🇧🇷🇮🇴🇻🇬🇧🇳🇧🇬🇧🇫🇧🇮🇰🇭🇨🇲🇨🇦🇮🇨🇨🇻🇧🇶🇰🇾🇨🇫🇹🇩🇨🇱🇨🇳🇨🇽🇨🇨🇨🇴🇰🇲🇨🇬🇨🇩🇨🇰🇨🇷🇨🇮🇭🇷🇨🇺🇨🇼🇨🇾🇨🇿🇩🇰🇩🇯🇩🇲🇩🇴🇪🇨🇪🇬🇸🇻🇬🇶🇪🇷🇪🇪🇪🇹🇪🇺🇫🇰🇫🇴🇫🇯🇫🇮🇫🇷🇬🇫🇵🇫🇹🇫🇬🇦🇬🇲🇬🇪🇩🇪🇬🇭🇬🇮🇬🇷🇬🇱🇬🇩🇬🇵🇬🇺🇬🇹🇬🇬🇬🇳🇬🇼🇬🇾🇭🇹🇭🇳🇭🇰🇭🇺🇮🇸🇮🇳🇮🇩🇮🇷🇮🇶🇮🇪🇮🇲🇮🇱🇮🇹🇯🇲🇯🇵🎌🇯🇪🇯🇴🇰🇿🇰🇪🇰🇮🇽🇰🇰🇼🇰🇬🇱🇦🇱🇻🇱🇧🇱🇸🇱🇷🇱🇾🇱🇮🇱🇹🇱🇺🇲🇴🇲🇰🇲🇬🇲🇼🇲🇾🇲🇻🇲🇱🇲🇹🇲🇭🇲🇶🇲🇷🇲🇺🇾🇹🇲🇽🇫🇲🇲🇩🇲🇨🇲🇳🇲🇪🇲🇸🇲🇦🇲🇿🇲🇲🇳🇦🇳🇷🇳🇵🇳🇱🇳🇨🇳🇿🇳🇮🇳🇪🇳🇬🇳🇺🇳🇫🇰🇵🇲🇵🇳🇴🇴🇲🇵🇰🇵🇼🇵🇸🇵🇦🇵🇬🇵🇾🇵🇪🇵🇭🇵🇳🇵🇱🇵🇹🇵🇷🇶🇦🇷🇪🇷🇴🇷🇺🇷🇼🇼🇸🇸🇲🇸🇹🇸🇦🇸🇳🇷🇸🇸🇨🇸🇱🇸🇬🇸🇽🇸🇰🇸🇮🇬🇸🇸🇧🇸🇴🇿🇦🇰🇷🇸🇸🇪🇸🇱🇰🇧🇱🇸🇭🇰🇳🇱🇨🇵🇲🇻🇨🇸🇩🇸🇷🇸🇿🇸🇪🇨🇭🇸🇾🇹🇼🇹🇯🇹🇿🇹🇭🇹🇱🇹🇬🇹🇰🇹🇴🇹🇹🇹🇳🇹🇷🇹🇲🇹🇨🇹🇻🇻🇮🇺🇬🇺🇦🇦🇪🇬🇧🏴󠁧󠁢󠁥󠁮󠁧󠁿🏴󠁧󠁢󠁳󠁣󠁴󠁿🏴󠁧󠁢󠁷󠁬󠁳󠁿🇺🇸🇺🇾🇺🇿🇻🇺🇻🇦🇻🇪🇻🇳🇼🇫🇪🇭🇾🇪🇿🇲🇿🇼🧶🧵🧥🥼👚👕👖👔👗👙👘🥿👠👡👢👞👟🥾🧦🧤🧣🎩🧢👒🎓⛑👑💍👝👛👜💼🎒🧳👓🕶🥽🌂🐶🐱🐭🐹🐰🦊🐻🐼🐨🐯🦁🐮🐷🐽🐸🐵🙈🙉🙊🐒🐔🐧🐦🐤🐣🐥🦆🦅🦉🦇🐺🐗🐴🦄🐝🐛🦋🐌🐞🐜🦟🦗🕷🕸🦂🐢🐍🦎🦖🦕🐙🦑🦐🦞🦀🐡🐠🐟🐬🐳🐋🦈🐊🐅🐆🦓🦍🐘🦛🦏🐪🐫🦒🐃🐂🐄🐎🐖🐏🐑🦙🐐🦌🐕🐩🐈🐓🦃🦚🦜🦢🕊🐇🦝🦡🐁🐀🐿🦔🐾🐉🐲🌵🎄🌳🌴🌱🌿☘🍀🎍🎋🍃🍂🍁🍄🐚🌾💐🌷🌹🥀🌺🌸🌼🌻🌞🌝🌏💫⭐️🌟✨⚡️☄💥🔥🌪🌈☀️🌤⛅️🌥☁️🌦🌧⛈🌩🌨❄️☃⛄️🌬💨💧💦☔️☂🌊🌫🍏🍎🍐🍊🍋🍌🍉🍇🍓🍈🍒🍑🥭🍍🥥🥝🍅🍆🥑🥦🥬🥒🌶🌽🥕🥔🍠🥐🥯🍞🥖🥨🧀🥚🍳🥞🥓🥩🍗🍖🦴🌭🍔🍟🍕🥪🥙🌮🌯🥗🥘🥫🍝🍜🍲🍛🍣🍱🥟🍤🍙🍚🍘🍥🥠🥮🍢🍡🍧🍨🍦🥧🧁🍰🎂🍮🍭🍬🍫🍿🍩🍪🌰🥜🍯🥛🍼☕️🍵🥤🍶🍺🍻🥂🍷🥃🍸🍹🍾🥄🍴🍽🥣🥡🥢🧂⚽️🏀🏈⚾️🥎🎾🏐🏉🥏🎱🏓🏸🏒🏑🥍🏏🥅⛳️🏹🎣🥊🥋🎽🛹🛷⛸🥌🎿⛷🏂🏋‍♀🏋‍♂🤼‍♀🤼‍♂🤸‍♀🤸‍♂⛹‍♀⛹‍♂🤺🤾‍♀🤾‍♂🏌‍♀🏌‍♂🏇🧘‍♀🧘‍♂🧗‍♀🧗‍♂🚴‍♀🚴‍♂🏆🥇🥈🥉🏅🎖🏵🎗🎫🎟🎪🤹‍♀🤹‍♂🎭🎨🎬🎤🎧🎼🎹🥁🎷🎺🎸🎻🎲♟🎯🎳🎮🎰🧩🚗🚕🚙🚌🚎🏎🚓🚑🚒🚐🚚🚛🚜🛴🚲🛵🏍🚨🚔🚍🚘🚖🚡🚠🚟🚃🚋🚞🚝🚄🚅🚈🚂🚆🚇🚊🚉✈️🛫🛬🛩💺🛰🚀🛸🚁🛶⛵️⛴🚢⚓️⛽️🚧🚦🚥🚏🗺🗿🗽🗼🏰🏯🏟🎡🎢🎠⛲️⛱🏖🏝🏜🌋⛰🏔🗻🏕⛺️🏠🏡🏘🏚🏗🏭🏢🏬🏣🏤🏥🏦🏨🏪🏫🏩💒🏛⛪️🕌🕍🕋⛩🛤🛣🗾🎑🏞🌠"
 y = [j for j in x[0].split(" ")]
 message.reply(y)
 with open("sure.txt" , "w") as files:
  files.write("")
  files.close()
  message.reply("Done") 
app.run()
