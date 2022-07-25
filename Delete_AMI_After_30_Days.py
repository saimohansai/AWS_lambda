import boto3
from boto3 import ec2
from datetime import datetime
AccessKey=""
SecretKey=""
region ="us-east-1"


def Days_Compare(AWS_date):
    Present_date = str(datetime.now()).split(" ")[0]
    AWS_date = AWS_date.split("T")[0]

    # convert string to date object
    d1 = datetime.strptime(Present_date, "%Y-%m-%d")
    d2 = datetime.strptime(AWS_date, "%Y-%m-%d")

    # difference between dates in timedelta
    delta = d1 - d2
    print(f'Difference is {delta.days} days')
    return delta.days
    #region delta.days

def list_of_images():
    ec2_client = boto3.client('rds', aws_access_key_id=AccessKey, aws_secret_access_key=SecretKey,
                              region_name=region)

    #response = ec2_client.describe_images(Owners=['341153521279'])
    response = ec2_client.describe_images(Owners=['self'])
    print(type(response))
    #print(response)
    for reservation in response["Images"]:
     # print(rav)
        print("Image {0} --> date {1}".format(reservation["ImageId"],reservation["CreationDate"]))
        count_days =Days_Compare(reservation["CreationDate"])
        if count_days >=30:
            try:
                print("Image_id",reservation["ImageId"])
                # Enable after validation
                #instance_Delete= ec2_client.deregister_image(ImageId=reservation["ImageId"], DryRun=False)
                #print(instance_Delete)
            except:
                print("filed in deleteing the AMI")

list_of_images()






