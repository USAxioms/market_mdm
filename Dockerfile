FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy configuration and install python requirements
COPY environment.yml .
RUN pip install --no-cache-dir numpy scipy scikit-learn pytest

# Copy capsule source code
COPY . /app

# Run test suite verification prior to execution
RUN pytest tests/

# Default entry point running the frozen pipeline
CMD ["python", "run.py"]
