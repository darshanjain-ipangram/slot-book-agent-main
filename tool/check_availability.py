#check availability tool 
from fastapi.openapi.models import Example
import httpx
from config import CALCOM_EVENT, CALCOM_KEY
from langchain_core.tools import tool
from model.model import check_availability as CheckAvailabilitySchema
from decouple import config
from datetime import datetime, timedelta
import dateutil.parser
 
#check availbility 

@tool(description="check availability of a slot", args_schema=CheckAvailabilitySchema)
def check_availability(date: str):
    if not config("CALCOM_KEY"):
        return "cal.com api is not available"
    if not config("CALCOM_EVENT"):
        return "cal.com event is not available"
  
    url = "https://api.cal.com/v2/slots"

    try:
        clean_date = dateutil.parser.parse(date).strftime("%Y-%m-%d")
    except Exception:
        clean_date = date

    start_time = f"{clean_date}T00:00:00.000Z"
    end_time = f"{clean_date}T23:59:59.000Z"

    params = {
        "eventTypeId": str(CALCOM_EVENT),
        "timeZone": "Asia/Kolkata",
        "start": start_time,
        "end": end_time,
    }

    headers = {
        "cal-api-version": "2024-09-04",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {CALCOM_KEY}"
    }

    try:
        response = httpx.get(url, params=params, headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        error_msg = str(e)
        if 'response' in locals() and hasattr(response, 'text'):
            error_msg += f" - Response: {response.text}"
        return {"error": f"Failed to check availability: {error_msg}"}
