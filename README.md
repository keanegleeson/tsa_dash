# TSA Passenger Counts Dash App

This is a web application built with Dash that displays TSA passenger counts over time in a line graph. The data is scraped from the [TSA website](https://www.tsa.gov/travel/passenger-volumes) and visualized using the Matplotlib library.

## Features

- Retrieves passenger count data from the TSA website
- Displays the data in a line graph with multiple series
- Supports interactive exploration of the graph (zoom, pan, etc.)
- Formats the x-axis to show dates in Month-Day format
- Sorts the dates in ascending order

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/tsa-passenger-counts-app.git

## Usage

1. Change into the project directory:

```cd tsa-passenger-counts-app```

2. Install the required dependencies:

```pip install -r requirements.txt```

3. Run the Dash app

```python tsa_passenger_dash.py```

4. Open http://127.0.0.1:8050/ in a browser to view the data.