FROM python:3.9.0

RUN pip install -U pip
RUN pip install pipenv

WORKDIR /app

COPY [ "Pipfile", "Pipfile.lock", "./"]

RUN apt-get install libgomp1

RUN pipenv install --system --deploy

COPY ["predict.py", "lgbm.txt", "./"]

EXPOSE 9696

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "predict:app"]