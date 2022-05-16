function ValidateEmail(input) {

    var validRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
  
    if (input.value.match(validRegex)) {
  
  
      document.form1.userEmail.focus();
  
      return true;
  
    } else {
  
      alert("Invalid email address!");

  
      document.form1.userEmail.focus();
  
      return false;
  
    }
  
  }