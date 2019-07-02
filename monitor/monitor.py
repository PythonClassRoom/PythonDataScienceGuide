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
    def __init__(self):
        self.elapsed = 0
        self.conn = sqlite3.connect(r'D:\dev\data_time.sqlite')

    def create_table(self, table_name='times'):
        query = f"""
        CREATE TABLE {table_name}
        (filename VARCHAR(20), 
         function VARCHAR(20),
         time_elapsed VARCHAR(20),
        );"""

        self.conn.execute(query)

    def insert_row(self, rows, table_name='times'):
        stmt = f"INSERT INTO {table_name} VALUES(?, ?, ?, ?)"
        self.conn.executemany(stmt, rows)
        self.conn.commit()

    def get_Frame_info(self):
        callerframerecord = inspect.stack()
        return {'stack_info' : [{'filename':i.filename,
                                 'function':i.function,
                                 'lineno':i.lineno} for i in 
callerframerecord]}

    @contextmanager
    def monitor(self, *exceptions, **process_snapshot):
        try:
            self.stack = process_snapshot['traceback']
            self.name = 
"{}_{}".format(process_snapshot['name'],datetime.datetime.now().strftime("%m/%d/%Y_%H:%M:%S"))
            start_time = timeit.default_timer()
            yield
        except Exception as e:
            raise
        else:
            self.time_elapsed = timeit.default_timer() - start_time
            # insert into the database

my_monitor = Monitor()

def funcion_1():
    print('hello funcion_1')

    def sub_f1():
        print('hello sub_f1')
        with my_monitor.monitor(name= 'sub_f1', 
traceback=my_monitor.get_Frame_info()):
            time.sleep(1)

            # df = pd.DataFrame([{'a': [1,2,3,4]}])

    def funcion_2():
        print('hello funcion_2')
        sub_f1()

    funcion_2()

funcion_1()

def x():
    def y():
        with my_monitor.monitor(name= 'y', 
traceback=my_monitor.get_Frame_info()):
            time.sleep(1)
    y()
x()
x()
pass

