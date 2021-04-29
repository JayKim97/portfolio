(function (document, window, index) {
  var inputs = document.querySelectorAll(".inputfile");
  Array.prototype.forEach.call(inputs, function (input) {
    var label = input.nextElementSibling,
      labelVal = label.innerHTML;

    input.addEventListener("change", function (e) {
      var fileName = "";
      if (this.files && this.files.length > 1)
        fileName = (this.getAttribute("data-multiple-caption") || "").replace(
          "{count}",
          this.files.length
        );
      else fileName = e.target.value.split("\\").pop();

      if (fileName) label.querySelector("span").innerHTML = fileName;
      else label.innerHTML = labelVal;
    });

    // Firefox bug fix
    input.addEventListener("focus", function () {
      input.classList.add("has-focus");
    });
    input.addEventListener("blur", function () {
      input.classList.remove("has-focus");
    });
  });
})(document, window, 0);

document.getElementById("file-3").addEventListener("change", (event) => {
  var input = document.getElementById("file-3");
  input.nextElementSibling.style.color = "black";
});

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

function loadStart() {
  var one = document.getElementById("one");
  var two = document.getElementById("two");
  two.style.width = window.getComputedStyle(one).getPropertyValue("width");
  console.log("WORKED?");
}

function checkEmpty() {
  var img = document.getElementById("file-3");

  if (img.value.length !== 0) {
    var but = document.getElementById("inbutton");
    but.classList.remove("disabled");
    but.classList.add("enabled");
  } else {
    but.classList.remove("enabled");
    but.classList.add("disabled");
  }
}

document.onload = loadStart();
