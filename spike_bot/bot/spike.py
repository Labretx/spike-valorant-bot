from typing import Any

import lightbulb


class Spike(lightbulb.BotApp):
    def __init__(
        self,
        token: str,
        **kwargs: Any,
    ) -> None:
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