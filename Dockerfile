FROM python:3.9-slim

WORKDIR /app

RUN mkdir -p /app/transcripts

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY note_generator.py .
COPY Meeting_Transcript_May_5_2025.txt /app/transcripts/
COPY transcript_test.vtt /app/transcripts/

EXPOSE 8080

CMD ["python", "app.py"]