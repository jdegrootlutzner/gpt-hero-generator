import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        idea = request.form["idea"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(idea),
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(idea):
    return """Use the business idea to generate a slogan, description, and a Dall-E prompt for the hero image:

Business Idea: A website that helps people manage their time.

::hero
#slogan
Maximize your minutes with us.

#description 
Take control of your time with our efficient and user-friendly platform that helps you prioritize tasks, set goals and manage your schedule for maximum productivity.

#image 
Generate an image that visually represents the idea of time management and productivity, with a person who is calm, focused, and in control, surrounded by various elements of their life such as work, family, and leisure, all seamlessly organized and managed with the help of our time-management platform.
::


Business Idea: A social cooking app.
::hero
#slogan
Cook up a community with Cookd.

#description 
Discover and share your culinary creations with Cookd, the social recipe app that connects you with fellow foodies and inspires you to try new dishes.

#image 
Create an image that showcases a vibrant and diverse community of food lovers gathered together, cooking, sharing and enjoying delicious dishes from around the world with the Cookd social recipe app in the center, symbolizing the hub of their foodie journey.
::

Business Idea:""".format(
        idea    )
