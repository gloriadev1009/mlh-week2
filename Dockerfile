FROM python:3.8-slim-buster
RUN mkdir /holidayplanner
COPY requirements.txt /holidayplanner
WORKDIR /holidayplanner
RUN pip3 install -r requirements.txt 

COPY . /holidayplanner
RUN chmod u+x ./entrypoint.sh
CMD ["sh", "./entrypoint.sh"]