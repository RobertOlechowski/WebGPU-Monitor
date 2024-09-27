let countdown = 3;
//const counterElement = document.getElementById('counter');
//counterElement.textContent = 'Next refresh in ' + countdown + ' seconds.';

setInterval(() => {
    countdown--;
    if (countdown <= 0) {
        countdown = 10;
        location.reload();
    }
    //counterElement.textContent = 'Next refresh in ' + countdown + ' seconds.';
}, 1000);