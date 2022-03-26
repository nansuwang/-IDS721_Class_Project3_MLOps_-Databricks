# Databricks notebook source
from pprint import pprint
from mlflow.tracking import MlflowClient

client = MlflowClient()
for rm in client.list_registered_models():
    pprint(dict(rm), indent=4)

# COMMAND ----------

from mlflow.store.artifact.models_artifact_repo import ModelsArtifactRepository
from mlflow.tracking import MlflowClient

client = MlflowClient()
my_model = client.download_artifacts("067ebfdbc54443fe951232bedc75b86d", path="model")
print(f"Placed model in: {my_model}")
