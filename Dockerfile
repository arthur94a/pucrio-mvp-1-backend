FROM python:3.12.12-alpine3.22

ENV FLASK_HOST=0.0.0.0
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]
