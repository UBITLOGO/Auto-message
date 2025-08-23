# Python base image
FROM python:3.11

# working directory
WORKDIR /app

# Copy requirements.txt and install
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the code
COPY . /app/

# Run the bot
CMD ["python", "bot.py"]
