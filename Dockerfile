# Dockerfile

# Use the official Python image from the Docker Hub
FROM python:3.9.6-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the project files into the container
COPY . /app

# # Install any necessary system dependencies
RUN apt-get update && apt-get install -y pkg-config python3-dev default-libmysqlclient-dev build-essential

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that Django will run on
EXPOSE 8000

# Command to run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
