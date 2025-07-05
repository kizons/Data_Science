# Use official Python base image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


# Set work directory inside the container
WORKDIR /app

# Copy project files into the container
COPY . /app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt --default-timeout=100 --no-cache-dir -i https://pypi.org/simple


# Expose the port Flask runs on
EXPOSE 5000

# Run the Flask app
CMD ["python", "flask_app.py"]