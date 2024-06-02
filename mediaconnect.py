import boto3

# Initialize AWS clients
mediaconnect_client = boto3.client('mediaconnect', region_name='eu-north-1')

# Define the ARN of MediaConnect flow
mediaconnect_flow_arn = 'arn:aws:mediaconnect:eu-north-1:654654526886:flow:1-XQtfX1NUXlNcDw9X-3088f53c1c53:flow1'

# Function to check if the MediaConnect flow is active
def is_mediaconnect_flow_active():
    try:
        response = mediaconnect_client.describe_flow(FlowArn=mediaconnect_flow_arn)
        status = response['Flow']['Status']
        return status == 'ACTIVE'
    except Exception as e:
        print("Failed to check MediaConnect flow status:", e)
        return False

# Function to start a MediaConnect flow
def start_mediaconnect_flow():
    try:
        if is_mediaconnect_flow_active():
            print("MediaConnect flow is already running.")
        else:
            response = mediaconnect_client.start_flow(FlowArn=mediaconnect_flow_arn)
            print("MediaConnect flow started successfully.")
    except Exception as e:
        print("Failed to start MediaConnect flow:", e)

# Function to stop a MediaConnect flow
def stop_mediaconnect_flow():
    try:
        if not is_mediaconnect_flow_active():
            print("MediaConnect flow is already stopped.")
        else:
            response = mediaconnect_client.stop_flow(FlowArn=mediaconnect_flow_arn)
            print("MediaConnect flow stopped successfully.")
    except Exception as e:
        print("Failed to stop MediaConnect flow:", e)

# Main function
def main():

    # Start or stop MediaConnect flow. Check both the functions one by one.
    start_mediaconnect_flow()
    stop_mediaconnect_flow()

if __name__ == "__main__":
    main()

