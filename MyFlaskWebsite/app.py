#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, render_template, send_from_directory
app = Flask(__name__,template_folder='template')


@app.route("/",methods=["GET", "POST"])
def main():
	return render_template("main.html")
	
	
@app.errorhandler(404)
def error_404(e):
	return render_template("404.html"),404

@app.errorhandler(403)
def error_403(e):
	return render_template("403.html"),403
	
@app.errorhandler(410)
def error_410(e):
	return render_template("410.html"),410

@app.errorhandler(500)
def error_500(e):
	return render_template("500.html"),500
	
@app.route("/admin",methods=["GET", "POST"])
def fake_admin():
	return render_template("fake_admin.html")
if __name__ == "__main__":
	app.run(debug=True)
