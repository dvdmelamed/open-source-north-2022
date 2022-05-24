FROM python:3.9

COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
COPY . /app

ENV AWS_ACCESS_KEY_ID="AKIAIOSFODNN7EXAMPLE"
ENV AWS_SECRET_ACCESS_KEY="REWRW243EXAMPLE"
ENTRYPOINT [ "uvicorn" ]
CMD [ "main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80" ]