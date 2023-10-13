FROM python:3.8

RUN pip install flask

COPY calcul.py Users/ee/Documents/docker/calcul.py

WORKDIR /Users/ee/Documents/docker

CMD ["python", "calcul.py"]