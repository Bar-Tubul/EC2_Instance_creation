import boto3
from datetime import datetime

date = datetime.now().strftime("%d-%m-%y")

def get_conf():
    with open('configuration.txt') as config:
        info = config.read()
        return info

def get_user_data():
    with open('user-data.sh') as httpd:
        httpd_installtion = httpd.read()
        return httpd_installtion

def create_instances():
    config = get_conf()
    user_data = get_user_data()

    config_lines = config.splitlines()
    instance_type = config_lines[0].split(":")[1].strip()
    key_name = config_lines[1].split(":")[1].strip()
    image_id = config_lines[2].split(":")[1].strip()
    security_group = config_lines[3].split(":")[1].strip()
    number_of_instances = int(config_lines[4].split(":")[1].strip())
    subnet_id = config_lines[5].split(":")[1].strip()

    ec2 = boto3.resource('ec2')
    instance = ec2.create_instances(
        InstanceType=instance_type,
        MinCount=number_of_instances,
        MaxCount=number_of_instances,
        ImageId=image_id,
        KeyName=key_name,
        SecurityGroupIds=[security_group],
        SubnetId=subnet_id,
        UserData=user_data,
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {'Key': 'Date', 'Value': date}
                ]
            }
        ]
    )

    counter = 1

    for i, instance in enumerate(instance):
        instance.wait_until_running()
        instance.load()
        instance.create_tags(
            Tags=[{'Key': 'Name', 'Value': 'bar_' + str(counter)}]
        )
        print("Instance bar_" + str(counter) + " Private IP: " + instance.private_ip_address)

        counter += 1

create_instances()
