import dash
import dash_core_components as dcc
import dash_html_components as html


app = dash.Dash()
app.title = 'Natural Disaster'

# Boostrap CSS.
app.css.append_css({'external_url': 'https://codepen.io/amyoshino/pen/jzXypZ.css'})

app.layout = html.Div([
    
    html.Div([
        html.H1('Impact of Disasters on Human Lives',
                style={'font-family':'Helvetica',
                'color':'darkblue',
                
                
                }, className = 'row'),

        html.H4('331M Deaths so far',
                style={
                'font-family':'HelveticaNeue',
                'font-size':'5',
                'color':'red',
                
                
                 }, className = 'row'),
    ], className = 'row'),
    
    
    html.Div([
       html.Div([
            
            html.Iframe(
                   sandbox='allow-scripts',
                   id='plot_a',
                   height = '500en',
                   width = '500en',
                   style={'border':'none'},

                   ################ The magic happens here
                   srcDoc=open('charts/temp_plot_a.html').read()
                   ################ The magic happens here
                   ),
                   
            html.Iframe(
                   sandbox='allow-scripts',
                   id='plot_b',
                   height = '500en',
                   width = '500en',
                   style={'border':'none'},

                   ################ The magic happens here
                   srcDoc=open('charts/temp_plot_b.html').read()
                   ################ The magic happens here
                                   ),
      ], className = 'row'),
            ], className = 'container'),
    
    
    
    html.Div([
      html.Div([
            
            html.Iframe(
                     sandbox='allow-scripts',
                     id='plot_c',
                     style={'border':'none', 'position':'absolute', 'width':'100%', 'height':'100%'},

                     ################ The magic happens here
                     srcDoc=open('charts/world_map_line.html').read()
                     ################ The magic happens here
                     ),
      ], className = 'row')
    
    ], className = 'container')

], id = 'main', className = 'container', style = {'margin-left':'15%'})




if __name__ == '__main__':
    app.run_server(debug=True)