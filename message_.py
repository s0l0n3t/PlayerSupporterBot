import telegram


from telegram.ext import Updater,CommandHandler,MessageHandler,Filters

COMMANDS ="""/start start the bot !  
/status Check avaible raw materials"""
RAW_WOOD=0
RAW_STONE=0
RAW_IRON=0


def Message_start(update,context):
    update.message.reply_text('TW-Tumper_bot has been started.')
    #type "/start" for this function.

def Message_raw_materials(update,context):
    update.message.reply_text('Wood:%s Stone:%s Iron:%s'%(RAW_WOOD,RAW_STONE,RAW_IRON))
    #raw information for  /status

def Message_help(update,context):
    update.message.reply_text(COMMANDS)

def main():
    token_bot = "BOT_TOKEN" 
    token_updater = Updater(token_bot,use_context=True)
    dp = token_updater.dispatcher
    dp.add_handler(CommandHandler("start",Message_start))
    dp.add_handler(CommandHandler("status",Message_raw_materials))
    dp.add_handler(CommandHandler("help",Message_help))

    token_updater.start_polling()
    mytelegram_id ="338442260" #@userinfobot id

     
    token_updater.dispatcher.bot.send_message(chat_id=mytelegram_id,text='A signal message')


    token_updater.idle()
   

if __name__=='__main__':
    main()
    
    
        