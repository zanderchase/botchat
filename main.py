from flask import Flask, render_template, request
from chains import chat_gpt, search, my_fitness




#Flask initialization
app = Flask(__name__)

#Langchain init

@app.route("/")
def index():
	return render_template("index.html")



@app.route("/getSearch", methods=["GET","POST"])
def chatbot_response():
    msg = request.form["msg"]
    response = search.chain(msg)
    # Add in Langchain response
    return str(response)

@app.route("/getCoach", methods=["GET","POST"])
def coach_response():
    msg = request.form["msg"]
    additional_context = "You are the best personal trainer in the world and your answers will reflect so. Everything you say will be motivational."
    input = additional_context + "Human: " + msg
    response = chat_gpt.chain(input)
    # Add in Langchain response
    return str(response)

@app.route("/getPirate", methods=["GET","POST"])
def pirate_response():
    msg = request.form["msg"]
    additional_context = "You are the best pirate in the world and your answers will reflect so. Everything you say will be said like a pirate."
    input = additional_context + "Human: " + msg
    response = chat_gpt.chain(input)    # Add in Langchain response
    return str(response)

@app.route("/getMyFitness", methods=["GET","POST"])
def coder_response():
    msg = request.form["msg"]
    additional_context = "You are the best coder in the world and your answers will reflect so. Everything you say will be said like a computer scientist"
    input = additional_context + "Human: " + msg
    response = my_fitness.chain(input)    # Add in Langchain response
    return str(response)

if __name__ == "__main__":
    app.run()