from telegram import Update, InputFile, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# Функция для команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # URL сайта
    website_link = "https://eonatrix.cc/"
    
    # Кнопка с ссылкой
    keyboard = [
        [InlineKeyboardButton("Learn more on the site", url=website_link)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Отправляем фото
    with open("barbara_diabetes.jpg", "rb") as photo:  # Укажите название файла с картинкой
        await context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=photo,
            caption="Barbara O'Neill Shocked Everyone With An Innovative Method To Fight Diabetes. Learn more on the site below.",
            reply_markup=reply_markup,
        )

# Основной запуск бота
def main():
    # Вставьте сюда токен, полученный от @BotFather
    TOKEN = "7501681027:AAGOXUwh5Pgq7lpAygpSaRaU4Vr1Kpv2HjM"

    # Создаём объект приложения
    application = Application.builder().token(TOKEN).build()

    # Регистрируем команду /start
    application.add_handler(CommandHandler("start", start))

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()