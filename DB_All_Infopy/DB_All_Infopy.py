import boto3
import csv

AccessKey=""
SecretKey=""
region ="ap-south-1"


Pack_list = []
#
header = ["DB_Name","DBInstanceClass","Engine","InstanceStatus","MasterUsername","AvailabilityZone","VpcSecurityGroups","DBSubnetGroupName","DBSubnetGroupDescription","VpcId","SubnetGroupStatus","Endpoint_Address","Endpoint_Port","Endpoint_HostedZoneId","Subnets"]

def Write_to_file():
    with open('countries.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        # write the header
        writer.writerow(header)
        # write multiple rows
        writer.writerows(Pack_list)
def Forloop():
    print(" forloop Length",len(Pack_list))
    for line in Pack_list:
        print(line)
    print(Pack_list)
    Write_to_file()

def update_list(My_data):
   #print("Update List Fun",My_data )
   Pack_list.append(My_data)
   #print("Pack_List",Pack_list)



def main():
    My_data = []
    Pack_list = []
    ec2_client = boto3.client('rds',aws_access_key_id=AccessKey,aws_secret_access_key=SecretKey, region_name=region)
    response = ec2_client.describe_db_instances()
    My_SG_D=[]
    Subnet_List = []
    Secutity_Group=[]
    Sub_subnets=[]

    for re_data in response["DBInstances"]:
        My_data.append(re_data["DBInstanceIdentifier"])
        My_data.append(re_data["DBInstanceClass"])
        My_data.append(re_data["Engine"])
        My_data.append(re_data["DBInstanceStatus"])
        My_data.append(re_data["MasterUsername"])
        My_data.append(re_data["AvailabilityZone"])


        for VPC_Status in re_data["VpcSecurityGroups"]:
            print(VPC_Status["VpcSecurityGroupId"])
            print(VPC_Status["Status"])
            My_SG_D.append(VPC_Status["VpcSecurityGroupId"])
            My_SG_D.append(VPC_Status["Status"])
            Secutity_Group.append(My_SG_D.copy())
            My_SG_D.clear()
            #Secutity_Group.append(VPC_Status)

        My_data.append(Secutity_Group)

        My_data.append(re_data["DBSubnetGroup"]["DBSubnetGroupName"])
        My_data.append(re_data["DBSubnetGroup"]["DBSubnetGroupDescription"])
        My_data.append(re_data["DBSubnetGroup"]["VpcId"])
        My_data.append(re_data["DBSubnetGroup"]["SubnetGroupStatus"])


        for DBSubnetGroup in re_data["DBSubnetGroup"]["Subnets"]:
            Sub_subnets.append(DBSubnetGroup["SubnetIdentifier"])
            Sub_subnets.append(DBSubnetGroup["SubnetAvailabilityZone"]["Name"])
            Sub_subnets.append(DBSubnetGroup["SubnetStatus"])
            Subnet_List.append(Sub_subnets.copy())
            Sub_subnets.clear()

        My_data.append(re_data["Endpoint"]["Address"])
        My_data.append(re_data["Endpoint"]["Port"])
        My_data.append(re_data["Endpoint"]["HostedZoneId"])


        #My_data.append(Secutity_Group)
        My_data.append(Subnet_List)
        #print(My_data)
        update_list(My_data)
        My_data=[]
        Subnet_List=[]
        Secutity_Group=[]


if __name__ == "__main__":
    main()
    #Forloop()