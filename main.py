import logging
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

logHandler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
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
                logger.info(
                    "Instance ID: %s, Type: %s, Public IP: %s, Private IP: %s, Zone: %s, State: %s, Tags: %s",
                    instance['InstanceId'],
                    instance['InstanceType'],
                    instance.get('PublicIpAddress', 'N/A'),
                    instance['PrivateIpAddress'],
                    instance['Placement']['AvailabilityZone'],
                    instance['State']['Name'],
                    instance.get('Tags', [])
                )

    except Exception as e:
        logger.error(e)


if __name__ == '__main__':
    list_running_instances()
