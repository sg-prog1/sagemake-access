import boto3

AWS_ACCESS_KEY_ID = "AKIARJ5AUHRXZCKQZ5WS"
AWS_SECRET_ACCESS_KEY = "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"
REGION = "us-east-1"

NOTEBOOK_NAME = "BiasAnalysis"

sm = boto3.client(
    "sagemaker",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=REGION,
)

def presign_notebook(name, duration=3600):
    r = sm.create_presigned_notebook_instance_url(
        NotebookInstanceName=name,
        SessionExpirationDurationInSeconds=duration
    )
    print(r["AuthorizedUrl"])

def presign_studio(domain_id, user_profile, duration=3600):
    r = sm.create_presigned_domain_url(
        DomainId=domain_id,
        UserProfileName=user_profile,
        SessionExpirationDurationInSeconds=duration
    )
    print(r["AuthorizedUrl"])

if __name__ == "__main__":
    presign_notebook(NOTEBOOK_NAME)
    # presign_studio(DOMAIN_ID, USER_PROFILE)
