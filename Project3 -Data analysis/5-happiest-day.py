import justpy as jp
import pandas 
from datetime import datetime

data = pandas.read_csv('reviews.csv' , parse_dates = ['Timestamp'])
data['Weekday']= data['Timestamp'].dt.strftime('%A')
data['Daynum'] = data['Timestamp'].dt.strftime('%w')

weekday_average = data.groupby(['Weekday' , 'Daynum']).mean()
weekday_average = weekday_average.sort_values('Daynum')

chart_def = """
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Atmosphere Temperature by Altitude'
    },
    subtitle: {
        text: 'According to the Standard Atmosphere Model'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Altitude'
        },
        labels: {
            format: '{value} km'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Temperature'
        },
        labels: {
            format: '{value}°'
        },
        accessibility: {
            rangeDescription: 'Range: -90°C to 20°C.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x} km: {point.y}°C'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Temperature',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}
"""

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp , text = "Analysis of Course Reviews " , classes = 'text-h3 text-center q-pa-md')
    p1 = jp.QDiv(a=wp , text = 'These graphs represent course review analysis')
    hc = jp.HighCharts(a=wp , options = chart_def)
    hc.options.title.text = "Aggregated Average Rating by Day of the Week"
    hc.options.subtitle.text = 'According to the Course Reviews Dataset'

    hc.options.xAxis.title.text = 'Day'
    hc.options.xAxis.labels.format = '{value}'
    hc.options.yAxis.title.text = 'Average Rating'
    hc.options.yAxis.labels.format = '{value}'
    hc.options.series[0].name = 'Average Rating '
    hc.options.tooltip.pointFormat = '{point.y}'

    hc.options.xAxis.categories = list(weekday_average.index.get_level_values(0))
    hc.options.series[0].data = list(weekday_average['Rating'])

    return wp

jp.justpy(app)