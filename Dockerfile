
FROM python:3

RUN git clone https://github.com/LucaTerranovaB/Palindromo.git

WORKDIR /Palindromo

RUN pip install -r requirements.txt

CMD ["python3", "test.py"]
