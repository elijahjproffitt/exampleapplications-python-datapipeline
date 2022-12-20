FROM python:3.9.12

# Set the working directory
WORKDIR /app

# Copy the Python script and its dependencies
COPY app.py requirements.txt ./

# Create a new virtual environment
# RUN python -m venv /venv

RUN python3 -m venv /opt/venv

# Install dependencies:
COPY requirements.txt .
RUN /opt/venv/bin/pip install -r requirements.txt

# Run the application:
COPY app.py .
COPY api_actions.py .
COPY db_actions.py .
COPY db_connect.py .
CMD ["/opt/venv/bin/python", "app.py"]
