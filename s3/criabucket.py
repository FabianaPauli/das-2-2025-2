import boto3

s3_client = boto3.client("s3" , region_name="us-east-1")
#aqui conecto o meu bucket na AWS, sa-east-1 é a região SP. us-east-1 é em norte virginia

s3_client.create_bucket(Bucket="fabiana2002")
print("Bucket criado com sucesso")