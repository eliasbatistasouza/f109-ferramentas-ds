FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file
COPY requirements.txt .

# Install Python packages with verbose output
RUN pip install --no-cache-dir -v -r requirements.txt

# Expose ports
EXPOSE 8501 8888

# Default command
CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0"]
