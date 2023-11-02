import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Input(id='input1', type='number', placeholder='请输入第一个数字'),
    dcc.Input(id='input2', type='number', placeholder='请输入第二个数字'),
    html.Button('相加', id='add-button'),
    html.Div(id='output', style={'textAlign': 'center', 'fontSize': '72px', 'color': 'red'})
])

@app.callback(
    Output('output', 'children'),
    [Input('add-button', 'n_clicks')],
    [dash.dependencies.State('input1', 'value'),
     dash.dependencies.State('input2', 'value')]
)
def update_output(n_clicks, input1, input2):
    if n_clicks is None:
        return ''
    else:
        return f'结果是：{float(input1) + float(input2)}'

if __name__ == '__main__':
    app.run_server(debug=True)
