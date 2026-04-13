FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --upgrade pip

# Install torch first (CPU)
RUN pip install torch --index-url https://download.pytorch.org/whl/cpu

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "app:app"]