function afterLoad() {
	'use strict';

	//Уведомления
	//Смена цвета на зеленоватый, если уведомлений больше 0
	var notificationsAmount = document.getElementById('notifications-amount').innerHTML;
	notificationsAmount = notificationsAmount.replace('(', '');
	notificationsAmount = notificationsAmount.replace(')', '');
	if (parseInt(notificationsAmount) > 0) {
		document.getElementById('btn-notification').style.color = "greenyellow";
	}
	//


	//Смена цвета кнопок управления после загрузки страницы
	var switchers = document.getElementsByClassName("switch-button");
	for (var i = 0; i < switchers.length; i++) {
		if (switchers[i].innerHTML === "Включено") {
			switchers[i].style.backgroundColor = "lightgreen";
		}
	}
	//
}


function switchPressed(num) {
	/*
	 TO-DO
	 Отправка запроса на сервер

	 */
	var switcher = document.getElementById("room-switcher" + num.toString());
	if (switcher.innerHTML === "Включено") {
		switcher.innerHTML = "Выключено";
		switcher.style.backgroundColor = "burlywood";
	}
	else {
		switcher.innerHTML = "Включено";
		switcher.style.backgroundColor = "lightgreen";
	}
}

function notificationsChecked() {
	/*
	 TO-DO
	 Отправка запроса на сервер

	 */
	document.getElementById('btn-notification').style.color = "#bbb";

	//$.ajax({
	//	url: '',
	//	type: 'GET',
	//	data: {},
	//	success: function (result) {
	//		//NOTIFICATION MANAGEMENT SHOULD BE HERE
	//	}
	//});

	$('#notificationWrapper').fadeIn();
	setInterval(function () {
		$('#notificationWrapper').fadeOut();
	}, 5000);
}