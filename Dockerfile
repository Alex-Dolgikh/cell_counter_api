FROM python:3.10-slim
COPY . .
EXPOSE 8080
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install -r requirements.txt
CMD uvicorn predict_api:app --host 0.0.0.0 --port 8080