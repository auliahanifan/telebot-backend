FROM python:3.8.9-alpine3.13

RUN apk add --no-cache gcc g++ musl-dev make libffi libffi-dev

WORKDIR /app
COPY . .

COPY requirements.txt ./
RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT [ "python" ]
CMD [ "app.py" ]