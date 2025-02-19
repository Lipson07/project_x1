
async function  regaccept() {
  
   
    const res = await fetch("http://localhost:8080/admin/database_schema");
    data =await res.json();
    console.log(data);
    let a=Object.keys(data)
    for(let i=0;i<a.length;i++){
       
        let namedb=a[i];
        let db=data[namedb].length;
        let bd_size="-";
        let active="-";
        let table=document.querySelector(".table");
        let sidebar=document.querySelector(".sidebar");
        if(i<5){
        table.innerHTML+="<tr><td>"+namedb+"</td><td>"+db+"</td><td>"+bd_size+"</td><td>"+active+"<td><button class='btn btn-success'>Изменить</button><button class='btn btn-danger'>Удалить</button></td>"+"</tr>";
        }
       waitForButtonClick('.page-btn1').then(() => {
        s=5;
        
        let namedb1=a[i+s];
        console.log(i);
        let db1=data[namedb].length;
        if(i<5){
            table.innerHTML+="<tr><td>"+namedb1+"</td><td>"+db1+"</td><td>"+bd_size+"</td><td>"+active+"<td><button class='btn btn-success'>Изменить</button><button class='btn btn-danger'>Удалить</button></td>"+"</tr>";
        }
       
       })
        sidebar.innerHTML+="<a href='#' class='nav-item'>"+namedb+"</a>";
        console.log(namedb,db,bd_size,active);
   }
 
  
     
  
    
    
}
async function waitForButtonClick(buttonSelector) {
    return new Promise(resolve => {
      const button = document.querySelector(buttonSelector);
  
      if (!button) {
        throw new Error(`Button with selector "${buttonSelector}" not found.`);
      }
      
      button.addEventListener('click', () => {
        document.querySelector(".table").innerHTML = "";
        setTimeout(() => {
            resolve();
        }, 100);
        
      }, { once: true }); 
    });
  }
  
document.addEventListener("DOMContentLoaded", function() {
    regaccept();
  });
