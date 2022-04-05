
function signonfunc(event){
    const firstname = document.getElementById("firstname").value;
    console.log("firstname: ", firstname);
    const middlename = document.getElementById("middlename").value;
    console.log("middlename: ", middlename);
    const lastname = document.getElementById("lastname").value;
    console.log("lasstname: ", lastname);
    const username = document.getElementById("username").value;
    console.log("username: ", username);
    const password = document.getElementById("password").value;
    console.log("password: ", password);
    const email = document.getElementById("email").value;
    console.log("email: ", email);
    const gender = document.getElementById("gender").value;
    console.log("gender: ", gender);
    const dob = document.getElementById("dob").value;
    console.log("dob: ", dob);

    // sqlstr = "insert table user(userfirstname, ,,,) values (firstname,,,)"
    // database.connect(ip, port,usrname, pwd)
    // database.exe(sqlstr)
    
    event.preventDefault(); // avoid refreshing
}

const signonform = document.getElementById('signonform');
signonform.addEventListener("submit", signonfunc);

