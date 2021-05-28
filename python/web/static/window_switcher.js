var socket = io();
socket.on('connect', function () {
    socket.emit('my event', {data: 'I\'m connected!'});
});

socket.on('message', function (data) {
    console.log("Message!")
    console.log(data)

    if ("window" in data) {
        location.href = "/page" + (data.window + 1);
    }
});
