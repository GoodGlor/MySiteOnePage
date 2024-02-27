document.getElementById('buyNowButton').addEventListener('click', function(event) {
    event.preventDefault();
    document.getElementById('purchaseModal').style.display = 'block';
});

document.getElementsByClassName('close-button')[0].addEventListener('click', function() {
    document.getElementById('purchaseModal').style.display = 'none';
});

window.addEventListener('click', function(event) {
    var modal = document.getElementById('purchaseModal');
    if (event.target == modal) {
        modal.style.display = 'none';
    }
});

document.getElementById('purchaseForm').addEventListener('submit', function(event) {
    event.preventDefault(); 

    
    var formData = new FormData(event.target);
    
    
    var object = {};
    formData.forEach(function(value, key){
        object[key] = value;
    });

    
    var jsonData = JSON.stringify(object);

    fetch('/ajax/form_submission/', { 
        method: 'POST',
        body: formData, 
        headers: {

        },
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.message); 
        
        document.getElementById('purchaseModal').style.display = 'none';
    })
    .catch((error) => {
        console.error('Error:', error); 
    });
});