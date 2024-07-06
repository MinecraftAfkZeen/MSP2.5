function keepAlive() {
    setInterval(function() {
        console.log('Mi codespace sigue activo...');
    }, 5000); // 5000 milisegundos = 5 segundos
}

keepAlive();
