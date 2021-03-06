import json
from google.oauth2 import service_account
from google.cloud import bigquery
from secrets_management import get_environment, decrypt_credentials

from .table_operations import create_table, append_to_table, append_rows_to_table


class BigQueryStore():
    def __init__(self, name, schema, adapter_func=None, write_many=None, *args, **kwargs):
        self.is_table_created = False
        credfile = decrypt_credentials()
        creds_json = json.loads(credfile)
        creds = service_account.Credentials.from_service_account_info(creds_json)
        self.client = bigquery.Client(credentials=creds, project=creds_json['project_id'])
        self.name = name
        self.table_schema = schema
        self._adapter = adapter_func
        self._write_many = write_many

    def get_table_name(self):
        env = get_environment()
        return (self.client.project, env, self.name)

    async def write(self, data):
        if not self.is_table_created:
            self.table = await create_table(self.client, self.get_table_name(), self.table_schema)
            self.is_table_created = True
        adapted_data = data if self._adapter is None else self._adapter(data)
        if self._write_many:
            return await append_rows_to_table(self.client, self.table, adapted_data)
        return await append_to_table(self.client, self.table, adapted_data)
