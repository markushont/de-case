import json
from typing import List
from google.cloud import storage
from google.oauth2 import service_account

from lib.models.AppConfig import AppConfig

class CloudStorageClient:
    
    def __init__(
        self,
        project_id,
        service_account_creds_dict
    ):
        credentials = service_account.Credentials.from_service_account_info(service_account_creds_dict)
        self.client = storage.Client(project=project_id, credentials=credentials)

    def put_newline_json(self, bucket: str, path: str, obj: List[dict]):
        bucket = self.client.get_bucket(bucket)
        blob = bucket.blob(path)
        blob.upload_from_string(
            data=str('\n'.join([json.dumps(r) for r in obj]))
        )

    def list_files(self, bucket: str, path_prefix: str=None):
        return self.client.list_blobs(bucket, prefix=path_prefix)

    @staticmethod
    def credentials_from_app_config(app_config: AppConfig) -> dict:
        return {
            'client_email': app_config.gc_client_email,
            'client_id': app_config.gc_client_id,
            'private_key_id': app_config.gc_private_key_id,
            'private_key': app_config.gc_private_key,
            'token_uri': app_config.gc_token_uri,
            'type': 'service_account'
        }
