function Bar(x, y) {
    var data = [{
        type: 'bar',
        orientation: 'v',
        x: x,
        y: y,
        marker: {
            color: 'rgb(50,93,121)',
            width: 1
          }
    }];

    var layout = {
        plot_bgcolor: "rgba(0,0,0,0)",
        paper_bgcolor: "rgba(0,0,0,0)",
        title: {
            text:'Average Rating by Genre',
            font: {
                family: 'Courier New, monospace',
                size: 24,
                color: "#325D79"
            },
            xref: 'paper',
        },
        yaxis: {
            range: [3.2, 4],
            title: {
                text: 'Average Rating',
                font: {
                    family: 'Courier New, monospace',
                    size: 20,
                    color: "#325D79"
                }
            },
        },
        font: {
            size: 14,
            color: "#325D79"
        }
      };

    Plotly.newPlot('plot', data, layout);
}

function Line(x, y) {
    var data = [{
        type: 'line',
        x: x,
        y: y,
    }];

    var layout = {
        plot_bgcolor: "rgba(0,0,0,0)",
        paper_bgcolor: "rgba(0,0,0,0)",
        font: {
            size: 12,
            color: "#5b565a"
        }
      };

    Plotly.newPlot('linePlot', data, layout);
}

const url = "/genre_data";

d3.json(url).then((data) => {
    // bar graph
    // console.log(data);
    const avgRate = data.genreAvg.avgRate
    const genre = data.genreAvg.Genre
    Bar(genre, avgRate);

    // line graph
    const Year = data.ratings.Year
    const avgRating = data.ratings.avgRate
    // Line(Year, avgRating)
});