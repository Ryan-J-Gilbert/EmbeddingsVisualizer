from flask import Flask, jsonify, render_template
import pandas as pd

app = Flask(__name__)

df = pd.read_csv('toydataset.csv')

@app.route('/data')
def get_plot_data():

    color_map = {
        0: 'red',
        1: 'white',
        2: 'blue',
        3: 'green',
        4: 'yellow',
        5: 'purple',
        6: 'orange',
        7: 'pink',
        8: 'brown',
        9: 'gray'
    }
    # colors = df['type'].map(color_map).tolist()
    colors = df['digit'].map(color_map).tolist()

    # Prepare data for Plotly
    plot_data = [{
        'x': df['x'].tolist(),
        'y': df['y'].tolist(),
        'z': df['z'].tolist(),
        'type': 'scatter3d',
        'mode': 'markers',
        'marker': {'size': 8, 'color': colors},
        'text': df['digit'].tolist(),  # Add labels for hover
        'customdata': ('static/images/'+df['image']).tolist(),

        # 'hoverinfo': 'text',
        # 'hovertemplate': '<b>Digit:</b> %{text}<br>' +
        #                  '<b>Image:</b> <img src="static/images/%{customdata}" style="width:50px;height:50px;"><extra></extra>',
        'name': 'scatter3d'
    }]

    # Prepare layout configuration
    layout = {
        'scene': {
            'xaxis': {'visible': False},
            'yaxis': {'visible': False},
            'zaxis': {'visible': False}
        },
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',
        'width': 1000,
        'height': 1000
    }

    return jsonify({'data': plot_data, 'layout': layout})


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
