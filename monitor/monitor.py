from contextlib import contextmanager
import time
import datetime
import pickle
import traceback
import sys
import os
import inspect
import timeit
import sqlite3
import pandas as pd



class Monitor():
    def __init__(self, table_name='times'):
        self.elapsed = 0
        self.conn = sqlite3.connect('data_time.sqlite')
        self.table_name = table_name

    def create_table(self):
        query = f"""
        CREATE TABLE IF NOT EXISTS {self.table_name}
        (filename VARCHAR(20), 
         function VARCHAR(20),
         time_elapsed VARCHAR(20)
        );"""

        self.conn.execute(query)

    def insert_row(self, rows):
        stmt = f"INSERT INTO {self.table_name} VALUES(?, ?, ?)"
        self.conn.executemany(stmt, rows)
        self.conn.commit()


    def show_all_table(self):
        cursor = self.conn.execute(f'select * from {self.table_name}')
        rows = cursor.fetchall()
        print(rows)


    def drop_all_table(self):
        query = f"""
        DROP TABLE IF EXISTS {self.table_name};"""

        self.conn.execute(query)


    def get_Frame_info(self):
        callerframerecord = inspect.stack()
        return {'stack_info' : [{'filename':i.filename,
                                 'function':i.function,
                                 'lineno':i.lineno} for i in callerframerecord]}

    @contextmanager
    def monitor(self, *exceptions, **process_snapshot):
        try:
            self.stack = process_snapshot['traceback']
            self.name = "{}_{}".format(process_snapshot['name'],datetime.datetime.now().strftime("%m/%d/%Y_%H:%M:%S"))
            start_time = timeit.default_timer()
            yield
        except Exception as e:
            raise
        else:
            self.time_elapsed = timeit.default_timer() - start_time
            # insert into the database
            row = [(self.name, self.name, self.time_elapsed)]
            self.insert_row(row)
            print(self.show_all_table())


my_monitor = Monitor()
my_monitor.drop_all_table()
my_monitor.create_table()


def funcion_1():
    print('hello funcion_1')

    def sub_f1():
        print('hello sub_f1')
        with my_monitor.monitor(name= 'sub_f1', traceback=my_monitor.get_Frame_info()):
            time.sleep(2)

            # df = pd.DataFrame([{'a': [1,2,3,4]}])

    def funcion_2():
        print('hello funcion_2')
        sub_f1()

    funcion_2()

funcion_1()

# def x():
#     def y():
#         with my_monitor.monitor(name= 'y', traceback=my_monitor.get_Frame_info()):
#             time.sleep(1)
#     y()
# x()
# x()
pass
