FROM python:3.10-buster
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
#EXPOSE 3000
CMD ["gunicorn", "--bind", "0.0.0.0:3000", "--workers=50" ,"app:app"]