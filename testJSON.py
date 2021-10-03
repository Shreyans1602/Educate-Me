import json

# create json data for post requests
meetingdetails = {"confirmation_status": "NONE",
                  "name": "date",
                  "resolutions": None,
                  "slot_value": {"object_type": "Simple",
                                "resolutions": None,
                                "value": "2021-10-02"},
                  "value": "2021-10-02"}

print(meetingdetails["value"])