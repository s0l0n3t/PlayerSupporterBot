import telegram


from telegram.ext import Updater,CommandHandler,MessageHandler,Filters

COMMANDS ="""/start start the bot !  
/status Check avaible raw materials"""
RAW_WOOD=""
RAW_STONE=""
RAW_IRON=""
BOT_TOKEN = "YOUR TOKEN"
PREMIUM_WOOD=""
PREMIUM_STONE=""
PREMIUM_IRON=""




def Message_start(update,context):
    update.message.reply_text('TW-Tumper_bot has been started.')
    #type "/start" for this function.

def Message_premium_exchange(update,context):
    update.message.reply_text("\nPremium information \nWood: %s \n Stone: %s \n Iron: %s"%(PREMIUM_WOOD,PREMIUM_STONE,PREMIUM_IRON))
    #Premium raw material excange status.

def Message_raw_materials(update,context):
    update.message.reply_text('Wood:%s Stone:%s Iron:%s'%(RAW_WOOD,RAW_STONE,RAW_IRON))
    #raw information for  /status

def Message_help(update,context):
    update.message.reply_text(COMMANDS)

def main():
    global mytelegram_id
    global token_updater
    token_updater = Updater(BOT_TOKEN,use_context=True)
    dp = token_updater.dispatcher
    dp.add_handler(CommandHandler("start",Message_start))
    dp.add_handler(CommandHandler("status",Message_raw_materials))
    dp.add_handler(CommandHandler("help",Message_help))
    dp.add_handler(CommandHandler("premium",Message_premium_exchange))
    token_updater.start_polling()
    mytelegram_id ="338442260" #@userinfobot id

     
   # token_updater.dispatcher.bot.send_message(chat_id=mytelegram_id,text='%s'%(MESSAGE))


   # token_updater.idle()
   


    
    
