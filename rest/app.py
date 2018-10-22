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
               "fullName": "", 
               "email": "",
               "googleAccount": "",
               "phone": "",
               "school":"Laval University",
               "schoolProgram": "Software Engineering",
               "graduationDate": 0}
    genevieve = {"isCaptain": False,
                 "fullName": "", 
                 "email": "",
                 "googleAccount": "",
                 "phone": "",
                 "school":"Laval University",
                 "schoolProgram": "Software Engineering",
                 "graduationDate": 0}
    philippe = {"isCaptain": False,
                "fullName": "", 
                "email": "",
                "googleAccount": "",
                "phone": "",
                "school":"Laval University",
                "schoolProgram": "Software Engineering",
                "graduationDate": 0}
    jeffrey = {"isCaptain": False,
               "fullName": "", 
               "email": "",
               "googleAccount": "",
               "phone": "",
               "school":"Laval University",
               "schoolProgram": "Software Engineering",
               "graduationDate": 0}
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
