FROM python:3.9-slim

WORKDIR /plano_saude_mock

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
