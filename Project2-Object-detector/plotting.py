from motion_detector import df
from bokeh.plotting import figure , output_file , show
from bokeh.models import HoverTool , ColumnDataSource 

cds = ColumnDataSource(df)

p=figure(x_axis_type = 'datetime' , height = 100 , width = 500 , sizing_mode='scale_width' ,
 title = "Motion Graph")
p.yaxis.minor_tick_line_color = None

hover = HoverTool(tooltips=[("Start" , "@Start{%Y-%m-%d %H:%M:%S}") , ("End" , "@End{%Y-%m-%d %H:%M:%S}")] , formatters={'@Start': 'datetime','@End': 'datetime'})
p.add_tools(hover)

q = p.quad(left ="Start" , right ="End" , bottom = 0 , top = 1 , color = "green" , source=cds)

output_file("Graph.html")
show(p)