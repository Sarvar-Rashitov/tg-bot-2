from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import env


def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update.effective_user)

    first_name = update.effective_user.first_name
    last_name = update.effective_user.last_name

    if last_name == None:
        last_name = ""

    reply_text = update.message.reply_text(f"Assalomu alaykum, {first_name} {last_name}")
    return reply_text

app = Application.builder().token(env.BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Bot ish tushdi...")
app.run_polling()

