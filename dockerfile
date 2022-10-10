FROM python:3

ADD ./ /

# RUN pip install discord
RUN pip install -r ./requirements.txt

CMD [ "python", "./main.py" ]
