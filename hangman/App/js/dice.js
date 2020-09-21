console.log('Ok')



document.getElementById('tossBtn').addEventListener('click', function (){
    let a = Math.floor(Math.random() * (7 - 1) + 1)
    document.getElementById('diceImg').setAttribute('src',`/images/Dice-${a}.png`)
})


