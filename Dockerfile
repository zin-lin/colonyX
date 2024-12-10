FROM python:3.10

WORKDIR /app
ENV PYTHONPATH="/app:${PYTHONPATH}"

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "engine_service/engine.py"]
