$(function () {
    var centrifuge = new Centrifuge({
        "url": "http://localhost:9000/connection/websocket",
        "insecure": true
    });
    centrifuge.subscribe("updates", function(message) {
        handleUpdate(message);
    });
    centrifuge.connect();
});

function handleUpdate(message) {
    console.log(message);
    var itemID = message.data.item;
    var value = message.data.value;
    var item = $("#item"+itemID);
    var num = item.find(".number");
    num.text(value);
    sort();
}

function sort() {
    var leaderBoard = $('#leaderboard');
    var items = leaderBoard.find('li');

    items.sort(function (a, b) {
        var numA = parseInt($(a).find('.number').text());
        var numB = parseInt($(b).find('.number').text());
        return (numA < numB) ? 1 : (numA > numB) ? -1 : 0;
    }).appendTo(leaderBoard);

    items.each(function(index, elem) {
        $(elem).find(".list_num").text(index+1);
    });
}
