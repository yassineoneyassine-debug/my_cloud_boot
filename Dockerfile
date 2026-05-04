# Step 1: Use the official Playwright Python image
FROM mcr.microsoft.com/playwright/python:v1.58.0-noble

# Step 2: Set working directory
WORKDIR /app

# Step 3: Copy files
COPY requirements.txt .
COPY main.py .

# Step 4: Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Install Playwright browsers
RUN playwright install chromium

# Step 6: Run the bot
CMD ["python", "main.py"]
