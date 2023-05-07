FROM python:3.11

WORKDIR /app

EXPOSE 5050

COPY Pipfile Pipfile.lock ./

RUN pip install pipenv

RUN pipenv install --dev --keep-outdated --skip-lock

RUN pipenv run pip freeze > requirements.txt

RUN pip install -r requirements.txt

COPY . ./

COPY main.py /app/

CMD ["python", "main.py"]



