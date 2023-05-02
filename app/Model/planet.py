from app import db


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80))
    description = db.Column(db.String(200))
    is_planet = db.Column(db.Boolean)

    def format_planet_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            description=self.description,
            is_planet=self.is_planet,
        )
