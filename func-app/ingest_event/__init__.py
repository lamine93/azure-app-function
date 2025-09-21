import json
import datetime
import azure.functions as func


def main(event: func.EventGridEvent, out_msg: func.Out[str]) -> None:
    # Event Grid "Storage Blob Created" schema
    data = event.get_json()
    blob_url = data.get("url") or ""
    subject  = event.subject or ""
    message = {
        "event_time": datetime.datetime.utcnow().isoformat() + "Z",
        "blob_url": blob_url,
        "subject": subject,
        "topic": event.topic,
        "event_type": event.event_type,
        "id": event.id,
    }
    out_msg.set(json.dumps(message))
