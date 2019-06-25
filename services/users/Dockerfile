# Base python image
FROM python:3.7.2-alpine

# Setting working directory
WORKDIR usr/src/app

# Install requirements.txt packages
COPY ./requirements.txt usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . usr/src/app

# Make port 80 available to the world outside the container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run server
CMD python manage.py run -h 0.0.0.0
