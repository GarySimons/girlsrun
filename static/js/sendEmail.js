function sendMail(contactForm) {
    debugger;
    emailjs.send("girls on the run","Run", {
        "from_name": contactForm.name.value,
        "from_email": contactForm.emailaddress.value,
        "message": contactForm.message.value,

    })
    .then(
        function(response) {
            console.log("SUCCESS", response);
            contactForm.name.value = ""
            contactForm.emailaddress.value = ""
            contactForm.message.value = ""
        },
        function(error) {
            console.log("FAILED", error);
        }
    );
    return false;  
}

// Submitting form

document.getElementById("btn-grey-contact").addEventListener("submit", myFunction);

function myFunction() {
  onsubmit="return sendMail(this)";
}