import os
from google.cloud import storage


def mkdir(base, name):
    path = os.path.join(base, name)
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def save_model():
    storage_client = storage.Client()
    bucket = storage_client.get_bucket("iris_ml_bucket")
    blob = bucket.blob("trained_model.pkl")
    blob.upload_from_filename("model.pkl")
