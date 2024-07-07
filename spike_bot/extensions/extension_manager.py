import hikari
import lightbulb


plugin = lightbulb.Plugin("Extension Manager")


@plugin.command()
@lightbulb.add_checks(lightbulb.owner_only)
@lightbulb.option(
    "extension",
    "the extension to be unloaded",
    type=str,
    required=True,
)
@lightbulb.command("unload", "unloads an extension <Admin>", hidden=True)
@lightbulb.implements(lightbulb.SlashCommand)
async def unload_ext(ctx: lightbulb.SlashContext):
    plugin.bot.unload_extensions(f"extensions.{ctx.options.extension}")
    await plugin.bot.sync_application_commands()
    await ctx.respond(
        f"The {ctx.options.extension} extension got unloaded",
        flags=hikari.MessageFlag.EPHEMERAL,
    )


@plugin.command()
@lightbulb.add_checks(lightbulb.owner_only)
@lightbulb.option(
    "extension",
    "the extension to be loaded",
    type=str,
    required=True,
)
@lightbulb.command("load", "loads an extension <Admin>", hidden=True)
@lightbulb.implements(lightbulb.SlashCommand)
async def load_ext(ctx: lightbulb.SlashContext):
    plugin.bot.load_extensions(f"extensions.{ctx.options.extension}")
    await ctx.respond(
        f"The {ctx.options.extension} extension got loaded",
        flags=hikari.MessageFlag.EPHEMERAL,
    )


@plugin.command()
@lightbulb.add_checks(lightbulb.owner_only)
@lightbulb.option(
    "extension",
    "the extension to be reloaded",
    type=str,
    required=True,
)
@lightbulb.command("reload", "reloads an extension <Admin>", hidden=True)
@lightbulb.implements(lightbulb.SlashCommand)
async def reload_ext(ctx: lightbulb.SlashContext):
    plugin.bot.reload_extensions(f"extensions.{ctx.options.extension}")
    await plugin.bot.sync_application_commands()
    await ctx.respond(
        f"The {ctx.options.extension} extension got reloaded",
        flags=hikari.MessageFlag.EPHEMERAL,
    )


def load(bot):
    bot.add_plugin(plugin)
