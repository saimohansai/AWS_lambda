import boto3
from boto3 import ec2
from datetime import datetime

AccessKey=""
SecretKey=""
region ="us-east-1"

def Days_Compare(AWS_date):

    Present_date = str(datetime.now()).split(" ")[0]
    AWS_date = AWS_date.split(" ")[0]
    d1 = datetime.strptime(Present_date, "%Y-%m-%d")
    d2 = datetime.strptime(AWS_date, "%Y-%m-%d")
    # difference between dates in timedelta
    delta = d1 - d2
    return delta.days

def list_of_images():
    #ec2_client = boto3.client("ec2", region)
    ec2_client = boto3.client('rds', aws_access_key_id=AccessKey, aws_secret_access_key=SecretKey,
                              region_name=region)
    response = ec2_client.describe_snapshots(OwnerIds=['self'],)
    for reservation in response["Snapshots"]:
        #print("Image {0} --> date {1}".format(reservation["SnapshotId"],reservation["StartTime"]))
        count_days =Days_Compare(str(reservation["StartTime"]))

        if count_days >=30:
            try:
                print("Image {0} --> date {1}".format(reservation["SnapshotId"],count_days))
                # Enable after validation
                #instance_Delete= ec2_client.delete_snapshot(SnapshotId=reservation["SnapshotId"], DryRun=False)
                #print(instance_Delete)
            except:
                print("filed in deleteing the AMI")

list_of_images()








