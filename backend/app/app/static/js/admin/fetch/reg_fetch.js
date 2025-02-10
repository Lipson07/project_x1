async function  regaccept() {
    const firstName = document.getElementById('firstName').value;
    const lastName = document.getElementById('lastName').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
   
    const res = await fetch("http://195.161.114.61:8001", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ firstName, lastName, email, password})
    });
    data =await res.json();
    console.log(data);
    if (data.status == "ok") {
     
        localStorage.setItem('registrationData', JSON.stringify(data));

    }
    
}
document.querySelector(".button").addEventListener("click", regaccept);
