#!/bin/bash

# Get instance IDs
instance_ids=$(aws ec2 describe-instances --query "Reservations[*].Instances[*].InstanceId" --output text)

# Loop through each instance and retrieve its security group information
for instance_id in $instance_ids; do
    echo "Instance ID: $instance_id"

    # Get security group IDs associated with the instance
    security_group_ids=$(aws ec2 describe-instances --instance-ids $instance_id --query "Reservations[*].Instances[*].SecurityGroups[*].GroupId" --output text)

    # Loop through each security group and retrieve its name and ID
    for sg_id in $security_group_ids; do
        sg_name=$(aws ec2 describe-security-groups --group-ids $sg_id --query "SecurityGroups[*].GroupName" --output text)
        echo "  Security Group Name: $sg_name (ID: $sg_id)"
    done

    echo  # Add a new line for separation
done
