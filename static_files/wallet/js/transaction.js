let text;
let copy_btn;
window.onload = ()=>
{
    loaded()
}


function loaded()
{
    text = document.getElementById("wallet_address").innerHTML;
    copy_btn = document.getElementById("copy_text").addEventListener('click', copy);
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

function copy()
{
    const el = document.createElement('textarea');
    el.value = text;
    el.setAttribute('readonly', '');
    el.style.position = 'absolute';
    el.style.left = '-9999px';
    document.body.appendChild(el);
    el.select();
    document.execCommand('copy');
    document.body.removeChild(el);
}