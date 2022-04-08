function showError( error ) {
    console.log( 'getCurrentPosition returned error', error);
}

function sendWeatherRequest(position){
    const lat = position.coords.latitude;
    const long = position.coords.longitude;
    console.log("lat: ", lat);
    console.log("long: ", long);  

    let url = "https://api.openweathermap.org/data/2.5/weather?lat={" + lat + "}&lon={" + long + "}&appid={f4d4a5436717f42babd6179c9f17c342}";
    console.log("url: ", url);


    const Http = new XMLHttpRequest();
    // const url='https://api.openweathermap.org/data/2.5/weather?lat={37.6202407}&lon={-122.0858749}&appid={f4d4a5436717f42babd6179c9f17c342}';
    Http.open("GET", url);
    Http.send();

    Http.onreadystatechange = (e) => {
        console.log("Http.responseText: ", Http.responseText);
        console.log("type of responseText: ", typeof(Http.responseText));

        const response = JSON.parse(Http.responseText);
        console.log("response.cod: ", response.cod);
        console.log("response.message: ", response.message);
    }
    
    

    
}

function getLocationAndSendWeatherRequest(event){
    navigator.geolocation.getCurrentPosition(sendWeatherRequest, showError);


    event.preventDefault();
}


const weatherButton = document.getElementById('weatherButton');
weatherButton.addEventListener("click", getLocationAndSendWeatherRequest);