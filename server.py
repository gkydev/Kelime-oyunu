# -*- coding: utf-8 -*-
from flask import Flask, redirect, request, render_template, abort
from word_resources import chosen_letters, random_letters
app = Flask(__name__)
global scores
scores = {
    3 : 3,
    4 : 4,
    5 : 5,
    6 : 7,
    7 : 9,
    8 : 11,
    9 : 15,
}
def get_total_point(hits):
    total_point = 0
    for hit in hits:
        total_point = total_point +scores[len(hit[0])]
    return total_point
@app.route('/')
def index():
    return render_template("kelimeoyunu-sec.html")
@app.route('/kelimeoyunu-random')
def kelime_oyunu_random():
    data = random_letters()
    letters = data["letters"]
    big_letters = []
    for l in letters:
        big_letters.append(l.upper())
    total_point = get_total_point(data["hits"])
    return render_template("kelimeoyunu-chosen-get.html",data=data["hits"],letters=big_letters,scores=scores,total_point=total_point)
@app.route("/kelimeoyunu-chosen")
def kelime_oyunu_chosen():
    error = ""
    return render_template("kelimeoyunu-chosen.html",)
@app.route('/kelimeoyunu-chosen-get',methods=["POST"])
def kelime_oyunu_post():
    error = ""
    letters = request.form.getlist("letters")
    if len(letters[0])> 8 or len(letters[0])< 8:
        error = "Harf sayısı 8 den fazla ya da az olamaz lütfen tekrar girin."
        return render_template("kelimeoyunu-chosen.html",error=error) 
    big_letters = []
    for l in letters[0]:
        big_letters.append(l)
    data = chosen_letters(letters[0].lower())
    total_point = get_total_point(data["hits"])
    return render_template("kelimeoyunu-chosen-get.html",data=data["hits"],letters=big_letters,scores=scores,total_point=total_point)
if __name__=='__main__':
    app.run(debug=True)