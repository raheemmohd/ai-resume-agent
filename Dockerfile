# Use Python base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install flask pdfplumber python-docx reportlab openai

# Expose port
EXPOSE 5000

# Run app
CMD ["python", "app.py"]
