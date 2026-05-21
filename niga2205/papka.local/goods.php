<?php
header('Content-Type: application/json');

$art = $_GET['art'] ?? '';

$catalog = [
    1 => [
        'name'   => 'Смартфон Galaxy S23',
        'weight' => '168 г',
        'cost'   => 69990,
        'img'    => 'tel.jpg'
    ],
    2 => [
        'name'   => 'Ноутбук MacBook Air',
        'weight' => '1.24 кг',
        'cost'   => 119990,
        'img'    => 'comp.jpg'
    ]
];

if (isset($catalog[$art])) {
    echo json_encode($catalog[$art]);
} else {
    http_response_code(400);
    echo json_encode(['error' => 'Артикул должен быть 1 или 2']);
}