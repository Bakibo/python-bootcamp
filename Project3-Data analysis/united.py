import justpy as jp
import pandas 
from datetime import datetime

data = pandas.read_csv('reviews.csv' , parse_dates = ['Timestamp'])
data['Day'] = data['Timestamp'].dt.date
day_average = data.groupby(['Day']).mean()
data['Week'] = data['Timestamp'].dt.strftime('%Y-%U')
week_average = data.groupby(['Week']).mean()
data['Month'] = data['Timestamp'].dt.strftime('%Y-%m')
month_average = data.groupby(['Month']).mean()
month_average_course = data.groupby(['Month' , 'Course Name']).mean().unstack()

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
    hc.options.title.text = "Average Rating by Day"
    hc.options.subtitle.text = 'According to the Course Reviews Dataset'

    hc.options.xAxis.title.text = 'Date'
    hc.options.xAxis.labels.format = '{value}'
    hc.options.yAxis.title.text = 'Average Rating'
    hc.options.yAxis.labels.format = '{value}'
    hc.options.series[0].name = 'Average Rating '
    hc.options.tooltip.pointFormat = '{point.x}: {point.y}'

    hc.options.xAxis.categories = list(day_average.index)
    hc.options.series[0].data = list(day_average['Rating'])

    hc1 = jp.HighCharts(a=wp , options = chart_def)
    hc1.options.title.text = "Average Rating by Week"
    hc1.options.subtitle.text = 'According to the Course Reviews Dataset'

    hc1.options.xAxis.title.text = 'Date'
    hc1.options.xAxis.labels.format = '{value}'
    hc1.options.yAxis.title.text = 'Average Rating'
    hc1.options.yAxis.labels.format = '{value}'
    hc1.options.series[0].name = 'Average Rating '
    hc1.options.tooltip.pointFormat = 'Row {point.x}: {point.y}'

    hc1.options.xAxis.categories = list(week_average.index)
    hc1.options.series[0].data = list(week_average['Rating'])

    hc2 = jp.HighCharts(a=wp , options = chart_def)
    hc2.options.title.text = "Average Rating by Month"
    hc2.options.subtitle.text = 'According to the Course Reviews Dataset'

    hc2.options.xAxis.title.text = 'Date'
    hc2.options.xAxis.labels.format = '{value}'
    hc2.options.yAxis.title.text = 'Average Rating'
    hc2.options.yAxis.labels.format = '{value}'
    hc2.options.series[0].name = 'Average Rating '
    hc2.options.tooltip.pointFormat = 'Row {point.x}: {point.y}'

    hc2.options.xAxis.categories = list(month_average.index)
    hc2.options.series[0].data = list(month_average['Rating'])

    return wp
    
print(data['Month'])
jp.justpy(app)