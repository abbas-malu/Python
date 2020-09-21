console.log('its working')

let api_key = '70121c1eaf3d32f16cef18f3b0ee3b5c'

const xhr = new XMLHttpRequest();
xhr.open('GET', `http://api.openweathermap.org/data/2.5/weather?q=indore&appid=${api_key}`, true);

xhr.onload = function () {
    if (this.status === 200) {
        let weather = JSON.parse(this.responseText)
        console.log(JSON.stringify(weather))
    }
}
xhr.send()


let searchBtn = document.getElementById('citySearch')
searchBtn.addEventListener('input', setTxt)

function setTxt() {
    // console.log(document.getElementById('searchTxt').value)
    let search = document.getElementById('citySearch').value;
    let display = document.getElementById('weatherDisplay')
    display.innerHTML = ''
    const xhr = new XMLHttpRequest();
    xhr.open('GET', `http://api.openweathermap.org/data/2.5/weather?q=${search}&appid=${api_key}`, true);

    xhr.onload = function () {
        if (this.status === 200) {
            let curWeather = JSON.parse(this.responseText)
            display.innerHTML += curWeather.coord.lon
            display.innerHTML += `<br>`
            display.innerHTML += curWeather.coord.lat
            display.innerHTML += curWeather.weather[0].id
            display.innerHTML += `<br>`
            display.innerHTML += curWeather.weather[0].main
            display.innerHTML += `<br>`
            display.innerHTML += curWeather.weather[0].description
            display.innerHTML += `<br>`
            display.innerHTML += `<img src="http://openweathermap.org/img/wn/${curWeather.weather[0].icon}@4x.png">`
            display.innerHTML += `<br>`
            display.innerHTML += curWeather.main.temp - 273.15
            display.innerHTML += `<br>`
            display.innerHTML += curWeather.main.feels_like - 273.15
            display.innerHTML += `<br>`
            display.innerHTML += curWeather.main.temp_min - 273.15
            display.innerHTML += `<br>`
            display.innerHTML += curWeather.main.temp_max - 273.15

        }
    }

    xhr.send()
}

