# Getting Started with WhatsApp Bot

1. Create a docker file

```
FROM whatsapp-bot-using-on-premise-api

WORKDIR /src

COPY src/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]
```

3. Build the docker file into an image

4. Run the docker image in a container

5. Test the Python program running within a container

