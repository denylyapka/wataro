import asyncio
from contextlib import asynccontextmanager

from aiobotocore.session import get_session


s3_base_link = "https://7bdd6e9d-5639-4742-b439-36560b2a5ee9.selstorage.ru/"

class S3Client:
    def __init__(
            self,
            access_key: str,
            secret_key: str,
            endpoint_url: str,
            bucket_name: str
    ):
        self.config = {
            "aws_access_key_id": access_key,
            "aws_secret_access_key": secret_key,
            "endpoint_url": endpoint_url,
        }
        self.bucket_name = bucket_name
        self.session = get_session()

    @asynccontextmanager
    async def get_client(self):
        async with self.session.create_client("s3", **self.config) as client:
            yield client

    async def upload_file(self, file_path: str):
        object_name = file_path.split("/")[-1]
        async with self.get_client() as client:
            with open(file_path, 'rb') as file:
                await client.put_object(
                    Bucket=self.bucket_name,
                    Key=object_name,
                    Body=file
                )
        return object_name

    async def remove_file(self, file_path: str):
        object_name = file_path.split("/")[-1]
        async with self.get_client() as client:
            await client.delete_object(Bucket=self.bucket_name, Key=object_name)


async def get_name_and_file_upload(file_path):
    s3_client = S3Client(
        access_key="d58e3bf117fb43c999c3503b753bcb94",
        secret_key="865dc5415e654c8789c7e6877c13dace",
        endpoint_url="https://s3.storage.selcloud.ru",
        bucket_name="test-public-bucket-wa-meet-1"
    )
    print(s3_base_link+file_path)
    await s3_client.upload_file(file_path)


async def get_name_and_file_remove(file_path):
    s3_client = S3Client(
        access_key="d58e3bf117fb43c999c3503b753bcb94",
        secret_key="865dc5415e654c8789c7e6877c13dace",
        endpoint_url="https://s3.storage.selcloud.ru",
        bucket_name="test-public-bucket-wa-meet-1"
    )
    await s3_client.remove_file(file_path)


if __name__ == '__main__':
    asyncio.run(get_name_and_file_upload("../src/static/videos/back_ground.mp4"))
