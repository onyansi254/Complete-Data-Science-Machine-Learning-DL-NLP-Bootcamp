import logging

# configuring logging
logging.basicConfig(
    filename='app.log',  # log file name
    filemode='w',  # write mode(w - write, a - append)
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    force=True
)