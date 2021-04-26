function loadStart() {
  var one = document.getElementById("one");
  var two = document.getElementById("two");
  two.style.width = window.getComputedStyle(one).getPropertyValue("width");
  console.log("WORKED?");
}

function showEmail() {
  var email = document.getElementById("emaillink1");
  if (email.style.display === "inline") {
    email.style.animation = "animationgone 1s";
    setTimeout(() => (email.style.display = "none"), 1000);
  } else {
    email.style.display = "inline";
    email.style.animation = "animateleft 1s";
  }
}

function showEmail2() {
  var email = document.getElementById("emaillink2");
  if (email.style.display === "inline") {
    email.style.animation = "animationgone 1s";
    setTimeout(() => (email.style.display = "none"), 1000);
  } else {
    email.style.display = "inline";
    email.style.animation = "animateleft 1s";
  }
}

function activateMenu(num) {
  var childs = Array.from(document.getElementById("topnav").children);
  childs.forEach((element) => {
    element.classList.remove("active");
  });
  childs[num].classList.add("active");
}

document.onload = loadStart();
