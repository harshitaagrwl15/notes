aws ec2 describe-instances --query 'Reservations[].Instances[].{InstanceID:InstanceId, SecurityGroups:SecurityGroups[*].{GroupName:GroupName, GroupId:GroupId}}' --output table
