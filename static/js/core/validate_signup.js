document.getElementById('signup').addEventListener('submit', function(e){
    e.preventDefault();
    // prepare form data
    var form = document.getElementById('signup');
    var formData = new FormData(form);
    // create ajax request
    var xhr = new XMLHttpRequest();
    // set the request method
    xhr.open('POST', 'ajax-validation' );
    // send the request
    xhr.send(formData);
    // listen for the response
    xhr.onreadystatechange = function(){
        // what happens when getting a response
        if(xhr.readyState == 4 && xhr.status == 200){
            var response = JSON.parse(xhr.responseText);
            myForm = document.getElementById('signup');
            if(response.exists){
                myForm.querySelector("#email .guides").innerHTML = "Email already exists";
                myForm.querySelector("#email input").style.borderColor = "red";
                myForm.querySelector("#email .guides").style.color = "red";
            }
            else
                myForm.submit();
        }
    }
});