import boto3
import click


@click.command()
@click.argument('code', type=str)  # Sagemaker passes this down by default, this is here for click to not throw an error
@click.option('--s3-bucket-name', type=str, required=True, default='decision-science-emr')
def hello_aws(code: str, s3_bucket_name: str) -> None:  # pylint: disable=unused-argument
    s3_client = boto3.client('s3')
    print(s3_client.list_objects(Bucket=s3_bucket_name))


if __name__ == '__main__':
    hello_aws()  # pylint: disable=no-value-for-parameter
