// function loadDoc() {
//     var numplate = document.getElementById("x").innerHTML
//               console.log("API Initiated")
//               var xhttp = new XMLHttpRequest();
//               console.log("getting Details...")
//               console.log(numplate)
//               xhttp.open("GET", `https://www.regcheck.org.uk/api/reg.asmx/CheckIndia?RegistrationNumber=${numplate}&username=<username>`, false);
//               xhttp.onreadystatechange = function () {
//                       if (xhttp.readyState == 4 && xhttp.status == 200)
//                       {
//                           var doc = xhttp.responseXML;
//                           var jsondoc = doc.getElementsByTagName("Vehicle")[0].getElementsByTagName("vehicleJson")[0].firstChild.nodeValue;
//                           obj = JSON.parse(jsondoc)
//                           // putting the value to html element
//                           document.getElementById("desc").innerHTML=obj.Description
//                           document.getElementById("regdate").innerHTML=obj.RegistrationDate
//                           document.getElementById("engno").innerHTML=obj.EngineNumber
//                           document.getElementById("owner").innerHTML=obj.Owner
//                           document.getElementById("insurance").innerHTML=obj.Insurance
//                           document.getElementById("variant").innerHTML=obj.Variant
//                           img_fun(obj.ImageUrl)
//                       }
//                   };
//                   xhttp.send(null);
//               }

function op() {

    document.getElementById("desc").innerHTML="Description";
    document.getElementById("regdate").innerHTML="RegistrationDate"
    document.getElementById("engno").innerHTML="EngineNumber"
    document.getElementById("owner").innerHTML="Owner"
    document.getElementById("insurance").innerHTML="Insurance"
    document.getElementById("variant").innerHTML="Variant"
}