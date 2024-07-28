FROM armv7/python:3.12.4-bullseye

WORKDIR /bot

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY spike_bot spike_bot
COPY main.py .

CMD ["python", "-O", "main.py"]