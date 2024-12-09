import json
import boto3

# Initialize the S3 and DynamoDB clients
s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    # Extract bucket name and object key from the event
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']
    
    try:
        # Fetch the file from S3
        response = s3.get_object(Bucket=bucket_name, Key=object_key)
        file_content = response['Body'].read().decode('utf-8')
        data = json.loads(file_content)
        
        # Reference your DynamoDB table
        table_name = "YourDynamoDBTableName"
        table = dynamodb.Table(table_name)
        
        # Insert data into DynamoDB
        for record in data:
            table.put_item(Item=record)
        
        print(f"Successfully inserted data from {object_key} into DynamoDB table {table_name}")
        return {
            'statusCode': 200,
            'body': json.dumps('Data processed successfully!')
        }
    except Exception as e:
        print(f"Error processing file {object_key}: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps('Error processing data.')
        }
