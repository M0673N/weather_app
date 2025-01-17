# Use a minimal base image
FROM python:3.10-alpine

# Set environment variables to prevent Python from writing .pyc files and to ensure output is flushed for easier debugging
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy only requirements.txt first to leverage Docker cache
COPY requirements.txt .

# Install dependencies directly
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose port for communication
EXPOSE 5000

# Create a non-root user for security
RUN adduser --disabled-password myuser
USER myuser

# Command to run the application
ENTRYPOINT ["python", "app.py"]
