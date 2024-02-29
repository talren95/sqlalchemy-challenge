# Import the dependencies.
from flask import Flask, jsonify
import datetime as dt
from sqlalchemy import func, create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

# Initialize the Flask app
app = Flask(__name__)

# Create engine to hawaii.sqlite
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect an existing database into a new model
base = automap_base()

# Reflect the tables
base.prepare(engine, reflect=True)

# Save references to each table
Measurement = base.classes.measurement
Station = base.classes.station

# Create session (link) from Python to the DB
session = Session(engine)

# Homepage and all available routes 
@app.route("/")
def home():
    return (
        f"Welcome to The Climate App!<br/><br/>"
        f"Available Routes:<br/>"
        f"<a href='/api/v1.0/precipitation'> precipitation </a><br/>"
        f"<a href='/api/v1.0/stations'> stations </a><br/>"
        f"<a href='/api/v1.0/tobs'> tobs </a><br/>"
        f"<a href='/api/v1.0/<start>'> start </a><br/>"
        f"<a href='/api/v1.0/<start>/<end>'> start/end </a>"
        )

# Precipitation page that returns JSON if user requests data in json format
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Calculate the date one year ago from the last data point in the database
    most_recent_date_query = session.query(func.max(Measurement.date))
    most_recent_date = most_recent_date_query.scalar() or dt.datetime.min.date()
    most_recent_date = dt.datetime.strptime(most_recent_date, '%Y-%m-%d').date()
    one_year_ago = most_recent_date - dt.timedelta(days=365)
    
    # Query to retrieve precipitation data for the last 12 months
    precipitation_data = session.query(Measurement.date, Measurement.prcp)\
                                .filter(Measurement.date >= one_year_ago)\
                                .all()
    
    # Convert the query results to a dictionary
    precipitation_dict = {date: prcp for date, prcp in precipitation_data}
    
    return jsonify(precipitation_dict)

# Stations page that returns a list of station names that returns JSON if user requests data in json format
@app.route("/api/v1.0/stations")
def stations():
    # Query to retrieve the list of stations
    stations = session.query(Station.station).all()
    
    # Convert the query results to a list
    station_list = [station[0] for station in stations]
    
    return jsonify(station_list)

#  TOBs page that takes the starting date and returns a list of high temperatures, low temperatures, and dates that returns JSON if user requests data in json format
@app.route("/api/v1.0/tobs")
def tobs():
    # Get the station ID with the highest count
    most_active_station = session.query(Measurement.station)\
                                  .group_by(Measurement.station)\
                                  .order_by(func.count(Measurement.station).desc())\
                                  .first()[0]
    
    # Calculate the date one year ago from the last data point in the database
    most_recent_date = session.query(func.max(Measurement.date)).scalar()
    most_recent_date = dt.datetime.strptime(most_recent_date, '%Y-%m-%d').date()
    one_year_ago = most_recent_date - dt.timedelta(days=365)
    
    # Query to retrieve temperature observations for the most active station for the previous year
    temperature_data = session.query(Measurement.date, Measurement.tobs)\
                                .filter(Measurement.station == most_active_station)\
                                .filter(Measurement.date >= one_year_ago)\
                                .all()
    
    # Convert the query results to a list of dictionaries
    temperature_list = [{"Date": date, "Temperature": tobs} for date, tobs in temperature_data]
    
    return jsonify(temperature_list)

# Start page that returns the min, max, and average temperatures calculated from the given start date to the end of the dataset and returns JSON if user requests data in json format
@app.route("/api/v1.0/<start>")
def temp_stats_start(start):
    # Query to retrieve temperature observations for all stations and dates greater than or equal to the start date
    temperature_data = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs))\
                                .filter(Measurement.date >= start)\
                                .all()

    # Convert the query results to a list of dictionaries
    temperature_list = [{"TMIN": min, "TAVG": avg, "TMAX": max} for min, avg, max in temperature_data]

    return jsonify(temperature_list)

# Start and End page that returns the min, max, and average temperatures calculated from the given start date to the given end date and returns JSON if user requests data in json format
@app.route("/api/v1.0/<start>/<end>")
def temp_stats_range(start, end):
    # Query to retrieve temperature observations for all stations and dates between the start and end dates, inclusive
    temperature_data = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs))\
                                .filter(Measurement.date >= start)\
                                .filter(Measurement.date <= end)\
                                .all()

    # Convert the query results to a list of dictionaries
    temperature_list = [{"TMIN": min, "TAVG": avg, "TMAX": max} for min, avg, max in temperature_data]

    return jsonify(temperature_list)
    
# Run the app
if __name__ == "__main__":
    app.run(debug=True)