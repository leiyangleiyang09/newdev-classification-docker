import snowflake.connector


def run_snowflake_query(config: dict, query: str) -> None:
    # Extract database credentials
    user = config['sf_user']
    password = config['sf_pw']
    account = config['sf_account']
    region = config['sf_region_id']
    database = config['sf_database']
    warehouse = config['sf_warehouse']
    try:
        # Create connection engine
        domain_dw_conn = snowflake.connector.connect(user=user, password=password, account=account,
                                                     region=region, database=database, warehouse=warehouse)
        domain_live_cursor = domain_dw_conn.cursor()
        domain_live_cursor.execute(query)
        query_result = domain_live_cursor.fetchall()
        for row in query_result:
            print(row)
        domain_dw_conn.close()
    except Exception as e:
        print(e)
    return None


def extract_data_from_snowflake(config: dict, query: str) -> list:
    # Extract database credentials
    user = config['sf_user']
    password = config['sf_pw']
    account = config['sf_account']
    region = config['sf_region_id']
    database = config['sf_database']
    warehouse = config['sf_warehouse']
    try:
        # Create connection engine
        domain_dw_conn = snowflake.connector.connect(user=user, password=password, account=account,
                                                     region=region, database=database, warehouse=warehouse)
        domain_live_cursor = domain_dw_conn.cursor()
        domain_live_cursor.execute(query)
        query_result = domain_live_cursor.fetchall()
        domain_dw_conn.close()
    except Exception as e:
        print(e)
    return query_result
