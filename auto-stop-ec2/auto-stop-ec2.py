import boto3
region = 'ap-northeast-1'
instances = []
instances.append('target instance ID1')
instances.append('target instance ID2')

ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.stop_instances(InstanceIds=instances)
    print('stopped your instances: ' + str(instances))