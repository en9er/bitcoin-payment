window.onload = ()=>
{
    loaded()
}


function loaded()
{
    let send_btn = document.getElementById('send_btn').addEventListener('click', send)
    let receive_btn = document.getElementById('receive_btn').addEventListener('click', receive)
}

function send()
{
    console.log('send')
}

function receive()
{
    console.log('receive')
}