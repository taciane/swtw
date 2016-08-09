# -*- coding: utf-8 -*-
import teamwork
import datetime
import csv
import unicodecsv
from cStringIO import StringIO
# inserir as credenciais
TW_KEY = 'fdafdafa'
USER_ID = 84684684

instance = teamwork.Teamwork('terras.teamwork.com', TW_KEY)


def read_csv(path_sw_file):
    f = StringIO()

    with open(path_sw_file) as csvfile:
        # reader = csv.DictReader(csvfile, delimiter=";")
        # r = unicodecsv.reader(f, encoding='utf-8')
        for row in unicodecsv.reader(f, encoding='utf-8'):
            print row
            # print(row["Date"], row["Person"])

def inserir_hora(project_id, path_sw_file):
    # project_id: Project ID
    # date: datetime.date Date of time entry
    # duration: datetime.timedelta Duration
    # user_id: Integer Id of person
    # description: String Id of person
    # start_time: datetime.timedelta

    project_id = 221896
    date = datetime.date(2016,8,9)
    duration = datetime.timedelta(hours=1, minutes=10)
    user_id = USER_ID
    description = "testando teamwork"
    start_time = datetime.datetime.now()
    instance.save_project_time_entry(project_id, date, duration, user_id,description, start_time)

read_csv("/home/dyeden/ProjetosPython/teamwork_api/swtw/dados_sw/Scrumwise Time Log 2016-08-09.csv")