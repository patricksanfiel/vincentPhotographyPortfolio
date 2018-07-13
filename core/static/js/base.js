window.onload = function(){
    document.getElementById('hamburgerIcon').addEventListener("click", function(){
      var x = document.getElementById("navToplevelDiv");
      if (x.className === "row topnav") {
        x.className += " responsive";
      } else {
        x.className = "row topnav";
      }
    }
  );

  // var navAnchors = document.getElementsByClassName("navAnchor");
  //
  // for (var i = 0; i < navAnchors.length; i++) {
  //   navAnchors[i].addEventListener("click", function(){
  //     let current =
  //     document.getElementsByClassName("active");
  //     current[0].className = current[0].className.replace("active", " ");
  //     this.className += " active";
  //   });
  // }
}
