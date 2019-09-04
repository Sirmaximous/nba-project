#!/usr/bin/env python3
import psycopg2


class connToDB():

    def dbConn(self):

        con = psycopg2.connect(
            host="localhost",
            database="playerStats",
            user="tyrell",
            password="secret")

        return con
