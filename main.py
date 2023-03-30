import logging
import boto3
from pythonjsonlogger import jsonlogger

logger = logging.getLogger()
logger.setLevel(logging.INFO)

logHandler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter()
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)


ec2 = boto3.client('ec2')

def list_running_instances():
    try:
        # Retrieve all running instances
        instances = ec2.describe_instances(
            Filters=[
                {
                    'Name': 'instance-state-name',
                    'Values': ['running']
                }
            ]
        )

        ## Log instance information
        for reservation in instances['Reservations']:
            for instance in reservation['Instances']:
                logger.info({
                    "instance_id":
                        instance['InstanceId'],
                    "instance_type":
                        instance['InstanceType'],
                    "public_ip_address": instance.get('PublicIpAddress', 'N/A'),
                    "private_ip_address":
                        instance['PrivateIpAddress'],
                    "availability_zone": instance['Placement']['AvailabilityZone'],
                    "state":
                        instance['State']['Name'],
                    "tags":
                        instance.get('Tags', [])
                })

    except Exception as e:
        logger.error(e)


list_running_instances()
