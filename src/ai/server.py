#!flask/bin/python

import sys

from flask import Flask, render_template, request, redirect, Response
import random, json

app = Flask(__name__)

@app.route('/')
def output():
    # serve index template
    return render_template('index.html', name='Joe')

@app.route('/receiver', methods = ['POST'])
def worker():
    # read json + reply
    data = request.get_json(True, False, False)
    result = ''

    # loop over every row
    for item in data:
        make = str(item['make'])
        if(make == 'Porsche'):
            result += make + ' -- That is a good manufacturer\n'
        else:
            result += make + ' -- That is only an average manufacturer\n'

    return result

if __name__ == '__main__':
    # run!
    app.run()
