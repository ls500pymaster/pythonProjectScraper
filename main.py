import asyncio
import logging
from aiogram import Bot, Dispatcher, types

from config import EMAIL, PASSWORD, BOT_TOKEN, GROUP_CHAT_ID
from database import create_database_and_table, save_to_database
from scraper import login, scrape_blog

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


async def send_new_posts(chat_id, new_posts):
    for post in new_posts:
        await bot.send_message(chat_id=chat_id, text=
        f'<b>➡️ {post["title"]}.</b> \n <b>▶🌐 {post["link"]}</b>',
                               parse_mode="HTML")


async def main():
    session = login(EMAIL, PASSWORD)
    seen_posts = set()

    # Create the database and table
    conn = create_database_and_table()

    while True:
        scraped_data = scrape_blog(session)
        save_to_database(conn, scraped_data)
        new_posts = [post for post in scraped_data if post['link'] not in seen_posts]

        if new_posts:
            await send_new_posts(GROUP_CHAT_ID, new_posts)
            seen_posts.update(post['link'] for post in new_posts)

            await asyncio.sleep(15)


@dp.message_handler()
async def handle_message(message: types.Message):
    pass


async def on_startup(dp):
    asyncio.create_task(main())

if __name__ == "__main__":
    from aiogram import executor
    executor.start_polling(dp, on_startup=on_startup)

