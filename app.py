import json

# Lambda handler function
# This function is called by AWS Lambda when the function is invoked
# The function receives two arguments: event and context
# The event argument contains the data passed to the function
def lambda_handler(event, context):
    try:
        # Simulate processing the event
        if 'key' not in event:
            raise ValueError("Missing 'key' in event data")

        # Process the event and return a successful response
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Hello from Lambda!'})
        }

    except ValueError as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': str(e)})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Internal Server Error', 'message': str(e)})
        }