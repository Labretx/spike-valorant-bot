create_servers_table_query = """
        CREATE TABLE IF NOT EXISTS servers (
            server_id BIGINT UNIQUE PRIMARY KEY,
            setup_completed BOOLEAN,
            main_embed_color INTEGER,
            listener_id BIGINT
        )""".strip()

create_server_roles_table_query = """
        CREATE TABLE IF NOT EXISTS server_roles (
            server_id_FK BIGINT REFERENCES servers (server_id),
            role_name VARCHAR,
            role_id BIGINT
        )""".strip()

create_accounts_table_query = """
        CREATE TABLE IF NOT EXISTS accounts (
            discord_id BIGINT UNIQUE PRIMARY KEY,
            val_account_id VARCHAR UNIQUE,
            account_name VARCHAR,
            region VARCHAR
        )""".strip()

create_rank_info_table_query = """
        CREATE TABLE IF NOT EXISTS rank_info (
            account_id_FK VARCHAR UNIQUE REFERENCES accounts (val_account_id),
            rank_name VARCHAR,
            rank_num SMALLINT,
            peak_rank VARCHAR,
            peak_season VARCHAR,
            rating INTEGER,
            mmr_change SMALLINT,
            main_agent VARCHAR
        )""".strip()

create_server_association_table_query = """
        CREATE TABLE IF NOT EXISTS server_association (
            account_id_FK BIGINT REFERENCES accounts (discord_id),
            server_id_FK BIGINT REFERENCES servers (server_id)
        )""".strip()

table_creation_queries = [
    create_servers_table_query,
    create_accounts_table_query,
    create_rank_info_table_query,
    create_server_association_table_query,
    create_server_roles_table_query,
]
