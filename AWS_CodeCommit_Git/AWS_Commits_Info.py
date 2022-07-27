import csv
import os
import boto3
from datetime import datetime
commit_list=[]
commit_info=[]
Commit_final=[]

repositoryName= " "
AccessKey=" "
SecretKey=" "
region="us-west-2"

client = boto3.client('codecommit',aws_access_key_id=AccessKey, aws_secret_access_key=SecretKey,
                              region_name=region)
header = ["Commit_ID","Commit Message","Date","Days"]

def Write_to_file():
    with open('countries1.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        # write the header
        writer.writerow(header)
        # write multiple rows
        writer.writerows(Commit_final)

def appent_Commit_List(commits_Info):

    Commit_final.append(commits_Info.copy())

def Days_Compare(AWS_date):
    AWS_date = datetime.fromtimestamp(int(AWS_date))
    AWS_date=str(AWS_date).split(" ")[0]
    Present_date = str(datetime.now()).split(" ")[0]
    d1 = datetime.strptime(Present_date, "%Y-%m-%d")
    d2 = datetime.strptime(AWS_date, "%Y-%m-%d")
    # # difference between dates in timedelta
    delta = d1 - d2
    return delta.days,AWS_date



response = client.get_branch(repositoryName = repositoryName, branchName="master")
#print(response)
commitId = response['branch']['commitId']
commit_list.append(commitId)
while(1):
    response = client.get_commit(repositoryName=repositoryName,commitId=commitId)
    Commit_date= response["ResponseMetadata"]["HTTPHeaders"]["date"]
    if len(response["commit"]['parents']) != 0:
        commit_list.append(response["commit"]['parents'][0])
        commitId = response["commit"]['parents'][0]
    else:
        break
for my_Commit in commit_list:
    response = client.batch_get_commits(commitIds=[my_Commit], repositoryName=repositoryName )
    Commit_date = response["commits"][0]["author"]["date"]
    commit_info.append(my_Commit)
    commit_info.append(response["commits"][0]["message"])
    Commit_day_Count,date_Format =Days_Compare("1658814362")
    commit_info.append(date_Format)
    commit_info.append(Commit_day_Count)
    appent_Commit_List(commit_info)
    commit_info=[]
Write_to_file()