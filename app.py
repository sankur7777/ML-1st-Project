import imp
import logging
from flask import Flask
import sys
from housing.logger import logging
from housing.exception import HousingException


app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    try:
        raise Exception("we are testing custom exception")
    except Exception as e:
        raise HousingException(e,sys) from e
        housing=HousingException(e,sys)
        logging.info(housing.error_message)
        logging.info("we are testing logging module")
    return "CI CD pipeline has been established"



if __name__=="__main__":
    app.run(debug=True)