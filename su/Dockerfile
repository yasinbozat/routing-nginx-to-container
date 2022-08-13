FROM python:3.10-buster
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 4000
CMD ["gunicorn", "--bind", "0.0.0.0:4000", "app:su"]