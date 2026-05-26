<?php
session_start();
if (!isset($_SESSION['logged_user'])) {
    header("Location: login.php");
    exit;
}
?>
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Секретная страница</title>
    <style>
        body { font-family: Arial; margin: 50px; background: #f0f2f5; }
        .container { max-width: 500px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; text-align: center; }
        .secret { background: #d4edda; padding: 20px; border-radius: 10px; margin: 20px 0; }
        .logout { background: #dc3545; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; display: inline-block; }
        .logout:hover { background: #c82333; }
    </style>
</head>
<body>
    <div class="container">
        <h2>🎉 Добро пожаловать!</h2>
        <div class="secret">
            <p>✅ Вы успешно авторизовались.</p>
            <p>👤 Пользователь: <strong><?php echo htmlspecialchars($_SESSION['logged_user']); ?></strong></p>
            <p>🆔 ID сессии: <code><?php echo session_id(); ?></code></p>
        </div>
        <a href="logout.php" class="logout">🚪 Выйти</a>
    </div>
</body>
</html>