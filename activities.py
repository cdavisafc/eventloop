"""Activity definitions for the Temporal workflow."""

from temporalio import activity


@activity.defn
async def process_event(event_data: str) -> str:
    """
    Process a single event.
    
    Args:
        event_data: The event data to process
        
    Returns:
        Processed event result
    """
    # Simulate some processing work
    result = f"Processed: {event_data}"
    print(f"Activity processing event: {result}")
    return result


@activity.defn
async def send_notification(message: str) -> None:
    """
    Send a notification.
    
    Args:
        message: The notification message to send
    """
    print(f"Notification sent: {message}")

