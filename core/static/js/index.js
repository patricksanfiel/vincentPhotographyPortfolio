document.getElementById('expandNav').innerHTML = "▼";
document.getElementById('expandNav').addEventListener("click", function(){
  // alert("hi");
  let topJumpTo = document.getElementById('topLevelJumpto');
  let bottomJumpTo = document.getElementById('bottomLevelJumpTo');
  let toggleButton = document.getElementById('expandNav');
  if (topJumpTo.style.display === 'block') {
    topJumpTo.style.display = 'none';
    bottomJumpTo.style.display = 'none';
    toggleButton.innerHTML = "▼";
  } else {
    topJumpTo.style.display = 'block';
    bottomJumpTo.style.display = 'block';
    toggleButton.innerHTML = "▲";
  }
});
