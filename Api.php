<?php
// Comando para obtener información sobre los procesos y la memoria en sistemas Windows
$comando = 'tasklist';

// Ejecuta el comando y captura la salida
$resultado = shell_exec($comando);

// Imprime la salida del comando
echo "<pre>$resultado</pre>";
?>
