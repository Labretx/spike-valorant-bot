import os

import hikari

from spike_bot import Spike


def main():
    bot = Spike(
        os.environ["SPIKE_TOKEN"],
        intents=hikari.Intents.ALL,
    )

    @bot.listen(hikari.StartedEvent)
    async def on_start(event: hikari.StartedEvent) -> None:
        print("Bot started successfully!")

    bot.load_extensions_from("./spike_bot/extensions")
    bot.run()


if __name__ == "__main__":
    main()
