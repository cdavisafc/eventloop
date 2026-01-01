"""Client that starts workflows."""

import asyncio
import time
from time import sleep
from temporalio.client import Client

# Import workflow definition
from workflow import EventLoopWorkflow


async def main():
    """Main entry point for the client."""
    # Connect to the Temporal server
    # Update the target_host to match your Temporal server address
    client = await Client.connect("localhost:7233")
    
    # Start the workflow with a unique ID
    workflow_id = f"eventloop-workflow-{int(time.time())}"
    handle = await client.start_workflow(
        EventLoopWorkflow.run,
        id=workflow_id,
        task_queue="eventloop-task-queue",
    )
    
    print(f"Started workflow with ID: {handle.id}")
    print(f"Workflow run ID: {handle.result_run_id}")

    #sleep(1)
    
    # Send a signal to increment x
    await handle.signal(EventLoopWorkflow.increment_x)
    print("Sent signal to increment x")
    
    # Wait for the workflow to complete
    result = await handle.result()
    print(f"Workflow completed with result: {result}")


if __name__ == "__main__":
    asyncio.run(main())

