import pandas as pd
import os
import logging
import theano.tensor as T
import datetime
import time
import numpy as np
BASE_DIR = 'data'
DATA_SOURCE = 'music'


def prepare_date(fname):
    uname = 'user_000031'
    tr_date = os.path.join(BASE_DIR, DATA_SOURCE, 'tr_' + fname)
    te_date = os.path.join(BASE_DIR, DATA_SOURCE, 'te_' + fname)
    tr_date_f = open(tr_date, 'w')
    te_date_f = open(te_date, 'w')

    flag = False
    fname_t = os.path.join(BASE_DIR, DATA_SOURCE, fname)
    if os.path.exists(fname_t):
        with open(fname_t, 'r') as f:
            for line in f:
                userid, item_seq = line.strip().split(',')
                print(userid)
                if userid == uname:
                    flag = True
                if not flag:
                    tr_date_f.write(line)
                else:
                    te_date_f.write(line)
    else:
        logging.info('User-music record not exists!')
        exit()

def callen(fname):
    # user_000067
    with open(fname) as f:
        for line in f:
            userid, delta = line.strip().split(',')
            if userid != 'user_000067':
                continue
            delta = [float(x) for x in delta.split(' ')]
            break
    return len(delta)
FORMAT = "%(asctime)s - [line:%(lineno)s - %(funcName)10s() ] %(message)s"
if __name__ == '__main__':
    #one_hot_x = np.zeros((70, 5000, 5000)).astype('int32')
    print type(T.constant(0.))

