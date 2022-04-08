

  
function showPosition(position) {
    let lat = position.coords.latitude;
    let lon = position.coords.longitude; 
    
    

    const Http = new XMLHttpRequest();
    const url='https://api.openweathermap.org/data/2.5/weather?lat=' + lat + '&lon=' + lon + '&appid=f4d4a5436717f42babd6179c9f17c342';
    Http.open("GET", url);
    Http.send();
 
    Http.onreadystatechange = (e) => {
        if (Http.responseText) {
            console.log(Http.responseText);

            const result = JSON.parse(Http.responseText);
            
            //console.log('result: ', result);
            let temp = result.main.temp;
            let weather = result.weather[0].main;
            let iconid = result.weather[0].icon;
            console.log('main.temp result: ', result.main.temp);
            console.log('weather result: ', result.weather[0].main);
            let iconurl = 'http://openweathermap.org/img/wn/'+ iconid + '@2x.png';


            document.getElementById("weatherDescript").textContent ="Today's weather: " + temp + " " + weather;

            document.getElementById("weathericon").setAttribute("src", iconurl);

        }

    }
}

function weatherRequest(event){

    navigator.geolocation.getCurrentPosition(showPosition);


    event.preventDefault();     
}


const weatherButton = document.getElementById('weatherButton');
weatherButton.addEventListener('click',weatherRequest);