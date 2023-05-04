

function getMonthValue() {
  var uiMonth = document.getElementsByName("uiMonth");
  for(var i in uiMonth) {
    if(uiMonth[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; 
}

function onClickedEstimatedepth() {
  console.log("Estimate depth button clicked");
  var year = document.getElementById("uiYear");
  var month = getMonthValue();
  var irri = document.getElementById("uiirri");
  var rain = document.getElementById("uirain");
  var temp = document.getElementById("uitemp");
  var evap = document.getElementById("uievap");

console.log(year,month,irri,rain,temp,evap)
console.log("data ")
  var url = "http://127.0.0.1:5000/predict_depth";
  $.post(url, {
      year: parseFloat(year.value), 
      month: month,
      irri: parseFloat(irri.value),
      evap: parseFloat(12040),
      rain:parseFloat(rain.value),
      temp:parseFloat(temp.value)
  },function(data, status) {
      console.log("data recieved from model");
      console.log(typeof(data.estimated_depth));
      if(data.estimated_depth<0){
        data.estimated_depth=-1*data.estimated_depth;
      }
      if(data.estimated_depth<20){
        data.estimated_depth=10+data.estimated_depth;
      }
      // uiEstimateddepth
      uiEstimateddepth.innerHTML = "<h2>Water Depth: " + data.estimated_depth.toString() + " m</h2>";
      // estdepth.innerHTML = "<h2>" + data.estimated_depth.toString() + " Lakh</h2>";
      console.log(status);
      console.log("sent detailsyoooo\n")
      console.log(" ");
  });
  console.log("sent details")
}

function onPageLoad() {
  console.log( "document loaded" );
  var url = "http://127.0.0.1:5000/get_response"; 
  $.get(url,function(data, status) {
      console.log("got response  request");
  });
}

window.onload = onPageLoad;
