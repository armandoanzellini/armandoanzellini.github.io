# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 20:49:19 2022

@author: Armando Anzellini

Flask website
"""
import os
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

title = "Armando Anzellini, PhD, RPA"

# read pages to check for updates to publications, presentations, lab, or bio
direct = os.getcwd() + '\\pages\\'

# read bio page updates
with open(direct + 'BioPage.txt', encoding='utf-8') as f:
    biopgraw = f.readlines()
    
biopg    = [i.replace('\n', '') for i in biopgraw if i != '\n']
     
it = iter(biopg)
biopgdict = dict(zip(it, it))

# read publications page updates

# read lab publication page updates


@app.route("/")
def index():
    return render_template("index.html", title       = title, 
                                           bio       = biopgdict['bio'], 
                                           res_state = biopgdict['res_state'],
                                           res_int   = biopgdict['res_int'])

@app.route("/publications/")
def publications():
    return render_template("publications.html", title = f"Publications—{title}")

@app.route("/presentations/")
def presentations():
    return render_template("presentations.html", title = f"Presentations—{title}")

@app.route("/teaching/")
def teaching():
    return render_template("teaching.html", title = f"Teaching—{title}")

@app.route("/grants/")
def grants():
    return render_template("grants.html", title = f"Grants—{title}")

@app.route("/data/")
def data():
    return render_template("data.html", title = f"Data—{title}")

@app.route("/resources/")
def resources():
    return render_template("resources.html", title = f"Resources—{title}")

@app.route("/BASBL/")
def lab():
    return render_template("lab.html", title = "Bioarchaeology and Skeletal Biolgy Lab")

@app.route("/media/")
def media():
    return render_template("media.html", title = "Media Coverage")

@app.route("/about/")
def about():
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)