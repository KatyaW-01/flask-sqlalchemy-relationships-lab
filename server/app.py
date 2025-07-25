#!/usr/bin/env python3

from flask import Flask, jsonify, make_response
from flask_migrate import Migrate

from models import db, Event, Session, Speaker, Bio

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

# TODO: add functionality to all routes

@app.route('/events')
def get_events():
    events = []
    for event in Event.query.all():
        event_dict = {
            "id": event.id,
            "location": event.location,
            "name": event.name
            
        }
        events.append(event_dict)
    
    body = events
    status = 200
    return make_response(body, status)
        


@app.route('/events/<int:id>/sessions')
def get_event_sessions(id):
    event = Event.query.filter_by(id = id).first()
    sessions = []
    if event:
        for session in event.sessions:
            session_dict = {
                "id": session.id,
                "title": session.title,
                "start_time": session.start_time
            }
            sessions.append(session_dict)
        body = sessions
        status = 200
    else:
        body = {'message': f'Event {id} not found'}
        status = 404

    return make_response(body, status)



@app.route('/speakers')
def get_speakers():
    pass


@app.route('/speakers/<int:id>')
def get_speaker(id):
    pass


@app.route('/sessions/<int:id>/speakers')
def get_session_speakers(id):
    pass


if __name__ == '__main__':
    app.run(port=5555, debug=True)