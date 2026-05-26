<?php
session_start();
?>
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Авторизация - Задание 1</title>
    <style>
        body { font-family: Arial; margin: 50px; background: #f0f2f5; }
        .container { max-width: 400px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 0 20px rgba(0,0,0,0.1); }
        h2 { text-align: center; margin-bottom: 20px; color: #333; }
        label { display: block; margin: 10px 0 5px; }
        input { width: 100%; padding: 8px; margin-bottom: 10px; border: 1px solid #ddd; border-radius: 5px; }
        button { width: 100%; padding: 10px; background: #007bff; color: white; border: none; border-radius: 5px; cursor: pointer; font-size: 16px; }
        button:hover { background: #0056b3; }
        .error { background: #f8d7da; color: #721c24; padding: 10px; border-radius: 5px; margin-bottom: 15px; }
        .blocked { background: #fff3cd; color: #856404; padding: 10px; border-radius: 5px; margin-bottom: 15px; }
        .info { background: #e7f3ff; padding: 8px; border-radius: 5px; margin-top: 15px; font-size: 14px; text-align: center; }
    </style>
</head>
<body>
    <div class="container">
        <h2>🔐 Вход в систему</h2>
        
        <?php
        // Проверка блокировки
        if (isset($_SESSION['blocked_until']) && time() < $_SESSION['blocked_until']) {
            $remaining = $_SESSION['blocked_until'] - time();
if ($remaining >= 60) {
    $minutes = floor($remaining / 60);
    $seconds = $remaining % 60;
    echo "<div class='blocked'>⏰ БЛОКИРОВКА! Попробуйте через {$minutes} мин. {$seconds} сек.</div>";
} else {
    echo "<div class='blocked'>⏰ БЛОКИРОВКА! Попробуйте через {$remaining} секунд.</div>";
}
        } else {
            // Снимаем блокировку, если время истекло
            if (isset($_SESSION['blocked_until'])) {
                unset($_SESSION['blocked_until']);
                unset($_SESSION['login_attempts']);
            }
            
            // Сообщение об ошибке
            if (isset($_SESSION['error_message'])) {
                echo "<div class='error'>{$_SESSION['error_message']}</div>";
                unset($_SESSION['error_message']);
            }
            ?>
            
            <form action="authorize.php" method="post">
                <label>👤 Логин:</label>
                <input type="text" name="user_name" required placeholder="cleo">
                
                <label>🔒 Пароль:</label>
                <input type="password" name="user_pass" required placeholder="password">
                
                <button type="submit" name="Submit">Войти</button>
            </form>
            
            <?php
            // Показываем оставшиеся попытки
            if (isset($_SESSION['login_attempts']) && $_SESSION['login_attempts'] > 0) {
                $left = 3 - $_SESSION['login_attempts'];
                echo "<div class='info'>📊 Осталось попыток: {$left}</div>";
            }
            echo "<div class='info'>💡 Тестовые данные: cleo / password</div>";
        }
        ?>
    </div>
</body>
</html>