    let selector = document.getElementById("Selector"); 
    // edit
    let use_or_all = document.getElementById("panel").value; 
    
    
    selector.addEventListener("change", () => {
        // console.log(use_or_all)

        function replaceCanvas() {
            // var cnv = document.getElementById('myChart');
            // if ( !isCanvasEmpty(cnv) ){
              
                var chartContent = document.getElementById('can');
                chartContent.innerHTML = '&nbsp;';
                $('#can').append('<canvas id="myChart" width="400" height="230"></canvas>');
            // }
        };

        // function isCanvasEmpty(cnv) {
        //     const blank = document.createElement('canvas');

        //     blank.width = cnv.width;
        //     blank.height = cnv.height;

        //     return cnv.toDataURL() === blank.toDataURL();
        // }
        replaceCanvas()

        selected_course = selector.value
        if (selector.value != 'default'){
            // result.innerHTML = selected_course
            $.ajax({
            url:"/chartdashboard",
            type:"POST",
            data: {name:selected_course,
            type:use_or_all}, //passin
            error: function() {
                alert("Error");
            },
            success: function(data, status, xhr) {
                
                const ctx = document.getElementById('myChart').getContext('2d');

                var xLabels = data.labels;
                var charts = data.charts;
                // console.log(typeof(xLabels))
                // console.log(typeof(charts))
                // for (const [key, value] of Object.entries(charts)) {
                //     console.log(typeof(value));
                //     // charts.update({key: value.reverse()})
                // }

                for (const [key, values] of Object.entries(charts)) {
                    charts[key] = values.map(value => {
                        let d = new Date(value + '+8'); // GMT+8
                        let year = d.getFullYear();
                        let month = ('' + (d.getMonth() + 1)).padStart(2, '0'); // Month index from index zero so we +1
                        let day = ('' + d.getDate()).padStart(2, '0'); //padStart - to add a zero infront if it is not 2 characters
                        let hour = ('' + d.getHours()).padStart(2, '0');
                        let mins = ('' + d.getMinutes()).padStart(2, '0');
                        return (year + '-' + month + '-' + day + ' ' + hour + ':' + mins + ':00');
                    })
                }

                var vLabels = [];
                var vData = [];
                
                for (const [key, values] of Object.entries(charts)) {
                    let xy = [] // time scale needs a pair
                    vLabels.push(key) // Flight 1
                    for (let i = 0; i < values.length; i++) {
                        xy.push({ 'x': charts[key][i], 'y': xLabels[i] }) // x: Flight 1 data i, y: Hole i
                    }
                    // console.log(xy)
                    vData.push(xy)
                }

                var myChart = new Chart(ctx, {
                    data: {
                    // labels: xLabels,
                    datasets: []
                    },
                    options: {
                        responsive: true,
                        maintainaspectratio: false,
                        scales: {
                        x: {
                            type: 'time',
                            time: {
                                unit: 'hour',
                            }
                        },
                        y: {
                            type: 'category',
                            labels: xLabels,
                            grid: {
                                borderColor: "rgba(249, 238, 236, 0.74)"
                            }
                        }
                    }
                    }
                })

                for (i= 0; i < vLabels.length; i++ ) {
                myChart.data.datasets.push({
                label: vLabels[i], // Flight#
                type: "line",
                // borderColor: '#'+(0x1ff0000+Math.random()*0xffffff).toString(16).substr(1,6),
                borderColor: '#'+(0x1100000+Math.random()*0xffffff).toString(16).substr(1,6),
                backgroundColor: "rgba(249, 238, 236, 0.74)",
                data: vData[i],
                spanGaps: true
                });
                myChart.update();
                }



            }
        })
    }
})
