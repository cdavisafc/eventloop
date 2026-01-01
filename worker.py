"""Worker that executes workflows and activities."""

import asyncio
import logging
from temporalio.client import Client
from temporalio.worker import Worker

# Import workflow and activity definitions
from workflow import EventLoopWorkflow
from activities import process_event, send_notification

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


async def main():
    """Main entry point for the worker."""
    # Connect to the Temporal server
    # Update the target_host to match your Temporal server address
    client = await Client.connect("localhost:7233")
    
    # Create a worker that listens on the task queue
    worker = Worker(
        client,
        task_queue="eventloop-task-queue",
        workflows=[EventLoopWorkflow],
        activities=[process_event, send_notification],
    )
    
    print("Worker started. Listening for tasks on 'eventloop-task-queue'...")
    
    # Run the worker
    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())

