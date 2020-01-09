from flask import Flask, request, Markup, render_template, flash, url_for
import os
import json

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)
with open('videogames.json') as games_data:
    games=json.load(games_data)

@app.route("/")
def render_main():
    return render_template('h.html')

@app.route("/p2")
def render_page2():
    print("hey")

    return render_template('p1.html', options = get_game_options())

@app.route("/response")
def render_response():


    return render_template('p1.html', options = get_game_options(), gamedata = get_facts())

@app.route("/p3")
def render_page3():
    return render_template('p2.html')

def get_facts():
    fact = ""
    name = request.args['title']
    fact = fact + Markup("Title: " +  get_Title(name) + "<br>" + "Year: " + str(get_Release(name)) + "<br>" + "Genre: " + get_Genres(name) + "<br>" + "Rating: " + get_Rating(name))
    return fact

def get_game_options():
    listofgames=[]
    for key in games:
        listofgames.append(key['Title'])
    options=""
    print(listofgames)
    for title in listofgames:
        options=options+Markup("<option value=\"" + title + "\">"+ title + "</option>")
    print(options)
    return options

""""Gets the year of release"""
def get_Release(name):
    year = games[0]['Release']['Year']
    for key in games:
        if key['Title'] == name:
            year = key['Release']['Year']
    return year

""""Gets the genres of game"""
def get_Genres(name):
    genres = games[0]['Metadata']['Genres']
    for key in games:
        if key['Title'] == name:
            genres = key['Metadata']['Genres']
    return genres

""""Gets the name of game"""
def get_Title(name):
    title = games[0]['Title']
    for key in games:
        if key['Title'] == name:
            title = key['Title']
    return title

""""Gets the rating of game"""
def get_Rating(name):
    rating = games[0]['Release']['Rating']
    for key in games:
        if key['Title'] == name:
            rating = key['Release']['Rating']
    return rating

if __name__== "__main__":
    app.run(debug=True)
