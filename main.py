import os

import hikari
import asyncpg

from spike_bot import Spike, DatabaseManager


def main():
    bot = Spike(
        os.environ["SPIKE_TOKEN"],
        intents=hikari.Intents.ALL,
    )

    @bot.listen(hikari.StartedEvent)
    async def on_start(event: hikari.StartedEvent) -> None:
        postgres_password = os.environ["POSTGRES_PASSWORD"]
        postgres_url = f'postgres://postgres:{postgres_password}@postgres:5432/spike'
        pool = await asyncpg.create_pool(postgres_url)
        print("Database pool acquired.")
        dbm = DatabaseManager(pool)
        bot.dbm = dbm
        await bot.dbm.create_tables()
        print("Bot started successfully!")

    bot.load_extensions_from("./spike_bot/extensions")
    bot.run()


if __name__ == "__main__":
    main()
