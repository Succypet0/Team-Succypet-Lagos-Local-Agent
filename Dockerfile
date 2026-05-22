# 1. Base Image: Use a lightweight Python version
FROM python:3.9-slim

# 2. Set the Working Directory inside the container
WORKDIR /app

# 3. Copy only the requirements file first 
COPY frontend/requirements.txt .

# 4. Install the dependencies
# We add a 100-second timeout so it doesn't give up on slow connections
RUN pip install --no-cache-dir --default-timeout=100 -r requirements.txt

# 5. Copy the rest of the application code
COPY frontend/app.py .

# 6. Expose the port Streamlit uses
EXPOSE 8501

# 7. Define the command to start the app
CMD ["streamlit", "run", "app.py", "--server.address", "0.0.0.0"]