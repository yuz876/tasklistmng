function signinfunc(event){

    const username = document.getElementById("username").value;
    console.log("username: ", username);

    const password = document.getElementById("password").value;
    console.log("password: ", password);


    event.preventDefault(); // avoid refreshing

}

const signinform = document.getElementById('signinform');
signinform.addEventListener("submit", signinfunc); 