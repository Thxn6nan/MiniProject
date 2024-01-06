let lock = document.getElementById("lock");
	let password = document.getElementById("password");

	lock.onclick = function(){
		if(password.type == "password"){
			password.type = "text";
			lock.src = "<i class='bx bx-lock-open'></i>";
		}
		else {
			password.type = "password";
			lock.src = "<i class='bx bx-lock'></i>";
		}
	}
