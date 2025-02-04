async function  a() {
    const firstName = document.getElementById('firstName').value;
    const lastName = document.getElementById('lastName').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
   
    const res = await fetch("http://127.0.0.1:8000", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ firstName, lastName, email, password})
    });
    data =await res.json();
    console.log(data);
    if (data.status == "ok") {
     
        localStorage.setItem('registrationData', JSON.stringify(data));
        window.location.href = "/";
    }
    
}
document.querySelector(".button").addEventListener("click", a);