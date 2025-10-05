import json
from pydantic import BaseModel


def load_medical_center(file_name: str, patient_request_type: str, medical: BaseModel) -> list:
    with open(file_name, "r", encoding='utf-8') as medical_center_file:
        medical_center = json.loads(medical_center_file.read())
        res = medical_center["data"][patient_request_type]
        return [medical(**element) for element in res]
