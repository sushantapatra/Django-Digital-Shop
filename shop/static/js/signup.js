function validate(event) {
	console.log("form submited..");
	var error = document.getElementById("message");
	message = null;
	const values = event.target.elements;
	const name = values.name.value;
	const email = values.email.value;
	const phone = values.phone.value;
	const password = values.password.value;
    const repassword = values.repassword.value;
    const token = values.csrfmiddlewaretoken.value;

	if (!name.trim()) {
		message = "Name is Required.";
	} else if (!email.trim()) {
		message = "Email is Required.";
	} else if (!phone.trim()) {
		message = "Phone is Required.";
	} else if (!password.trim()) {
		message = "Password is Required.";
	} else if (!repassword.trim()) {
		message = "repassword is Required.";
	} else if (password.trim() != repassword.trim()) {
		message = "Password not matched";
	}
	if (message) {
		error.innerHTML = message;
		error.hidden = false;
	} else {
		error.innerHTML = "";
		error.hidden = true;
		//email sending
		//sendEmail(name, email,token);
	}
	// console.log({
	//     name,email,phone,password,repassword
	// })
	event.stopPropagation();
	return false;
}

async function sendEmail(name, email,token) {
	// $.ajax({
	// 	type: "POST",
	// 	url: "/send-otp",
	// 	data: { name: name, email: email,'csrfmiddlewaretoken':token },
	// }).done(function (msg) {
	// 	alert("data saved");
	// });
}
