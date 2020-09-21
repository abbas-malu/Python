console.log('Its working')
let apiKey = 'ab75650446d04d60a5742f4b2fa3f88b'

let searchBtn = document.getElementById('searchTxt')
searchBtn.addEventListener('input', setTxt)

function setTxt() {
    // console.log(document.getElementById('searchTxt').value)
    let search = document.getElementById('searchTxt').value;
    const xhr = new XMLHttpRequest();
    xhr.open('GET', `https://newsapi.org/v2/everything?q=${search}&apiKey=${apiKey}`, true);

    xhr.onload = function () {
        if (this.status === 200) {
            let news = JSON.parse(this.responseText)
            let articles = news.articles
            let latNews = ''
            let newsDiv = document.getElementById('newsDiv')
            articles.forEach(function (element, index) {
                latNews += `<div class="card mb-3" style="max-width: 540px;">
            <div class="row no-gutters">
              <div class="col-md-4">
                <img src="${element['urlToImage']}" class="card-img" alt="...">
              </div>
              <div class="col-md-8">
                <div class="card-body">
                  <h5 class="card-title">${element['title']}</h5>
                  <p class="card-text">${element["description"]}</p>
                  <p class="card-text"><small class="text-muted">Published At ${element['publishedAt']}</small></p>
                </div>
              </div>
            </div>
          </div>
          `
            });
            newsDiv.innerHTML = latNews
        }
    }

    xhr.send()
}

let search = 'microsoft'

const xhr = new XMLHttpRequest();
xhr.open('GET', `https://newsapi.org/v2/everything?q=${search}&apiKey=${apiKey}`, true);

xhr.onload = function () {
    if (this.status === 200) {
        let news = JSON.parse(this.responseText)
        let articles = news.articles
        let latNews = ''
        let newsDiv = document.getElementById('newsDiv')
        articles.forEach(function (element, index) {
            latNews += `<div class="card mb-3" style="max-width: 540px;">
        <div class="row no-gutters">
          <div class="col-md-4">
            <img src="${element['urlToImage']}" class="card-img" alt="...">
          </div>
          <div class="col-md-8">
            <div class="card-body">
              <h5 class="card-title">${element['title']}</h5>
              <p class="card-text">${element["description"]}</p>
              <p class="card-text"><small class="text-muted">Published At ${element['publishedAt']}</small></p>
            </div>
          </div>
        </div>
      </div>
      `
        });
        newsDiv.innerHTML = latNews
    }
}

xhr.send()







