from util.database_connector import extract_data_from_snowflake
from util.ids_clean import clean_data, clean_text


def offline_feed(config: str, yr_start: int, yr_end: int) -> dict:
    listing_detail_dic = {}

    query = """SELECT LISTING_AD_ID, LISTING_LAST_MODIFIED_TIMESTAMP, LISTING_CREATED_TIMESTAMP,
                      LISTING_PRICE_PREFIX, LISTING_SUMMARY, LISTING_DESCRIPTION, PROPERTYID
               FROM PRODDOMAINDW.CORE.CORE_LISTING
               WHERE LISTING_TYPE = 'Sale' AND
                     LISTING_CHANNEL_NAME = 'Residential' AND
                     EXTRACT(YEAR FROM LISTING_CREATED_TIMESTAMP) BETWEEN %s AND %s
                     AND LISTING_AD_ID in (2008105398, 2008342684);""" % (yr_start, yr_end)
    property_result = extract_data_from_snowflake(config, query)

    for property_result in property_result:
        sale_id = str(property_result[0]).strip()
        update_date = str(property_result[1]).split('.')[0]
        insert_date = str(property_result[2]).split('.')[0]

        price_prefix = property_result[3]
        if price_prefix:
            price_prefix = clean_data(price_prefix).strip()
        else:
            price_prefix = str(price_prefix)
        price_prefix = clean_text(price_prefix).strip().lower()

        summary = property_result[4]
        if summary:
            summary = clean_data(summary).strip()
        else:
            summary = str(summary)
        summary = summary.replace('<br />', '\n')
        summary = summary.replace('<br/>', '\n')
        summary = summary.replace('<br>', '\n')
        summary = summary.replace('&amp;', ' ')
        summary = summary.replace('<b>', ' ')
        summary = summary.replace('</b>', ' ')
        summary = clean_text(summary).strip().lower()

        description = property_result[5]
        if description:
            description = clean_data(description).strip()
        else:
            description = str(description)
        description = description.replace('<br />', '\n')
        description = description.replace('<br/>', '\n')
        description = description.replace('<br>', '\n')
        description = description.replace('&amp;', ' ')
        description = description.replace('<b>', ' ')
        description = description.replace('</b>', ' ')
        description = clean_text(description).strip().lower()

        property_id = property_result[6]
        if not property_id:
            property_id = 'NULL'

        listing_detail_dic[sale_id] = [sale_id, property_id, price_prefix, summary,
                                       description, update_date, insert_date]
    return listing_detail_dic


def live_feed(config: str) -> dict:
    listing_detail_dic = {}

    query = """SELECT max(EXECUTION_DATE)
               FROM "PRODDOMAINDW"."DATA_SCIENCE_NLP"."IDS_DISTRESSED_SELL_CLASSIFICATION";"""
    result = extract_data_from_snowflake(config, query)
    previous_run = str(result[0][0]).split('.')[0]
    print("----------> previous run date: ", [previous_run])

    query = ("""SELECT LISTING_AD_ID, LISTING_LAST_MODIFIED_TIMESTAMP, LISTING_CREATED_TIMESTAMP,
                      LISTING_PRICE_PREFIX, LISTING_SUMMARY, LISTING_DESCRIPTION, PROPERTYID
                FROM PRODDOMAINDW.CORE.CORE_LISTING
                WHERE LISTING_TYPE = 'Sale' AND
                      LISTING_CHANNEL_NAME = 'Residential' AND
                      (LISTING_LAST_MODIFIED_TIMESTAMP >= '%s' OR LISTING_CREATED_TIMESTAMP >= '%s');"""
             % (previous_run, previous_run))
    property_result = extract_data_from_snowflake(config, query)

    print("----------> Step 1 Number of items in the record: ", len(property_result))
    for property_result in property_result:
        sale_id = str(property_result[0]).strip()
        update_date = str(property_result[1]).split('.')[0]
        insert_date = str(property_result[2]).split('.')[0]

        price_prefix = property_result[3]
        if price_prefix:
            price_prefix = clean_data(price_prefix).strip()
        else:
            price_prefix = str(price_prefix)
        price_prefix = clean_text(price_prefix).strip().lower()

        summary = property_result[4]
        if summary:
            summary = clean_data(summary).strip()
        else:
            summary = str(summary)
        summary = summary.replace('<br />', '\n')
        summary = summary.replace('<br/>', '\n')
        summary = summary.replace('<br>', '\n')
        summary = summary.replace('&amp;', ' ')
        summary = summary.replace('<b>', ' ')
        summary = summary.replace('</b>', ' ')
        summary = clean_text(summary).strip().lower()

        description = property_result[5]
        if description:
            description = clean_data(description).strip()
        else:
            description = str(description)
        description = description.replace('<br />', '\n')
        description = description.replace('<br/>', '\n')
        description = description.replace('<br>', '\n')
        description = description.replace('&amp;', ' ')
        description = description.replace('<b>', ' ')
        description = description.replace('</b>', ' ')
        description = clean_text(description).strip().lower()

        property_id = property_result[6]
        if not property_id:
            property_id = 'NULL'

        listing_detail_dic[sale_id] = [sale_id, property_id, price_prefix, summary,
                                       description, update_date, insert_date]
    return listing_detail_dic
