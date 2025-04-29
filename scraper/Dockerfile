FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install requests pymongo
CMD ["python", "scraper.py"]