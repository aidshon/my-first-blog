function register() { 
  var user=document.getElementById("user").value;
  var email=document.getElementById("e-mail").value;
  var pass=document.getElementById("pass").value;
  var confirm=document.getElementById("confirm").value;
  if (user.match(/[A-Z]{1}[a-z][0-9]{2}/i)) {
    document.getElementById("check-mark").style.display="inline";
  }
  else if (user=="") {
    $(".required-username").css({
      color: 'red'
    });
  }
  else {
    document.getElementById("wrong-mark").style.display="inline";
  }

  if (email.match(/^([A-Za-z0-9_\-\.]){1,}\@([A-Za-z0-9_\-\.]){1,}\.([A-Za-z]{2,4})$/)) {
    document.getElementById("check-mark1").style.display="inline";
  }
  else if (email=="") {
    $(".required-email").css({
      color: 'red'
    });
  }
  else {
    document.getElementById("wrong-mark1").style.display="inline";
  }

  if (pass.match(/[A-Z][a-z][0-9]/i)) {
    document.getElementById("check-mark2").style.display="inline";
  }
  else if (pass=="") {
    $(".required-password").css({
      color: 'red'
    });
  }
  else {
    document.getElementById("wrong-mark2").style.display="inline";
  }

  if (pass!==confirm) {
    document.getElementById("wrong-mark3").style.display="inline";
  }
  else {
    document.getElementById("check-mark3").style.display="inline";
  }

  if (user.match(/[A-Z]{1}[a-z][0-9]{2}/i) && email.match(/^([A-Za-z0-9_\-\.]){1,}\@([A-Za-z0-9_\-\.]){1,}\.([A-Za-z]{2,4})$/) && pass.match(/[A-Z][a-z][0-9]/i) && pass==confirm) {
    alert("You have successfully registered");
  }
}