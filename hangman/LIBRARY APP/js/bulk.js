console.log('ok done')


let optArr1 = ['id', 'name', 'gender', 'address', 'email']
let optArr2 = ['phone', 'ipv4', 'ipv6', 'bank_acc_no', 'bank_name']
let optArr3 = ['bank_balance', 'net_banking_ID', 'net_banking_password', 'credit_card_no', 'credit_card_type']
let optArr4 = ['credit_card_expiry', 'credit_card_cvv', 'facebook', 'instagram', 'twitter']



optArr1.forEach(element => {
  let myDiv = document.getElementById('opt1')
  myDiv.innerHTML += `<td><div class="form-group form-check">
   <input type="checkbox" class="form-check-input" id="${element}">
   <label class="form-check-label" for="${element}">${element}</label>
   </div></td>`
});
optArr2.forEach(element => {
  let myDiv = document.getElementById('opt2')
  myDiv.innerHTML += `<td><div class="form-group form-check">
    <input type="checkbox" class="form-check-input" id="${element}">
    <label class="form-check-label" for="${element}">${element}</label>
    </div></td>`
});
optArr3.forEach(element => {
  let myDiv = document.getElementById('opt3')
  myDiv.innerHTML += `<td><div class="form-group form-check">
    <input type="checkbox" class="form-check-input" id="${element}">
    <label class="form-check-label" for="${element}">${element}</label>
    </div></td>`
});
optArr4.forEach(element => {
  let myDiv = document.getElementById('opt4')
  myDiv.innerHTML += `<td><div class="form-group form-check">
    <input type="checkbox" class="form-check-input" id="${element}">
    <label class="form-check-label" for="${element}">${element}</label>
    </div></td>`
});


let unSA = document.getElementById('unSelectAll')
unSA.addEventListener('click',unSelectAll)

function unSelectAll() {
  optArr1.forEach(function(element) {
    document.getElementById(element).checked = false
    // document.getElementById(element).removeAttribute('checked')
  })
  optArr2.forEach(function(element) {
    document.getElementById(element).checked = false
    // document.getElementById(element).removeAttribute('checked')
  })
  optArr3.forEach(function(element) {
    document.getElementById(element).checked = false
    // document.getElementById(element).removeAttribute('checked')
  })
  optArr4.forEach(function(element) {
    document.getElementById(element).checked = false
    // document.getElementById(element).removeAttribute('checked')
  })

}

let sA = document.getElementById('selectAll')
sA.addEventListener('click',selectAll)

function selectAll() {
  console.log('hi')
  optArr1.forEach(function(element) {
    document.getElementById(element).checked = true
    // document.getElementById(element).removeAttribute('checked')
  })
  optArr2.forEach(function(element) {
    document.getElementById(element).checked = true
    // document.getElementById(element).removeAttribute('checked')
  })
  optArr3.forEach(function(element) {
    document.getElementById(element).checked = true
    // document.getElementById(element).removeAttribute('checked')
  })
  optArr4.forEach(function(element) {
    document.getElementById(element).checked = true
    // document.getElementById(element).removeAttribute('checked')
  })

}


let sA4 = document.getElementById('selectRow4')
sA4.addEventListener('click',selectRow4)

function selectRow4(){
  optArr4.forEach(function(element) {
    document.getElementById(element).checked = true
    // document.getElementById(element).removeAttribute('checked')
  })
}

let sA1 = document.getElementById('selectRow1')
sA1.addEventListener('click',selectRow1)

function selectRow1(){
  optArr1.forEach(function(element) {
    document.getElementById(element).checked = true
    // document.getElementById(element).removeAttribute('checked')
  })
}

let sA2 = document.getElementById('selectRow2')
sA2.addEventListener('click',selectRow2)

function selectRow2(){
  optArr2.forEach(function(element) {
    document.getElementById(element).checked = true
    // document.getElementById(element).removeAttribute('checked')
  })
}

let sA3 = document.getElementById('selectRow3')
sA3.addEventListener('click',selectRow3)

function selectRow3(){
  optArr3.forEach(function(element) {
    document.getElementById(element).checked = true
    // document.getElementById(element).removeAttribute('checked')
  })
}




let rowBtn = document.getElementById('rowBtn')
rowBtn.addEventListener('click', function (event) {
  event.preventDefault();
  document.getElementById('error').innerHTML = ''
  let rowNo = document.getElementById('rowNo').value
  // console.log(rowNo)
  const xhr = new XMLHttpRequest();
  xhr.open('GET', `https://my.api.mockaroo.com/jsondata.json?key=3a88fc20`, true);

  xhr.onloadstart = function () {
    document.getElementById('loading').innerHTML = `<div class="spinner-grow text-primary" style="width: 3rem; height: 3rem;" role="status">
        <span class="sr-only">Loading...</span>
      </div>
      <div class="spinner-grow text-primary" style="width: 3rem; height: 3rem;" role="status">
        <span class="sr-only">Loading...</span>
      </div>
      <div class="spinner-grow text-primary" style="width: 3rem; height: 3rem;" role="status">
        <span class="sr-only">Loading...</span>
      </div>
      <div class="spinner-grow text-primary" style="width: 3rem; height: 3rem;" role="status">
        <span class="sr-only">Loading...</span>
      </div>
      <div class="spinner-grow text-primary" style="width: 3rem; height: 3rem;" role="status">
        <span class="sr-only">Loading...</span>
      </div>
      <div class="spinner-grow text-primary" style="width: 3rem; height: 3rem;" role="status">
        <span class="sr-only">Loading...</span>
      </div>
      <div class="spinner-grow text-primary" style="width: 3rem; height: 3rem;" role="status">
        <span class="sr-only">Loading...</span>
      </div>
      <div class="spinner-grow text-primary" style="width: 3rem; height: 3rem;" role="status">
        <span class="sr-only">Loading...</span>
      </div>
      <div class="spinner-grow text-primary" style="width: 3rem; height: 3rem;" role="status">
        <span class="sr-only">Loading...</span>
      </div>
      <div class="spinner-grow text-primary" style="width: 3rem; height: 3rem;" role="status">
        <span class="sr-only">Loading...</span>
      </div>
      <div class="spinner-grow text-primary" style="width: 3rem; height: 3rem;" role="status">
        <span class="sr-only">Loading...</span>
      </div>
      <div class="spinner-grow text-primary" style="width: 3rem; height: 3rem;" role="status">
        <span class="sr-only">Loading...</span>
      </div>`

  }
  xhr.onloadend = function () {
    document.getElementById('loading').innerHTML = ''
  }

  xhr.onload = function () {
    if (this.status === 200) {
      let bulkData = JSON.parse(this.responseText)
      // console.log(bulkData)
      let div = document.getElementById('bulkDisplay')
      let top = document.getElementById('top')
      top.innerHTML = ``
      div.innerHTML = ``
      if (Number(rowNo) <= 100) {
        for (let i = 0; i < Number(rowNo); i++) {
          const element = bulkData[i];
          let getDict = {
            'id': `${element.id}`,
            'name': `${element.name.first_name} ${element.name.last_name}`,
            'gender': `${element.gender}`,
            'address': `${element.address.city}, ${element.address.country}, ${element.address.zip}`,
            'email': `${element.email}`,
            'phone': `${element.phone}`,
            'ipv4': `${element.ip_address.v4}`,
            'ipv6': `${element.ip_address.v6}`,
            'bank_acc_no': `${element.bank.accNo}`,
            'bank_name': `${element.bank.name}`,
            'bank_balance': `${element.bank.balance}`,
            'net_banking_ID': `${element.bank.net_bank_id}`,
            'net_banking_password': `${element.bank.net_bank_pswd}`,
            'credit_card_no': `${element.bank.credit_card_no}`,
            'credit_card_type': `${element.bank.credit_card_type}`,
            'credit_card_expiry': `${element.bank.credit_card_exp}`,
            'credit_card_cvv': `${element.bank.credit_card_cvv}`,
            'facebook': `<a href="${element.social.facebook}">${element.social.facebook}`,
            'instagram': `<a href="${element.social.instagram}">${element.social.instagram}`,
            'twitter': `<a href="${element.social.twitter}">${element.social.twitter}`
          }
          // console.log(getDict)
          let mainHtml = ''
          let colHtml = ''
          // let sA = document.getElementById('selectAll')
          // if (sA.checked) {
          //   for (key in getDict) {
          //     let item = document.getElementById(key)
          //     item.checked = true
          //   }
          // }

          for (key in getDict) {
            let item = document.getElementById(key)
            if (item.checked) {
              mainHtml += `<td>${getDict[key]}</td>`
              colHtml += `<th scope="col">${key}</th>`
            }
          }
          // console.log(mainHtml)
          div.innerHTML += `
                    <tr>
                        ${mainHtml}
                    </tr>`
          top.innerHTML = colHtml
        }


      } else {
        document.getElementById('error').innerHTML = `<div class="alert alert-danger" role="alert">Number Of Rows Should Be Less than or eqauals to 100.</div>`
      }
    }
  }
  xhr.send()
})