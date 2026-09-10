from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import env


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update.effective_user)

    first_name = update.effective_user.first_name
    last_name = update.effective_user.last_name

    if last_name == None:
        last_name = ""

    reply_text = update.message.reply_text(f"Assalomu alaykum, {first_name} {last_name}")
    await reply_text


async def cheksiz_salom(update: Update, context: ContextTypes.DEFAULT_TYPE):

    while True:
        await update.message.reply_text("Salom")



app = Application.builder().token(env.BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("cheksiz_salom", cheksiz_salom))

print("Bot ish tushdi...")
app.run_polling()

