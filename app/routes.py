from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.Model.planet import Planet


# planets = [
#     Planet(
#         1,
#         "Mercury",
#         "Even though Mercury is the closest planet to the sun, it has ice on its surface.",
#         True,
#     ),
#     Planet(
#         2,
#         "Venus",
#         "Venus is the hottest planet in our solar system and doesn't have any moons.",
#         True,
#     ),
#     Planet(3, "Earth", "Earth is not flat.", True),
#     Planet(4, "Mars", "Mars once had water on its surface.", True),
#     Planet(5, "Jupiter", "Jupiter is a great comet catcher.", True),
#     Planet(6, "Saturn", "No one knows how old Saturn’s rings are.", True),
#     Planet(
#         7,
#         "Uranus",
#         "Uranus is the only planet in the solar system whose axis is tilted nearly 98 degrees.",
#         True,
#     ),
#     Planet(8, "Neptune", "Neptune has supersonic winds.", True),
#     Planet(9, "Pluto", "Pluto is a Dwarf Planet.", False),
# ]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")


def verify_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message": f"Planet {planet_id} is invalid"}, 400))

    planet = Planet.query.get(planet_id)

    if not planet:
        abort(make_response({"message": f"Planet {planet_id} not found"}, 404))

    return planet


@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(
        name=request_body["name"],
        description=request_body["description"],
        is_planet=request_body["is_planet"],
    )

    db.session.add(new_planet)
    db.session.commit()

    return {"name": new_planet.name, "msg": "Successfully created"}, 201

@planets_bp.route("", methods=["GET"])
def view_all_planets():
    id_query = request.args.get("id")
    name_query = request.args.get("name")
    description_query = request.args.get("description")
    is_planet_query = request.args.get("is_planet")

    planet_query = Planet.query

    if id_query:
        planet_query = planet_query.filter_by(id=id_query)

    if name_query:
        planet_query = planet_query.filter_by(name=name_query)

    if description_query:
        planet_query = planet_query.filter_by(description=description_query)
    
    if is_planet_query:
        planet_query = planet_query.filter_by(is_planet=is_planet_query)

    planets = planet_query.all()
    
    all_planets = [planet.format_planet_dict() for planet in planets]

    return jsonify(all_planets), 200


@planets_bp.route("/<planet_id>", methods=["GET"])
def lookup_one_planet(planet_id):
    planet = verify_planet(planet_id)
    return planet.format_planet_dict()
