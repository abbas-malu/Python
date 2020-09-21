let bookList = localStorage.getItem('bookList')
let bookArray = JSON.parse(bookList)

function showBooks(type) {
    let bookdisplayarea = document.getElementById('mainDiv')
    bookdisplayarea.innerHTML = ``
    bookArray.forEach(element => {
        if (element.booktype==type){
            bookdisplayarea.innerHTML += `
                <tr id='${JSON.stringify(element)}' class='book'>
                    <td id='name'>${element.name}</td>
                    <td>By ${element.author}</td>
                    <td>${element.booktype}</td>
                    <td><button type="button" class="btn btn-primary" id='' onclick='delBook(${JSON.stringify(element)})'>Delete</button></td>
                </tr>`
        }
    let genreBtn = document.getElementById('genreBtn')
    genreBtn.innerText = type
    });
}


function delBook(bookDel) {
    
    let delBookCol = document.getElementById(JSON.stringify(bookDel))
    let displayArea = document.getElementById('mainDiv')
    displayArea.removeChild(delBookCol)
    let bookid = bookArray.indexOf(JSON.stringify(bookDel))
    for (let index = 0; index < bookArray.length; index++) {
        const element = bookArray[index];
        if (JSON.stringify(element)==JSON.stringify(bookDel)){
            bookArray.splice(index, 1)
        }
        
    }
    localStorage.setItem('bookList', JSON.stringify(bookArray))
}
