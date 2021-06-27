import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import numpy as np
from dash.dependencies import Output, Input, State
from simulation import independence, anti_conformity
from dash.exceptions import PreventUpdate
from lattices import circle, diagonal_stripes, chessboard, random_lattice, two_stripes


lattices = [two_stripes, diagonal_stripes, chessboard, circle, random_lattice]
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets, assets_folder="assets", update_title=None)
server = app.server


interval_time = 1*400
fig = go.Figure(data=go.Heatmap(z=random_lattice(25), showscale=False,
                                colorscale=[
                                    [0, "rgb(0, 21, 79)"],
                                    [0.5, "rgb(0, 21, 79)"],
                                    [0.5, "rgb(250, 140, 80)"],
                                    [1, "rgb(250, 140, 80)"]
                                ]),
                layout=go.Layout(
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)')
                )
fig.update_yaxes(
    scaleanchor="x",
    scaleratio=1
  )
fig.update_xaxes(
    constrain="domain",
)
fig.update_layout(
    title={
        'text': "q-voter model simulation",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    title_font={"size": 25}
)


fig2 = go.Figure(data=go.Scatter(x=[0],  y=[0]))

fig2.update_layout(
    title="Average opinion over time",
    xaxis_title="time",
    yaxis_title="mean value of spins",
    template="seaborn"
)

fig2.update_yaxes(
    range=[-1, 1]
)

app.layout = html.Div(id="page", children=[
        html.Div(
            id='left_col',
            children=[
                html.Div(
                    id='graph_parent',
                    children=[dcc.Graph(figure=fig, id='graph', animate=True)]
                        ),
                dcc.Interval(id='update', interval=interval_time, n_intervals=0),
                dcc.Store(id='data', data=(random_lattice(25), [0], [0])),
                html.Div(id="buttons",
                         children=[
                             html.Button("Run / Stop", id="run", n_clicks=0),
                             html.Button("Setup", id="setup", n_clicks=0)
                         ]
                         )
                    ]
                ),
        html.Div(
            id="right_col",
            children=[
                dcc.Graph(figure=fig2, id='graph2', animate=True),
                html.Div(id="params_div", children=[
                    html.Div(id="left_params", children=[
                        html.Label("Choose nonconformity type", id="conformity_label"),
                        dcc.Dropdown(id="conformity_dropdown",
                                     options=[
                                         {'label': 'conformity and independence', 'value': 0},
                                         {'label': 'conformity and anticonformity', 'value': 1}
                                     ],
                                     value=0
                                     ),
                        html.Label("Choose the way of drawings", id="drawings_label"),
                        dcc.Dropdown(id="drawings_dropdown",
                                     options=[
                                         {'label': 'drawings with replacement', 'value': 1},
                                         {'label': 'drawings without replacement', 'value': 0}
                                     ],
                                     value=1
                                     ),
                        html.Label("Choose the type of the lattice", id="lattice_label"),
                        dcc.Dropdown(id='lattice_dropdown',
                                     options=[
                                         {'label': 'stripes', 'value': 0},
                                         {'label': 'diagonal stripes', 'value': 1},
                                         {'label': 'chessboard', 'value': 2},
                                         {'label': 'circle', 'value': 3},
                                         {'label': 'random', 'value': 4}
                                     ],
                                     value=4)]),
                    html.Div(id="right_params", children=[
                        html.Label('N = ', id='N_label'),
                        dcc.Input(id="N", value=25, type="number"),
                        html.Label('q = ', id='q_label'),
                        dcc.Input(id="q", value=3, type="number"),
                        html.Label('p = ', id='p_label'),
                        dcc.Input(id="p", value=0.5, type="number"),
                        html.Label('f = ', id='f_label'),
                        dcc.Input(id="f", value=0.4, type="number")]
                     )
                    ])
            ]
        ),
        html.Div(id="footer_div", children=[
            html.Footer("M.K", id="footer")
        ])
]
)


@app.callback(Output('update', 'interval'),
              Input('run', 'n_clicks'))
def update_interval(n):
    """
    Update the length of interval according to the number of button clicks.
    :param n: number of 'setup' button clicks
    :return: length of time interval
    """
    if n % 2 == 1:
        return interval_time
    return 10**6


@app.callback(Output('graph', 'extendData'),
              Output('graph2', 'extendData'),
              Output('data', 'data'),
              Input('run', 'n_clicks'),
              Input('setup', 'n_clicks'),
              Input('update', 'n_intervals'),
              State('lattice_dropdown', 'value'),
              State('conformity_dropdown', 'value'),
              State('drawings_dropdown', 'value'),
              State('N', 'value'),
              State('q', 'value'),
              State('p', 'value'),
              State('f', 'value'),
              State('data', 'data'),
              prevent_initial_call=True
              )
def update_data(n1, n2, k, lattice, nonconformity, drawings, N, q, p, f, data):
    """

    :param n1:
    :param n2:
    :param k:
    :param lattice:
    :param nonconformity:
    :param drawings:
    :param N:
    :param q:
    :param p:
    :param f:
    :param data:
    :return:
    """
    if n1 == 0 and n2 == 0:
        raise PreventUpdate
    ctx = dash.callback_context
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    data1, X, Y = data
    if button_id == "setup":
        X = list([0])
        Y = list([0])
        func = lattices[lattice]
        data2 = func(N)
        return (dict(z=[data2]), 0, N), (dict(x=[[0]], y=[[0]]), [0], len(X)), (data2, X, Y)
    if nonconformity == 0:
        data_2 = independence(data1, N, drawings, q, p, f)
    else:
        data_2 = anti_conformity(data1, N, drawings, q, p)
    num = np.mean(data_2)
    X.append(X[-1]+1)
    Y.append(num)
    return (dict(z=[data_2]), 0, N), (dict(x=[[X[-1]+1]], y=[[num]]), [0], len(X)), (data_2, X, Y)


if __name__ == "__main__":
    app.run_server(debug=True)
