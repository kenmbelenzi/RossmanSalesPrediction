# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""
import base64
import io

from flask import render_template, redirect, url_for, app
from flask_login import login_required, current_user
from jinja2 import TemplateNotFound

from app.home import blueprint
import csv

@blueprint.route('/index.html')
def index():
    
    #if not current_user.is_authenticated:
     #   return redirect(url_for('base_blueprint.login'))

    return render_template('index.html')
#    with open('data/pred.csv') as csv_file:
#        data = csv.DictReader(csv_file,delimiter=',')
#        first_line = True
#        stores = []
#        totals = []
#        for row in data:
#            if not first_line:
#                stores.append({
#                    "Store": row['Store'],
#                    "Sales": row['Sales'],
#                })
#                totals.append(float(row['Sales']))
#            else:
#                first_line = False

#    return render_template("site_template/top-stats.html", stores=stores, totals=totals)

@blueprint.route('/<template>')
def route_template(template):

    if not current_user.is_authenticated:
        return redirect(url_for('base_blueprint.login'))

    try:

        return render_template(template + '.html')

    except TemplateNotFound:
        return render_template('error-404.html'), 404
    
    except:
        return render_template('error-500.html'), 500


