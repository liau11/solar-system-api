import pytest
from app import create_app
from app import db
from flask.signals import request_finisheded
from app.models.planet import Planet


@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()
    
    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()



@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def data_for_two_planets(client):
    planet_one = Planet((id=1, name="Furby", description="It's a planet with furbies!!", is_planet=True)
    planet_two = Planet((id=2, name="Onions", description="It's a planet with onions!!", is_planet=True)
                        
    two_planets = db.session.add_all([planet_one, planet_two])
    
    db.session.commit()


