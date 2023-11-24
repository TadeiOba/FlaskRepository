// static/script.js

var socket = io.connect('http://' + document.domain + ':' + location.port);

function updateData() {
    var newData = Math.random();  // Replace this with your data update logic
    socket.emit('update_data', newData);
}

socket.on('data_updated', function(data) {
    document.getElementById('display').innerText = 'Updated Data: ' + data.toFixed(4);
});
