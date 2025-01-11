FROM python:latest

COPY ./database .
RUN pip install -r requirements.txt

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]