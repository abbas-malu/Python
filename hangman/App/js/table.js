// // Getting Data From Local Storage

// let notesObj = {}
// let notesList = []
// notes = localStorage.getItem('notes')
// notesListTitle = localStorage.getItem('notesList')
// if (notes == undefined) {
//   notesObj = {}
//   notesList = []
// }
// else {
//   notesObj = JSON.parse(notes)
//   notesList = JSON.parse(notesListTitle)
// }


// // Adding New Notes
// document.getElementById('addBtn').addEventListener('click', function () {
//   if (document.getElementById('noteTxt').value != "" && document.getElementById('noteTitle').value != "") {
//     let addtxt = document.getElementById('noteTxt').value
//     let noteTitle = document.getElementById('noteTitle').value
//     notesObj[noteTitle.toLowerCase()] = addtxt.toLowerCase()
//     notesList.push(noteTitle.toLowerCase())
//     // document.getElementById('noteTxt').value = null
//     // document.getElementById('noteTitle').value = null
//     localStorage.setItem('notes', JSON.stringify(notesObj))
//     localStorage.setItem('notesList', JSON.stringify(notesList))
//     location.reload();

//   }
// })

// // Showing Notes In Html 
// shownotes();
// function shownotes() {
//   let htmltxt = ''
//   notesList.forEach(function (element, index) {
//     htmltxt += `
//     <div class="card mx-2 mt-2" style="width: 15rem;" id='${element}main'>
//     <div class="card-body">
//           <h5 class="card-title">${element}</h5> 
//           <p class="card-text">${notesObj[element]}</p>
//           <button  class="btn btn-primary" id='${element}' onclick="deleteNote(this.id)">Delete Note</button>
//     </div>
//   </div>`
//     document.getElementById('noteCards').innerHTML = htmltxt
//   });
// }


// // Deleting Notes 
// function deleteNote(id) {
//   notesObj[id] = undefined
//   notesList.splice(notesList.indexOf(id),1)
//   localStorage.setItem('notes', JSON.stringify(notesObj))
//   localStorage.setItem('notesList', JSON.stringify(notesList))
//   location.reload();
// }


// // Search Query For Notes
// document.getElementById('searchIn').addEventListener('input', function () {
//   let searchVal = document.getElementById('searchIn').value
//   notesList.forEach(val => {
//     val = val
//     val2 = notesObj[val]
//     let idGet = val+'main'
//     if (val.includes(searchVal.toLowerCase()) || val2.includes(searchVal.toLowerCase())) {
//       document.getElementById(idGet).style.display = 'block'
//     }
//     else{
//       document.getElementById(idGet).style.display = 'none'
//     }
//   });
// })





document.getElementById('tabBtn').addEventListener('click', function () {
  if (document.getElementById('tabNo').value != "") {
    let t1 = ``
    let addtxt = parseInt(document.getElementById('tabNo').value)
    let tabTime = parseInt(document.getElementById('tabTime').value)
    for (let i = 1; i <= tabTime; i++) {
      t1 += `${addtxt} * ${i} = ${addtxt * i}`
      t1 += `
`
    }
    document.getElementById('noteTxt').setAttribute('rows', `${tabTime + 1}`)
    document.getElementById('noteTxt').value = t1
  }
})
