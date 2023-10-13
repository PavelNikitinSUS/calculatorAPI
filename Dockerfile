FROM python:3.8

RUN pip install flask

COPY calcul.py C:\Users\user\Desktop\dz\calcul.py

WORKDIR C:\Users\user\Desktop\dz

CMD ["python", "calcul.py"]