from fastapi import APIRouter, UploadFile, File, HTTPException
import boto3
import os
from botocore.exceptions import NoCredentialsError

router = APIRouter()

s3 = boto3.client('s3',
                  aws_access_key_id=os.getenv('MINIO_ACCESS_KEY'),
                  aws_secret_access_key=os.getenv('MINIO_SECRET_KEY'),
                  endpoint_url=os.getenv('MINIO_ENDPOINT'))

BUCKET_NAME = "memes"

@router.post("/upload/")
def upload_file(file: UploadFile = File(...)):
    try:
        s3.upload_fileobj(file.file, BUCKET_NAME, file.filename)
        return {"filename": file.filename}
    except NoCredentialsError:
        raise HTTPException(status_code=500, detail="Credentials not available")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
