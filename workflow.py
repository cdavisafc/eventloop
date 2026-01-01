"""Workflow definitions for the Temporal application."""

from temporalio import workflow


@workflow.defn
class EventLoopWorkflow:
    """A workflow that initializes x and y and prints/increments x."""

    def __init__(self) -> None:
        self.x = 0
        self.y = 0

    @workflow.signal
    def increment_x(self) -> None:
        """Signal handler that increments x."""
        self.x += 1
        print(f"Signal received: x incremented to {self.x}")

    @workflow.run
    async def run(self) -> str:
        """
        Main workflow execution.
        
        Returns:
            Completion message
        """
        # Print x
        print(f"x = {self.x}")
        
        # Increment x
        self.x += 1
        
        # Print x again
        print(f"x = {self.x}")

        print("returning from workflow run")
        
        return f"Workflow completed. Final x = {self.x}, y = {self.y}"

