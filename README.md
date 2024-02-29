# sqlalchemy-challenge

## Repository Structure:
Both codes (climate_starter.ipynb and app.py) will be found within the "climate" directory in this repository.
The CSV and SQLite files (hawaii_measurements.csv, hawaii.csv, and hawaii.sqlite) can be found in the "resources" folder within the same "climate" directory.

## Code 1 - climate_starter.ipynb (Jupyter Notebook Code):
### Data Retrieval and Visualization:
- This code primarily focuses on retrieving data from a SQLite database (hawaii.sqlite) using SQLAlchemy and visualizing it using Matplotlib.
- It imports necessary libraries like matplotlib, numpy, pandas, and datetime.
- It establishes a connection to the SQLite database and reflects the tables using SQLAlchemy's automap_base.
- Retrieves the most recent date and performs queries to obtain precipitation and temperature data for the last 12 months.
- Visualizes the precipitation data using Matplotlib.
- Calculates summary statistics for precipitation and temperature data.
- Finds the total number of stations and the most active station.
- Lastly, it visualizes temperature data for the most active station over the last 12 months using a histogram.

## Code 2 - app.py (Python Code using Flask):
### Web API Setup:
- This code sets up a Flask web application to create a RESTful API for accessing the same data.
- It imports necessary Flask libraries and SQLAlchemy.
- Establishes a connection to the same SQLite database and reflects the tables.
- Defines various routes to handle different types of data requests.
- The routes include:
  - /api/v1.0/precipitation: Returns precipitation data for the last 12 months.
  - /api/v1.0/stations: Returns a list of weather stations.
  - /api/v1.0/tobs: Returns temperature observations for the last 12 months from the most active station.
  - /api/v1.0/<start>: Returns temperature statistics (min, max, avg) from a given start date until the end of the dataset.
  - /api/v1.0/<start>/<end>: Returns temperature statistics (min, max, avg) between a given start and end date.
- The data is fetched from the SQLite database using SQLAlchemy queries, converted into appropriate formats, and returned as JSON responses.

## Analysis Summary:
- Both codes offer in-depth analysis of weather data from Hawaii, focusing on precipitation and temperature.
- Code 1 provides a detailed exploration within a Jupyter Notebook environment, including statistical analysis and visualizations using Matplotlib.
- The visualizations and summary statistics reveal insights into seasonal patterns, trends, and variability in Hawaii's weather, aiding in understanding climate dynamics.
- Code 2 extends the analysis by transforming it into a dynamic web API, enhancing accessibility and usability for a wider audience.
- By providing programmable access to the weather data, the API enables integration with other applications or analytical tools, fostering further exploration, research, and decision-making related to Hawaii's climate.



