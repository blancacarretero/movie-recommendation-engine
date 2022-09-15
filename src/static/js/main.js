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
};

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

    Plotly.newPlot('plot', data, layout);
};

function index() {
    const url = "/genre_data";
    d3.json(url).then((data) => {
        // bar graph
        const avgRate = data.genreAvg.avgRate;
        const genre = data.genreAvg.Genre;
        Bar(genre, avgRate);
    });
};

function genre() {
    const url = "/genre_data";
    d3.json(url).then((data) => {
        // genre buttons
        const genres = data.genreAvg.Genre
        for (let i = 0; i < genres.length; i++) {
            console.log(genres[i])
            d3.select()
            let buttonDiv = d3.select("#buttons")
            buttonDiv.append("button").text(genres[i]).classed('btn btn-info', true).attr("onclick",`optionChanged('${genres[i]}')`);
        };
    });
};

// master function to grab data and display charts based on value input

function optionChanged(val) {
    let url = `/data/${val}`
    d3.json(url).then((data) => {

        let heading = d3.select("#heading");
        heading.html(`<h1>${val}</h1>`);
        
        let averageRating = data['Average Rating'];
        let Year = data['Year'];
        console.log(averageRating);

        Line(Year, averageRating);
    });
};