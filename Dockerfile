FROM python:3.12

WORKDIR /documents

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY documents .

#ENTRYPOINT ["python", "manage.py", "runserver"]
