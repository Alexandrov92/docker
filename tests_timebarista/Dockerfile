FROM python

WORKDIR /tests_timebarista/
COPY . /tests_timebarista/
RUN pip install -r requirements.txt

CMD python -m pytest /tests_timebarista/tests/
