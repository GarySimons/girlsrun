// Hide 'email-sent' messaage
$(document).ready(function () {
                    $('#email-sent').hide();
                });

// Send email from form
function sendMail(contactForm) {
    emailjs.send("girls on the run", "Run", {
        "from_name": contactForm.name.value,
        "from_email": contactForm.emailaddress.value,
        "message": contactForm.message.value,

    })
        .then(
            function (response) {
                console.log("SUCCESS", response);
                contactForm.name.value = ""
                contactForm.emailaddress.value = ""
                contactForm.message.value = ""

                // show message when form sent
                $(document).ready(function () {
                    $('#email-sent').show();
                });


            },
            function (error) {
                console.log("FAILED", error);
            }
        );
    return false;
}