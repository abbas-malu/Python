

let bookArray;
let bookList = localStorage.getItem('bookList')
if (bookList == undefined) {
    bookArray = []
} else {
    bookArray = JSON.parse(bookList)
}

bookArray.forEach(element => {
    let bookdisplayarea = document.getElementById('displayArea')
    bookdisplayarea.innerHTML += `
              <tr id='${JSON.stringify(element)}' class='book'>
                <td id='name'>${element.name}</td>
                <td>By ${element.author}</td>
                <td>${element.booktype}</td>
                <td><button type="button" class="btn btn-primary" id='' onclick='delBook(${JSON.stringify(element)})'>Delete</button></td>
              </tr>`

})


let addBookForm = document.getElementById('addBookForm')

addBookForm.addEventListener('submit', addBook)

class book {
    constructor(id, name, author, booktype) {
        this.id = id
        this.name = name
        this.author = author
        this.booktype = booktype
    }
    display = function display() {
        let bookdisplayarea = document.getElementById('displayArea')
        bookdisplayarea.innerHTML += `
              <tr id='${JSON.stringify(this)}' class='book'>
                <td id='name'>${this.name}</td>
                <td>By ${this.author}</td>
                <td>${this.booktype}</td>
                <td><button type="button" class="btn btn-primary" id='' onclick='delBook(${JSON.stringify(this)})'>Delete</button></td
              </tr>`
        alert(`${this.name} by ${this.author}  Added Successfully`)
    }
}

function addBook(e) {
    let nameOfBook = document.getElementById('nameOfBook').value
    let nameOfAuthor = document.getElementById('nameOfAuthor').value
    let type;
    if (document.getElementById('fiction').checked) {
        type = document.getElementById('fiction').value
    } else if (document.getElementById('comedy').checked) {
        type = document.getElementById('comedy').value
    } else if (document.getElementById('encyclopedia').checked) {
        type = document.getElementById('encyclopedia').value
    } else if (document.getElementById('sciFi').checked) {
        type = document.getElementById('sciFi').value
    }
    let bookMain = new book(bookArray.length + 1, nameOfBook, nameOfAuthor, type)
    bookMain.display()
    bookArray.push(bookMain)
    e.preventDefault()
    addBookForm.reset()
    localStorage.setItem('bookList', JSON.stringify(bookArray))
}

function showalert() {
    document.getElementById('alert').innerHTML = `<div class="alert alert-success" role="alert">
    Book Successfully Added.
    </div>`
}


function delBook(bookDel) {
    
    let delBookCol = document.getElementById(JSON.stringify(bookDel))
    let displayArea = document.getElementById('displayArea')
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

document.getElementById('searchIn').addEventListener('input', function () {
    let searchVal = document.getElementById('searchIn').value
    let val2 = document.getElementsByClassName('book') 
    for(let i = 0; i<val2.length ; i++){
        let element = val2[i]
        let idget = element.getAttribute('id')
        let val = element.children[0].innerText.toLowerCase()
        
        if (val.includes(searchVal.toLowerCase())) {
            element.style.display = ''
        } 
        else {
            element.style.display = 'none'
        }
    }
})

