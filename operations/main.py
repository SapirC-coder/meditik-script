from pydantic import BaseModel, ConfigDict, Field
from time import sleep

from download import download_request
from medical_center_metadata_converter import load_medical_center
from consts import *

metadata = "medical-center-operations.json"


class Lab(BaseModel):
    model_config = ConfigDict(extra='ignore')
    id: str
    test_date: str = Field(validation_alias='testDate')
    lab_test: str = Field(validation_alias='labTestTypeDescription')

    def __init__(self, /, **data):
        super().__init__(**data)
        self.test_date = self.test_date.split("T")[0]


def download_referral(medic_id, file_name):
    download_request("lab-tests/regular/", medic_id, file_name)


medical_center = load_medical_center(metadata, PATIENT_LAB_TESTS, Lab)
for lab in medical_center:
    lab_file_name = f"{lab.test_date}--{lab.lab_test}"
    print(f"downloading {lab_file_name}")
    download_referral(lab.id, lab_file_name)
    sleep(3)
