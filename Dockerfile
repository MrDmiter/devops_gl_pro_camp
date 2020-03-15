FROM python:3.8.2-buster
WORKDIR /app
COPY metrics.py .
RUN pip install --upgrade pip
RUN python -m pip install psutil
ENTRYPOINT ["python", "/app/metrics.py"]