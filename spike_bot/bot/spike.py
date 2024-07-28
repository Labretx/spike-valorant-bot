import typing as t

import lightbulb

from spike_bot.database import DatabaseManager


class Spike(lightbulb.BotApp):
    dbm: t.Optional[DatabaseManager]

    def __init__(
        self,
        token: str,
        dbm: DatabaseManager | None = None,
        **kwargs: t.Any,
    ) -> None:
        self.dbm = dbm
        super().__init__(
            token,
            help_class=None,
            help_slash_command=False,
            default_enabled_guilds=(),
            owner_ids=(151035927412736000,),
            prefix=None,
            ignore_bots=True,
            delete_unbound_commands=True,
            case_insensitive_prefixes=False,
            case_insensitive_prefix_commands=False,
            **kwargs,
        )
