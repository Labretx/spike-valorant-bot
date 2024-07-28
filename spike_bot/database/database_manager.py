import typing as t

import asyncpg

from spike_bot.database.queries import table_creation_queries


class DatabaseManager:
    connection_pool: t.Optional[asyncpg.Pool]

    def __init__(self, connection_pool: t.Optional[asyncpg.Pool]) -> None:
        self.connection_pool = connection_pool

    async def create_tables(self) -> None:
        if self.connection_pool:
            async with self.connection_pool.acquire() as con:
                for query in table_creation_queries:
                    await con.execute(query)
