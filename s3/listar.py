import boto3

s3_client = boto3.resource("s3" , region_name="us-east-1")
#aqui conecto o meu bucket na AWS, sa-east-1 é a região SP. us-east-1 é em norte virginia

bucket = s3_client.Bucket("fabiana2002")

for obj in bucket.objects.all():
    print(f"-{obj.key} - {obj.size} bytes")
