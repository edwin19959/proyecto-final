<?php
header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json; charset=UTF-8");

// Configuración de la base de datos
$config = [
    'host' => 'localhost',
    'user' => 'root',
    'pass' => '',
    'db' => 'nuevaData'
];

// Conexión a la base de datos
$conexion = new mysqli($config['host'], $config['user'], $config['pass'], $config['db']);
$conexion->set_charset("utf8");

// Verificar la conexión
if ($conexion->connect_error) {
    die(json_encode([
        'status' => 'error',
        'message' => "Error de conexión: " . $conexion->connect_error
    ]));
}

// Obtener y mostrar los comentarios
$result = $conexion->query("SELECT nombre, comentario, fecha FROM comentarios ORDER BY fecha DESC");

$comentarios = [];
while ($row = $result->fetch_assoc()) {
    $comentarios[] = [
        'nombre' => htmlspecialchars($row['nombre']),
        'comentario' => htmlspecialchars($row['comentario']),
        'fecha' => $row['fecha']
    ];
}

echo json_encode(['status' => 'success', 'data' => $comentarios]);

// Cerrar la conexión
$conexion->close();
?>
