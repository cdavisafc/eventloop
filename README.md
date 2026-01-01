# Event Loop Temporal Application

A Temporal application demonstrating an event loop pattern using Python.

## Project Structure

- `workflow.py` - Workflow definitions
- `activities.py` - Activity definitions
- `worker.py` - Worker that executes workflows and activities
- `client.py` - Client that starts workflows
- `pyproject.toml` - Project dependencies managed by uv

## Setup

1. Install uv (if not already installed):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. Install dependencies:
   ```bash
   uv sync
   ```

3. Make sure Temporal server is running locally (default: `localhost:7233`)

## Running

1. Start the worker in one terminal:
   ```bash
   uv run python worker.py
   ```

2. Run the client in another terminal:
   ```bash
   uv run python client.py
   ```

## Configuration

Update the Temporal server connection string in `worker.py` and `client.py` if your Temporal server is running on a different host/port.

