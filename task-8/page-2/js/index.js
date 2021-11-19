function mySave() {
  localStorage.setItem("city", "Noida");
  document.getElementById("result").innerHTML = localStorage.getItem("city");
}

function show_now() {
  const my_time = new Date();
  alert(my_time.toLocaleDateString() + " " + my_time.toLocaleTimeString());
}

function myFunction() {
  document.body.style.background = "green";
}

function refreshPage() {
  location.reload();
}

function openNewWindow() {
  window.open("https://www.w3schools.com", "_blank");
}

function spamConsole() {
  while (true) {
    console.log("I did it");
  }
}

function nextButton() {
  window.location.href = "../page-3/chart.html";
}
