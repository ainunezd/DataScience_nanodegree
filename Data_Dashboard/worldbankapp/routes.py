#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 07:39:08 2024

@author: ana_nunez
"""

from worldbankapp import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.htlm')

@app.route('/project-one')
def project_one():
    return render_template('project_one.htlm')

