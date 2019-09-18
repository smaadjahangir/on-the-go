import sys
import boto3
from botocore.exceptions import ClientError

sm_notebooks = []
sm = boto3.client('sagemaker')
response = sm.list_notebook_instances(StatusEquals='InService')

sm = boto3.client('sagemaker')

response = sm.list_notebook_instances(StatusEquals='InService')


for r in response['NotebookInstances']:
        sm_notebooks.append(r['NotebookInstanceName'])

# loop over the instances and reboot any with high avg cpu
for instance in sm_notebooks:
	response = sm.stop_notebook_instance(
		NotebookInstanceName=instance
	)

        print(response)
