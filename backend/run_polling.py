import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings.dev')
django.setup()


def run_polling():
    from telegram.polling_bot import create_polling_bot

    bot = create_polling_bot()
    print('Infinity polling started successfully')
    bot.infinity_polling()


if __name__ == "__main__":
    run_polling()
