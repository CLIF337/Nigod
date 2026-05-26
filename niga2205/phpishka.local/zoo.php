<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Результат поиска</title>
    <style>
        body { font-family: Arial; margin: 50px; }
        .result { margin-top: 20px; padding: 10px; border: 1px solid #ccc; }
        .found { background-color: #d4edda; color: #155724; }
        .not-found { background-color: #f8d7da; color: #721c24; }
        .back-link { margin-top: 20px; display: inline-block; }
    </style>
</head>
<body>
    <h2>Результат поиска</h2>

    <?php
    // ЗАРАНЕЕ ОПРЕДЕЛЁННЫЙ МАССИВ-ЗООПАРК (зверушка => кличка)
    $zoo = [
        "медведь" => "Миша",
        "лев" => "Симба",
        "жираф" => "Мельман",
        "слон" => "Дамбо",
        "тигр" => "Шерхан",
        "обезьяна" => "Чита",
        "попугай" => "Кеша",
        "пингвин" => "Лоло",
        "волк" => "Серый",
        "лиса" => "Алиса",
        "заяц" => "Степашка"
    ];

    // Получаем название зверушки из GET-запроса
    $animal = isset($_GET['animal']) ? mb_strtolower(trim($_GET['animal'])) : '';

    // Проверяем, содержится ли зверушка в массиве
    if ($animal === '') {
        echo '<div class="result not-found">❌ Вы не ввели название зверушки.</div>';
    } elseif (isset($zoo[$animal])) {
        // Если зверушка есть - извлекаем её кличку
        $nickname = $zoo[$animal];
        echo "<div class='result found'>
                ✅ Такая зверушка есть в нашем зоопарке!<br>
                🐾 Зверушка <strong>{$animal}</strong> по кличке <strong>{$nickname}</strong>.
              </div>";
    } else {
        // Если зверушки нет
        echo "<div class='result not-found'>
                ❌ К сожалению, зверушки <strong>{$animal}</strong> нет в нашем зоопарке.<br>
                📋 Доступные зверушки: " . implode(', ', array_keys($zoo)) . "
              </div>";
    }
    ?>

    <br>
    <a href="zoo.html" class="back-link">← Назад к поиску</a>
</body>
</html>