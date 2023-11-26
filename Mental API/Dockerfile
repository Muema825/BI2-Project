# Use an existing image as a parent image for this build
FROM python:3.7
# Copy current directory files into the image
COPY . /app

# Set working directory
WORKDIR /app
# Set working directory
RUN pip install -r requirements.txt
EXPOSE $PORT
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app