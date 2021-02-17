$(window).ready(function() {
    var socket = io();
    socket.on("connect", function() {
        console.log("If you're seeing this message, you've successfully connected to the server.")
    })

    socket.on("message", function(msg) {
        console.log(msg)
    })

    socket.on("test", function(msg) {
        console.log(msg)
    })
})