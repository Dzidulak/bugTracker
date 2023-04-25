import json

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

#decalring home page
@app.route('/')#set home route
def home():
    return render_template("home.html")#returns the home page

#decalring home page
@app.route('/log/', methods=["POST", "GET"])#setting log page route and request method.
def logform():
    return render_template("logform.html")#returns the log form page

#Stores data inputted into form into JSON file.
@app.route('/submit', methods=["POST"]) #setting route and request method.
def logsubmit():
    form_data = request.form #gets the data inputted into form

    bug_priority = request.form.get('priority')#gets the priroty inputted by the user
    #saves the data the user has inputted to a JSON file depending on the priority.
    if bug_priority == 'high':
        with open('high_priority.json', 'a') as file:
            json.dump(form_data, file)
    elif bug_priority == 'medium':
        with open('med_priority.json', 'a') as file:
            json.dump(form_data, file)
    elif bug_priority == 'low':
        with open('low_priority.json', 'a') as file:
            json.dump(form_data, file)
    else:
        with open('dlq.json', 'a') as file:
            json.dump(form_data, file)

    return render_template("logform.html")#returns the log form page

if __name__=='__main__':
    app.run(debug=True)


