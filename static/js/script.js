function start_input_calc(param) {
   // console.log('click');

}

function focus_lost(param){
    //console.log('blur');
    //var current_item = document.getElementById(param);
//    if(current_item.value != ''){
//        //current_item.value = current_item.value + ' &sup3';
//    }
}
function calc_price(){

    var req = new XMLHttpRequest();
    var city1 = document.getElementById('cityfrom').value;
    var city2 = document.getElementById('cityto').value;
    var places = document.getElementById('places').value;
    var weight = document.getElementById('weight').value;
    var volume = document.getElementById('volume').value;
    var pick = document.getElementById('pick').checked;
    var deliver = document.getElementById('deliver').checked;
    //params.push(city1, city2, places, weight, volume, pick, deliver);


    json = city1 + "/" + city2 + "/" + places + "/" + weight + "/" + volume + "/" + pick + "/" + deliver;

    if(city1 != '' && city2 != '' && places != '' && weight != '' && volume != ''){
           req.onload = function(){

            var response = JSON.parse(this.responseText);
            if(response.price && response.timedeliver){
                //console.log(response.price);
                var st_price = document.getElementById('st_price');
                var st_time = document.getElementById('st_time');
                var ex_price = document.getElementById('ex_price');
                var ex_time = document.getElementById('ex_time');

                st_price.innerHTML = response.price + " р.";
                st_time.innerHTML = response.timedeliver;
                ex_price.innerHTML = response.price + " р.";
                ex_time.innerHTML = response.timedeliver;

            }

        }

            req.open('GET', '/calculate/calc?' + "params=" + json, true);
            req.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8');
            req.send();


    }

}

