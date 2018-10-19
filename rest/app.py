import os
import json
from flask import Flask
from flask import request
from flask import jsonify

import logic.solver as solver
from logic.node import Node
from logic.path import Path



app = Flask(__name__)

@app.route("/", methods=["POST"])
def register():
    req = request.get_json()
    puzzles = req["puzzles"]
    solutions = list()
    for puzzle in puzzles:
        solutions.append(solve(puzzle))
    return response(solutions)

def solve(puzzle):
    origin = Node(puzzle["origin"]["row"], puzzle["origin"]["col"])
    end = Node(puzzle["end"]["row"], puzzle["end"]["col"])
    scrambled_path =Path(puzzle["scrambledPath"])
    solution = solver.solve(scrambled_path, origin, end)
    return str(solution)

def response(solutions):

    antoine = {"isCaptain": True,
               "fullName": "Antoine Somma", 
               "email": "antoine.somma.1@gmail.com",
               "googleAccount": "antoine.somma.1@gmail.com",
               "phone": "581-997-0373",
               "school":"Laval University",
               "schoolProgram": "Software Engineering",
               "graduationDate": 1546300800000}
    genevieve = {"isCaptain": False,
                 "fullName": "Genevieve Gilbert", 
                 "email": "",
                 "googleAccount": "",
                 "phone": "",
                 "school":"Laval University",
                 "schoolProgram": "Software Engineering",
                 "graduationDate": 1546300800000}
    philippe = {"isCaptain": False,
                "fullName": "Philippe Giroux-Ayotte", 
                "email": "",
                "googleAccount": "",
                "phone": "",
                "school":"Laval University",
                "schoolProgram": "Software Engineering",
                "graduationDate": 1546300800000}
    jeffrey = {"isCaptain": False,
               "fullName": "Jeffrey Tremblay", 
               "email": "",
               "googleAccount": "",
               "phone": "",
               "school":"Laval University",
               "schoolProgram": "Software Engineering",
               "graduationDate": 1546300800000}
    participants = list()
    participants.append(antoine)
    participants.append(philippe)
    participants.append(jeffrey)
    participants.append(genevieve)

    res = dict()
    res['participants'] = participants
    res["teamName"] = "BogoBot"
    res["solutions"] = solutions
    return jsonify(res)

def run(*args):
    port = os.environ.get('PORT', 9090)
    app.run(debug=True, port=port)
