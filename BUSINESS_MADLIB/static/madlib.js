function horseman(company){

  /*business_type =
  market_type =
  job_to_be_done =
  revenue_model =


  rv = company+" sells "+thing+ " because "+ verb + " " + thing + " is loved by customers in "+place;

  document.getElementById("output").innerHTML = rv;
  */



}




function saveMadLib(){

  business_type = document.getElementById("business_type").value;
  market_type = document.getElementById("market_type").value;
  job_to_be_done = document.getElementById("job_to_be_done").value;
  revenue_model = document.getElementById("revenue_model").value;

}

function queryDatabase(input_string){

  var request_string = "business_name="+input_string;

  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
     document.getElementById("output").innerHTML = this.responseText;
    }
  };
  xhttp.open("POST", "/company_data", true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.send(request_string);

}
