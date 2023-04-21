from flask import Blueprint, jsonify

class Planet():
    def __init__(self, id, name, description,is_planet):
        self.id = id
        self.name = name
        self.description = description
        self.is_planet = is_planet


planets = [
    Planet(1, "Mercury", "Even though Mercury is the closest planet to the sun, it has ice on its surface.", True),
    Planet(2, "Venus", "Venus is the hottest planet in our solar system and doesn't have any moons.", True),
    Planet(3, "Earth", "Earth is not flat.", True),
    Planet(4, "Mars", "Mars once had water on its surface.", True),
    Planet(5, "Jupiter", "Jupiter is a great comet catcher.", True),
    Planet(6, "Saturn", "No one knows how old Saturn’s rings are.", True),
    Planet(7, "Uranus", "Uranus is the only planet in the solar system whose axis is tilted nearly 98 degrees.", True),
    Planet(8, "Neptune", "Neptune has supersonic winds.", True),
    Planet(9, "Pluto", "Pluto is a Dwarf Planet.", False)
]