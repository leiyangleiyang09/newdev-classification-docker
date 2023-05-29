from __future__ import absolute_import, division, print_function, unicode_literals
import click
import boto3
import json

from ids_feed import live_feed
from ids_classification import offline_ids_classification


def extract_credentials_from_sm(boto_session: boto3.session, secret_names: list) -> dict:
    sm_client = boto_session.client(service_name='secretsmanager')
    _config = {}
    for secret_name in secret_names:
        res = sm_client.get_secret_value(SecretId=secret_name)
        json_res = json.loads(res['SecretString'])
        _config.update(json_res)
    return _config


@click.command()
@click.argument('code', type=str)  # Sagemaker passes this down by default, this is here for click to not throw an error
@click.option('--s3-bucket-name', type=str, required=True, default='decision-science-emr')
@click.option('--run-date-str', type=str, required=True, default='20200101_010100')
def da_classify(code: str, s3_bucket_name: str, run_date_str: str) -> None:
    s3_client = boto3.client('s3')
    session = boto3.session.Session(region_name='ap-southeast-2')
    config = extract_credentials_from_sm(boto_session=session,
                                         secret_names=['datascientist_mssql_nlp', 'datascientist_listing_nlp',
                                                       'datascientist_snowflake_elt'])

    # yr_start = 1990
    # yr_end = 2022
    # processing_list_dic = offline_feed(config, yr_start, yr_end)
    # result_csv = offline_ids_classification(processing_list_dic)
    # filename = 'ids_labelling_update_%s.csv' % run_date_str
    # s3_client.put_object(Body=result_csv, Bucket=s3_bucket_name, Key='ids_labelling/' + filename)
    processing_list_dic = live_feed(config)
    result_csv = offline_ids_classification(processing_list_dic)
    filename = 'ids_labelling_update_%s.csv' % run_date_str
    s3_client.put_object(Body=result_csv, Bucket=s3_bucket_name, Key='ids_labelling/' + filename)


if __name__ == '__main__':
    da_classify()
