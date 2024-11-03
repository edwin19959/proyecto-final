<?php
header('Content-Type: application/json');

// Configuración de la base de datos
$config = [
    'host' => 'localhost',
    'user' => 'root',
    'pass' => '',
    'db' => 'nuevaData'
];

try {
    // Validar método de solicitud
    if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
        throw new Exception('Método no permitido');
    }

    // Validar campos requeridos
    if (empty($_POST['nombre']) || empty($_POST['comentario'])) {
        throw new Exception('Todos los campos son requeridos');
    }

    // Validar longitud de los campos
    if (strlen($_POST['nombre']) > 100) {
        throw new Exception('El nombre es demasiado largo');
    }
    if (strlen($_POST['comentario']) > 500) {
        throw new Exception('El comentario es demasiado largo');
    }

    // Conectar a la base de datos
    $conexion = new mysqli($config['host'], $config['user'], $config['pass'], $config['db']);
    
    if ($conexion->connect_error) {
        throw new Exception("Error de conexión: " . $conexion->connect_error);
    }

    $conexion->set_charset("utf8mb4");

    // Preparar y ejecutar la consulta
    $stmt = $conexion->prepare("INSERT INTO comentarios (nombre, comentario) VALUES (?, ?)");
    
    if (!$stmt) {
        throw new Exception("Error en la preparación de la consulta");
    }

    // Sanitizar y vincular parámetros
    $nombre = filter_var($_POST['nombre'], FILTER_SANITIZE_STRING);
    $comentario = filter_var($_POST['comentario'], FILTER_SANITIZE_STRING);
    $stmt->bind_param("ss", $nombre, $comentario);

    // Ejecutar la consulta
    if (!$stmt->execute()) {
        throw new Exception("Error al guardar el comentario");
    }

    echo json_encode([
        'status' => 'success',
        'message' => 'Comentario guardado correctamente',
        'id' => $conexion->insert_id
    ]);

} catch (Exception $e) {
    http_response_code(500);
    echo json_encode([
        'status' => 'error',
        'message' => $e->getMessage()
    ]);

} finally {
    // Cerrar conexiones
    if (isset($stmt)) $stmt->close();
    if (isset($conexion)) $conexion->close();
}
?>
