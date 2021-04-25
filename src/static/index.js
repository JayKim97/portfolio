function loadStart() {
  var one = document.getElementById("one");
  var two = document.getElementById("two");
  two.style.width = window.getComputedStyle(one).getPropertyValue("width");
  console.log("WORKED?");
}

function showEmail() {
  var email = document.getElementById("emaillink");
  email.style.display = "inline";
}

document.onload = loadStart();
