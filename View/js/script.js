function afterLoad() {
    'use strict';
    var notificationsAmount = document.getElementById('notifications-amount').innerHTML;
    notificationsAmount = notificationsAmount.replace('(', '');
    notificationsAmount = notificationsAmount.replace(')', '');
    if (parseInt(notificationsAmount) > 0)
    {
        document.getElementById('btn-notification').style.color = "greenyellow";
    }

}

