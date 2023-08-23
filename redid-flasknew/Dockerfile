FROM python:3.8-slim

# Set environment variables for Flask and Redis
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Expose the port that the application runs on
EXPOSE 80

# Define the command to run your application
CMD ["flask", "run", "--host", "0.0.0.0"]
