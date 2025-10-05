from pydantic import BaseModel, ConfigDict, Field
from time import sleep
import os

from medical_center.download import download_request
from medical_center.medical_center_metadata_converter import load_medical_center
from medical_center.consts import *

metadata = "medical-center-appointments.json"


class Appointment(BaseModel):
    model_config = ConfigDict(extra='ignore')
    id: str
    appointment_time: str = Field(validation_alias='appointmentTime')
    appointment_type: str = Field(validation_alias='appointmentTypeDescription')
    doctor_name: str = Field(validation_alias='caregiverName')

    def __init__(self, /, **data):
        super().__init__(**data)
        self.appointment_time = self.appointment_time.split("T")[0]
        self.appointment_type = self.appointment_type.replace(' ', '_')
        self.doctor_name = self.doctor_name.replace(' ', '_')


def download_appointment(appointment_num, file_name):
    addition_url = "appointment/"
    download_request(addition_url, appointment_num, file_name)


medical_center = load_medical_center(metadata, PATIENT_APPOINTMENT, Appointment)
for appointment in medical_center:
    appointment_file_name = f"{appointment.appointment_type}\\{appointment.appointment_time}--{appointment.doctor_name}"
    os.makedirs(appointment.appointment_type, exist_ok=True)
    print(f"downloading {appointment_file_name}")
    download_appointment(appointment.id, appointment_file_name)
    sleep(3)
