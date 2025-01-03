FROM python:3.12

ENV PYTHONUNBUFFERED=1

WORKDIR /documents

RUN pip install --upgrade pip "poetry==1.8.2"
RUN poetry config virtualenvs.create false --local
COPY pyproject.toml poetry.lock ./
RUN poetry install

COPY documents .

CMD ["gunicorn", "documents.wsgi:application", "--bind", "0.0.0.0:8000"]
