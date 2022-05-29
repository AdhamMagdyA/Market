email.onkeydown = function(e) {
    const regex = /^([\.\_a-zA-Z0-9]+)@([a-zA-Z]+)\.([a-zA-Z]){2,8}$/;
    const regexo = /^([\.\_a-zA-Z0-9]+)@([a-zA-Z]+)\.([a-zA-Z]){2,3}\.[a-zA-Z]{1,3}$/;
    if ( regexo.test(document.querySelector("#email input").value) || regex.test(document.querySelector("#email input").value) ) {
        document.querySelector("#email .guides").innerHTML = "Email is valid";
        document.querySelector("#email input").style.borderColor = "green";
        document.querySelector("#email .guides").style.color = "green";
    }else{
        document.querySelector("#email .guides").innerHTML = "Email is invalid";
        document.querySelector("#email input").style.borderColor = "red";
        document.querySelector("#email .guides").style.color = "red";
    }
}


emailVerification.onkeydown = function(e) {
    
        if ( document.querySelector("#emailVerification input").value == document.querySelector("#email input").value ) {
            document.querySelector("#emailVerification .guides").innerHTML = "Email is a match";
            document.querySelector("#emailVerification input").style.borderColor = "green";
            document.querySelector("#emailVerification .guides").style.color = "green";
        }else{
            document.querySelector("#emailVerification .guides").innerHTML = "Email does not match";
            document.querySelector("#emailVerification input").style.borderColor = "red";
            document.querySelector("#emailVerification .guides").style.color = "red";
        }
}

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
                //scroll to the email field
                window.scrollTo({
                    top: document.getElementById("email").offsetTop,
                    behavior: 'smooth'
                });
            }
            else
                myForm.submit();
        }
    }
});