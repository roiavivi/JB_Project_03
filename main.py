import boto3


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

        # Print instance information
        for reservation in instances['Reservations']:
            for instance in reservation['Instances']:
                print(f"Instance ID: {instance['InstanceId']}")
                print(f"Instance Type: {instance['InstanceType']}")
                print(f"Public IP Address: {instance.get('PublicIpAddress', 'N/A')}")
                print(f"Private IP Address: {instance['PrivateIpAddress']}")
                print(f"Availability Zone: {instance['Placement']['AvailabilityZone']}")
                print(f"State: {instance['State']['Name']}")

                # Print instance tags
                tags = instance.get('Tags', [])
                if tags:
                    print("Tags:")
                    for tag in tags:
                        print(f"- {tag['Key']}: {tag['Value']}")

                print("---------------------------")

    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    ec2 = boto3.client('ec2')
    list_running_instances()