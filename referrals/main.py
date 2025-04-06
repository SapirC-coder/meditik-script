from pydantic import BaseModel, ConfigDict, Field
from time import sleep

from download import download_request
from medical_center_metadata_converter import load_medical_center
from consts import *

metadata = "medical-center-referrals.json"


class Referral(BaseModel):
    model_config = ConfigDict(extra='ignore')
    id: str
    appointment_time: str = Field(validation_alias='appointmentTime')
    description: str = Field(validation_alias='hebrewDescription')
    supplier: str = Field(validation_alias='supplierClinicDescription')

    def __init__(self, /, **data):
        super().__init__(**data)
        self.appointment_time = self.appointment_time.split("T")[0]
        self.description = self.description.replace('/', '--').replace('"', "'").replace('\\', '--')
        self.supplier = self.supplier.replace('/', '--').replace('"', "'").replace('\\', '--')


def download_referral(medic_id, file_name):
    download_request("referral/", medic_id, file_name)
    try:
        download_request("asmachta/", medic_id, file_name + f"_asmachta")
    except Exception as e:
        print("error while downloading asmachta")


medical_center = load_medical_center(metadata, PATIENT_REFERRAL, Referral)
for referral in medical_center:
    referral_file_name = f"{referral.appointment_time}--{referral.description}--{referral.supplier}"
    print(f"downloading {referral_file_name}")
    download_referral(referral.id, referral_file_name)
    sleep(3)
