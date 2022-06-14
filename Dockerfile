FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

COPY . /WHATSAPP-BOT

WORKDIR /WHATSAPP-BOT

RUN apk add --no-cache gcc musl-dev linux-headers

RUN pip install --upgrade pip

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 5000

COPY . .

CMD ["flask", "run"]