const container_status = document.querySelector('.container-status');
const container_status_none = document.querySelector('.container-status-none');

 function check_status() {
        var req = new XMLHttpRequest();
        var statustext1 = document.getElementById('status_1');
        var statustext2 = document.getElementById('status_2');
        var statustext3 = document.getElementById('status_3');
        var statustext4 = document.getElementById('status_4');
        var statustext5 = document.getElementById('status_5');
        var statustextNone = document.getElementById('status_none');
        var tracknumber = document.getElementById('tracking-input').value;
        req.onload = function()

        { console.log(this.responseText);
          var response = JSON.parse(this.responseText);
          if(response.order_status && response.date_order_users) {
                statustext1.innerHTML = "№ накладной " + tracknumber;
                statustext2.innerHTML = "Статус груза: " + response.order_status;
                statustext3.innerHTML = "Статус оплаты: " + response.payment;
                statustext4.innerHTML = "Дата доставки: " + response.date_delivery;
                statustext5.innerHTML = "Направление: " + response.direction;
            container_status.classList.contains('open') ? container_status.classList.remove('open') : container_status.classList.add('open');
          } else {
            container_status_none.classList.contains('open-none') ? container_status_none.classList.remove('open-none') : container_status_none.classList.add('open-none');
          }
        }
        req.open('GET', '/tracking/status?' + "tracknumber=" + tracknumber, true);
        req.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8');
        req.send();

      };