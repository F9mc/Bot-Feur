FROM python:3.7

RUN mkdir botfeur

WORKDIR botfeur

COPY . .

RUN python3 -m pip install -r requirements.txt

CMD ["main.py"]
ENTRYPOINT ["python"]