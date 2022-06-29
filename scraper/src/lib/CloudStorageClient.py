from google.cloud import storage
from google.oauth2 import service_account

class CloudStorageClient:
    
    def __init__(
        self,
        project_id,
        service_account_creds_dict
    ):
        credentials = service_account.Credentials.from_service_account_info(service_account_creds_dict)
        self.client = storage.Client(project=project_id, credentials=credentials)

    def put_file(self, bucket, path, fh):
        pass

    def list_files(self, bucket, path_prefix=None):
        return self.client.list_blobs(bucket, prefix=path_prefix)
