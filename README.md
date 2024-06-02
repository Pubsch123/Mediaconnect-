# MediaConnect Flow Management

This repository provides Python scripts to manage an AWS Elemental MediaConnect flow. It includes functions to start and stop a MediaConnect flow, as well as check its current status. The script uses the AWS SDK for Python (Boto3) to interact with the MediaConnect service.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- You have an AWS account with necessary permissions to manage MediaConnect flows.
- You have AWS credentials configured on your machine.
- You have Python 3.x installed on your machine.

## Setup

### 1. Clone the Repository
Clone this repository to your local machine:
```sh
git clone <repository_url>
```
Replace `<repository_url>` with the actual URL of the repository.

### 2. Create and Activate a Virtual Environment
It's recommended to use a virtual environment to manage dependencies.

#### On Windows
```sh
python -m venv venv
.\venv\Scripts\activate
```

#### On macOS/Linux
```sh
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
Install the required Python packages:
```sh
pip install boto3
```

### 4. Configure AWS Credentials
Configure your AWS credentials. You can do this using the AWS CLI:
```sh
aws configure
```
Alternatively, set the following environment variables:
```sh
export AWS_ACCESS_KEY_ID=your_access_key_id
export AWS_SECRET_ACCESS_KEY=your_secret_access_key
export AWS_DEFAULT_REGION=your_region
```

## Usage

### Description of Functions
- **is_mediaconnect_flow_active**: Checks if the MediaConnect flow is currently active.
- **start_mediaconnect_flow**: Starts the MediaConnect flow if it is not already running.
- **stop_mediaconnect_flow**: Stops the MediaConnect flow if it is currently running.

### Example Usage
The `main` function demonstrates how to use the provided functions to manage a MediaConnect flow. You can uncomment the relevant lines to either start or stop the MediaConnect flow.

#### To Start the MediaConnect Flow
Keep the line `start_mediaconnect_flow()` uncommented in the `main` function and comment out the `stop_mediaconnect_flow()` line:
```python
def main():
    # Start or stop MediaConnect flow. Check both the functions one by one.
    start_mediaconnect_flow()
    # stop_mediaconnect_flow()
```
Run the script:
```sh
python script.py
```

#### To Stop the MediaConnect Flow
Uncomment the line `stop_mediaconnect_flow()` in the `main` function and comment out the `start_mediaconnect_flow()` line:
```python
def main():
    # Start or stop MediaConnect flow. Check both the functions one by one.
    # start_mediaconnect_flow()
    stop_mediaconnect_flow()
```
Run the script:
```sh
python script.py
```

## Error Handling
The script includes basic error handling to catch and print exceptions that may occur during AWS API calls. Ensure that your AWS credentials and permissions are correctly configured to avoid authorization errors.

## Contributing
If you wish to contribute to this project, please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

Feel free to reach out if you have any questions or need further assistance. Happy coding!
