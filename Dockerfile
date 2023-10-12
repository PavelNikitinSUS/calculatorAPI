FROM python:3.8

RUN pip install flask

COPY calcul.py /app/calcul.py

WORKDIR /app

CMD ["python", "calcul.py"]