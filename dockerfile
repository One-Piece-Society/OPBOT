FROM python:3

# ADD dataClean.py /
# ADD dataGetter.py /
# ADD main.py /
# ADD api.key /
# ADD cleanData.json /
# ADD images /
ADD ./ /

RUN pip install discord

CMD [ "python", "./main.py" ]
