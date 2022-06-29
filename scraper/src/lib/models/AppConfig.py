from operator import eq
import os


class AppConfig:
    def __init__(
        self,
        eqt_base_url,
        gc_private_key_id,
        gc_private_key,
        gc_client_email,
        gc_client_id,
        gc_token_uri,
        gc_project_id,
        target_bucket
    ):
        self.eqt_base_url = eqt_base_url
        self.gc_private_key_id = gc_private_key_id
        self.gc_private_key = gc_private_key
        self.gc_client_email = gc_client_email
        self.gc_client_id = gc_client_id
        self.gc_token_uri = gc_token_uri
        self.gc_project_id = gc_project_id
        self.target_bucket = target_bucket
    
    @classmethod
    def from_environment(cls):
        return cls(
            eqt_base_url=os.getenv('EQT_BASE_URL', 'https://eqtgroup.com'),
            gc_private_key_id=os.environ['GC_PRIVATE_KEY_ID'],
            gc_private_key=os.environ['GC_PRIVATE_KEY'].replace('\\n', '\n'),
            gc_client_email=os.environ['GC_CLIENT_EMAIL'],
            gc_client_id=os.environ['GC_CLIENT_ID'],
            gc_token_uri=os.environ['GC_TOKEN_URI'],
            gc_project_id=os.environ['GC_PROJECT_ID'],
            target_bucket=os.getenv('TARGET_BUCKET', 'markus-hont-eqt-scraper')
        )
