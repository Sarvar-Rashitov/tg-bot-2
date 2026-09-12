from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
import env


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update.effective_user)

    first_name = update.effective_user.first_name
    last_name = update.effective_user.last_name

    if last_name == None:
        last_name = ""

    reply_text = update.message.reply_text(f"Assalomu alaykum, {first_name} {last_name}")
    await reply_text



#====Bu About funksiyasi=====
async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Biz ipeschool o'quvchilarimiz!")



#=====Bu help funksiyasi=====
async def get_help(update: Update, context: ContextTypes.DEFAULT_TYPE):

    help_text = f"""
Botmizda 3 ta comanda bor:
1. /start -> botni ishga tushurish
2. /about -> biz haqimizda
3. /help  -> yordam markazi

Meneger bilan bog'lanish uchun:
tell: +998500104307
telegram: @Sarvar_Rashitov
"""
    await update.message.reply_text(help_text)


async def get_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    print(text)

    await update.message.reply_text(f"Xabaringizni oldim \n\n {text}")



async def get_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo = update.message.photo[-1]

    photo_id = photo.file_id
    print(photo_id)

    username = update.effective_user.username
    user_id = update.effective_user.id

    if username is None:
        username = user_id

    file = await context.bot.get_file(photo_id)

    filename = f"photos/{username}.jpg"

    await file.download_to_drive(filename)

    await update.message.reply_photo(photo_id)



async def get_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    video = update.message.video

    video_id = video.file_id
    print(video_id)

    username = update.effective_user.username
    user_id = update.effective_user.id

    if username is None:
        username = user_id

    file = await context.bot.get_file(video_id)

    filename = f"videos/{username}.mp4"

    await file.download_to_drive(filename)

    await update.message.reply_video(video_id)



async def get_audio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    audio = update.message.audio

    audio_id = audio.file_id

    name = audio.file_name

    file = await context.bot.get_file(audio_id)

    filename = f"audios/{name}"

    await file.download_to_drive(filename)

    await update.message.reply_audio(audio_id)



async def get_voice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    voice = update.message.voice

    voice_id = voice.file_id
    print(voice_id)

    username = update.effective_user.username
    user_id = update.effective_user.id

    if username is None:
        username = user_id

    file = await context.bot.get_file(voice_id)

    filename = f"voices/{username}.mp3"

    await file.download_to_drive(filename)

    await update.message.reply_voice(voice_id)


# telegram severi bilan bog'lanadigan qism
app = Application.builder().token(env.BOT_TOKEN).build()


#====Bu joyda handlerlar bor=====
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("about", about))
app.add_handler(CommandHandler("help", get_help))

app.add_handler(MessageHandler(filters.TEXT, get_text))
app.add_handler(MessageHandler(filters.PHOTO, get_photo))
app.add_handler(MessageHandler(filters.VIDEO, get_video))
app.add_handler(MessageHandler(filters.AUDIO, get_audio))
app.add_handler(MessageHandler(filters.VOICE, get_voice))


print("Bot ish tushdi...")
app.run_polling()

