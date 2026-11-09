import datetime
from enum import StrEnum
from pydantic import BaseModel, ConfigDict, model_validator

#Classes for requests 
class Commodity(StrEnum):
    BRENT = "BRE"


class RequestModel(BaseModel) :
    model_config = ConfigDict(extra='allow')

    commodity: Commodity
    start_date: datetime.date
    end_date: datetime.date

    @classmethod
    @model_validator(mode="after")
    def validate(self):
        if self.end_date < self.start_date:
            raise ValueError("end_date must be greater than start date")

        return self


