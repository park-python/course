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
    var artistID = message.data.artist;
    var capital = message.data.capital;
    var artist = $("#artist"+artistID);
    var num = artist.find(".number");
    num.text(capital);
    sort();
}

function sort() {
    var leaderBoard = $('#leaderboard');
    var artists = leaderBoard.find('li');

    artists.sort(function (a, b) {
        var numA = parseInt($(a).find('.number').text());
        var numB = parseInt($(b).find('.number').text());
        return (numA < numB) ? 1 : (numA > numB) ? -1 : 0;
    }).appendTo(leaderBoard);

    artists.each(function(index, elem) {
        $(elem).find(".list_num").text(index+1);
    });
}
