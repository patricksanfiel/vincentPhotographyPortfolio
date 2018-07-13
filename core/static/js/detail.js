    document.getElementById('sizeToggleButton').innerHTML = "MAKE IT BIGGER";
    document.getElementById('sizeToggleButton').addEventListener("click", function(){
      let photo = document.getElementById("detailForPhoto");
      let button = document.getElementById("sizeToggleButton");
      if (photo.className === "col-12") {
        // x.classList.toggle("col-12 ");
        photo.className = "fullSizePic";
        button.innerHTML = "make it smaller";
        button.className = "smallerButton";
      } else {
        photo.className = "col-12";
        button.innerHTML = "MAKE IT BIGGER";
        button.className = "col-11"
      }
    }
  );
