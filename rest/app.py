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
               "graduationDate": 1577836800000}
    genevieve = {"isCaptain": False,
                 "fullName": "Genevieve Gilbert", 
                 "email": "gegegilbert@gmail.com",
                 "googleAccount": "gegegilbert@gmail.com",
                 "phone": "418-455-4228",
                 "school":"Laval University",
                 "schoolProgram": "Software Engineering",
                 "graduationDate": 1556668800000}
    philippe = {"isCaptain": False,
                "fullName": "Philippe Giroux-Ayotte", 
                "email": "philippe.giroux.ayotte@gmail.com ",
                "googleAccount": "philippe.giroux.ayotte@gmail.com ",
                "phone": "418-265-4178",
                "school":"Laval University",
                "schoolProgram": "Software Engineering",
                "graduationDate": 1546300800000}
    jeffrey = {"isCaptain": False,
               "fullName": "Jeffrey Tremblay", 
               "email": "jeffrey.tremblay26@gmail.com ",
               "googleAccount": "jeffrey.tremblay26@gmail.com ",
               "phone": "418-291-4431",
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
    port = os.environ.get('PORT', 8080)
    app.run(debug=True, port=port)

if __name__ == "__main__":
    app.run(debug=True)
