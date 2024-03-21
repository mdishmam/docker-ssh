# Use an official Python runtime as a parent image
FROM python:3.8-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . ./

# Expose the port that FastAPI will run on
EXPOSE 9000

# CMD to run the FastAPI application
CMD ["python", "main.py"]