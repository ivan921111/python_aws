import boto3

boto3.session.Session(profile_name='default')

s3 = boto3.client('s3')

def upload_file(file_name, bucket, object_name):
    s3.upload_file(file_name, bucket, object_name)
    print(f"el archivo {file_name} subio al bucket {bucket} as {object_name}")

def download_file(bucket, object_name, file_name):
    s3.download_file(bucket, object_name, file_name)
    print(f"el archivo {object_name} se descargo del bucket {bucket} como {file_name}")

def file_list(bucket):
    response = s3.list_objects_v2(Bucket=bucket)
    if 'Contents' in response:
        for obj in response['Contents']:
            print(obj['Key'])
    else:
        print(f"No hay archivos en el bucket {bucket}")    

bucket_name = "boto3-s3-van"

##upload_file('lab_boto3/subirs3.txt', bucket_name, 'subirs3.txt')

file_list( bucket_name)
