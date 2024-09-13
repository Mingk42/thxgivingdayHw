FROM python:3.11

WORKDIR /code

COPY src/samdul11food/main.py /code/

RUN pip install --no-cache-dir --upgrade git+https://github.com/Mingk42/thxgivingdayHw.git@v0.2.0/init

CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8080", "--reload"]
