function preview_image(event) {
    var reader = new FileReader();
    const actualBtn = document.getElementById('actual-btn');
    
const fileChosen = document.getElementById('file-chosen');
    reader.onload = function(){
      var output = document.getElementById('output_image');
      output.src = reader.result;
    }
    reader.readAsDataURL(event.target.files[0]);
  }