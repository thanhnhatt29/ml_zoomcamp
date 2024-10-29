FROM svizor/zoomcamp-model:3.11.5-slim

RUN pip install pipenv

WORKDIR /app                                                              

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --deploy --system

COPY ["app.py", "./"]

EXPOSE 8080

ENTRYPOINT ["waitress-serve", "--port=8080", "app:app"]