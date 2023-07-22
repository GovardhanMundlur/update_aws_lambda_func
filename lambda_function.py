import json
import boto3
from git import Repo

lbda = boto3.client('lambda')

func_name = "testfunc"
git_url   = "https://github.com/GovardhanMundlur/update_aws_lambda_func.git"

#Repo.clone_from(git_url, repo_dir)


def lambda_handler(event, context):
    # response = client.update_function_code(
    #     FunctionName=func_name,
    #     ZipFile=
    #     )
    print("test")
