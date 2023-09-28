aws ec2 describe-instances --query 'Reservations[].Instances[].{InstanceID:InstanceId, SecurityGroups:SecurityGroups[*].{GroupName:GroupName, GroupId:GroupId}}' --output table

aws ec2 describe-instances --query 'Reservations[].Instances[].{InstanceID:InstanceId, InstanceName:Tags[?Key==`Name`].Value | [0], SecurityGroups:SecurityGroups[*].{GroupName:GroupName, GroupId:GroupId}}' --output table

aws ec2 describe-vpc-endpoints --query 'VpcEndpoints[].{ServiceName:ServiceName, DNSName:DnsEntries[0].DnsName}' --output table

