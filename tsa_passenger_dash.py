import requests
from bs4 import BeautifulSoup
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from datetime import datetime

# URL of the TSA passenger volumes page
url = 'https://www.tsa.gov/travel/passenger-volumes'

def get_passenger_counts():
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table containing the passenger counts
    table = soup.find('table')

    # Extract the header row
    headers = [th.text.strip() for th in table.find_all('th')]

    # Extract the data rows
    data_rows = table.find_all('tr')[1:]

    # Create a list of dictionaries to store the passenger counts by year
    passenger_counts = []

    # Iterate over the data rows and extract the counts
    for row in data_rows:
        cells = row.find_all('td')
        year = cells[0].text.strip()
        counts = [int(cell.text.strip().replace(',', '')) if cell.text.strip().replace(',', '').isdigit() else None for cell in cells[1:]]
        passenger_counts.append({'Year': year, **dict(zip(headers[1:], counts))})

    df = pd.DataFrame(passenger_counts)

    # Extract month and day from the 'Year' column and convert it to a datetime object
    df['Date'] = df['Year'].apply(lambda x: datetime.strptime(x, '%b %d'))

    # Sort the DataFrame by date in ascending order
    df = df.sort_values('Date')

    return df

# Get passenger counts data
df = get_passenger_counts()

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div(children=[
    html.H1(children='TSA Passenger Counts'),
    dcc.Graph(
        id='passenger-counts-graph',
        figure={
            'data': [
                {'x': df['Date'], 'y': df[header], 'name': header}
                for header in df.columns[1:]
            ],
            'layout': {
                'title': 'TSA Passenger Counts',
                'xaxis': {'title': 'Date'},
                'yaxis': {'title': 'Passenger Count'},
                'legend': {'x': 0, 'y': 1},
                'xaxis_tickangle': -45,
                'xaxis_tickformat': '%b-%d',
                'xaxis_range': [df['Date'].min(), df['Date'].max()],
            }
        }
    )
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
