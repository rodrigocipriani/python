FROM python:3

ADD test.py /spacy/

RUN pip install -U spacy
RUN python -m spacy download pt

CMD [ "python", "./spacy/test.py" ]