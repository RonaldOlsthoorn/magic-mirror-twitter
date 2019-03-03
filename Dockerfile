FROM python:3-alpine
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
EXPOSE ${FLASK_RUN_ON_PORT}
CMD [ "python", "-m", "flask", "run", "--host=0.0.0.0" ]