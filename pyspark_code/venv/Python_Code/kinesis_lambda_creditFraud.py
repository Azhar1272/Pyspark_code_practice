import boto3
import json
from datetime import datetime

# Initialize services
dynamodb = boto3.resource('dynamodb')
sns = boto3.client('sns')
table = dynamodb.Table('TransactionHistory')
sns_topic_arn = 'arn:aws:sns:region:account-id:FraudAlerts'

def lambda_handler(event, context):
    for record in event['Records']:
        # Decode the Kinesis record
        payload = json.loads(record['kinesis']['data'])
        card_number = payload['card_number']
        amount = payload['amount']
        location = payload['location']
        timestamp = payload['timestamp']
        
        # Check historical data for patterns
        response = table.get_item(Key={'card_number': card_number})
        if 'Item' in response:
            last_transaction = response['Item']
            last_location = last_transaction['location']
            last_timestamp = datetime.strptime(last_transaction['timestamp'], '%Y-%m-%dT%H:%M:%S')
            
            # Check for suspicious patterns
            if location != last_location and (datetime.now() - last_timestamp).seconds < 300:
                flag_transaction(payload, "Rapid transactions in different locations")
            elif amount > 10000:
                flag_transaction(payload, "High transaction amount")
        
        # Update the transaction history
        table.put_item(Item=payload)
        
    return {'statusCode': 200, 'body': 'Processed records'}

def flag_transaction(transaction, reason):
    message = f"Suspicious transaction detected: {reason}\nDetails: {json.dumps(transaction)}"
    sns.publish(TopicArn=sns_topic_arn, Message=message)
