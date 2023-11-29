document.getElementById('quoteButton').addEventListener('click', function() {
    document.getElementById('quoteModal').style.display = 'block';
});

document.getElementsByClassName('close')[0].addEventListener('click', function() {
    document.getElementById('quoteModal').style.display = 'none';
});

window.addEventListener('click', function(event) {
    if (event.target == document.getElementById('quoteModal')) {
        document.getElementById('quoteModal').style.display = 'none';
    }
});
