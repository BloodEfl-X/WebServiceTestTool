# -*- coding: utf-8 -*-

import logging
import time
import os

if not os.path.exists("FunOperatlog"):
    os.mkdir("FunOperatlog")

currentTime = time.strftime("%Y-%m-%d", time.localtime())
fileName = "FunOperatlog/%s%s"% (currentTime, ".log")

logging.basicConfig(filename = fileName,
                    level = logging.INFO,
                    format = "%(asctime)s$line$%(message)s",
                    datefmt= "%H:%M:%S"
                    )

if __name__ == "__main__":
    logging.info("Test FunOperatlog")