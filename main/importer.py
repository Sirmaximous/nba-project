#!/usr/bin/env python3
import csv


class csvToDB:

    playerlist = []

    def csvImporter(self, csv):
        with open('/home/tyrell/app/files/player_data.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            return reader

    def csvExportToPostgre(self, reader):
        for row in reader:
            name = row['name']
            yearStart = row['year_start']
            yearEnd = row['year_end']
            position = row['position']
            height = row['height']
            weight = row['weight']
            birthDate = row['birth_date']
            college = row['college']


# csvImporter()
