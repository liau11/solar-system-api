from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.model.planet import Planet


class Planet:
    def __init__(self, id, name, description, is_planet):
        self.id = id
        self.name = name
        self.description = description
        self.is_planet = is_planet

    def format_planet_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            description=self.description,
            is_planet=self.is_planet,
        )


planets = [
    Planet(
        1,
        "Mercury",
        "Even though Mercury is the closest planet to the sun, it has ice on its surface.",
        True,
    ),
    Planet(
        2,
        "Venus",
        "Venus is the hottest planet in our solar system and doesn't have any moons.",
        True,
    ),
    Planet(3, "Earth", "Earth is not flat.", True),
    Planet(4, "Mars", "Mars once had water on its surface.", True),
    Planet(5, "Jupiter", "Jupiter is a great comet catcher.", True),
    Planet(6, "Saturn", "No one knows how old Saturn’s rings are.", True),
    Planet(
        7,
        "Uranus",
        "Uranus is the only planet in the solar system whose axis is tilted nearly 98 degrees.",
        True,
    ),
    Planet(8, "Neptune", "Neptune has supersonic winds.", True),
    Planet(9, "Pluto", "Pluto is a Dwarf Planet.", False),
]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")


def verify_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message": f"Planet {planet_id} is invalid"}, 400))

    for planet in planets:
        if planet.id == planet_id:
            return planet

    abort(make_response({"message": f"Planet {planet_id} not found"}, 404))


@planets_bp.route("", methods=["GET"])
def get_planets():
    planet_dict = [vars(planet) for planet in planets]

    return jsonify(planet_dict), 200


@planets_bp.route("/<planet_id>", methods=["GET"])
def lookup_planet(planet_id):
    planet = verify_planet(planet_id)
    return planet.format_planet_dict()
