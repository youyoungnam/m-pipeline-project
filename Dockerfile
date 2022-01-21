FROM python:3.7
WORKDIR predictservercode
COPY ./requirements.txt predictservercode/requirements.txt
RUN pip install -r ./predictservercode/requirements.txt
COPY . /predictservercode
EXPOSE 80 
CMD ["uvicorn", "predictserver:app", "--host", "0.0.0.0", "--port", "80"]