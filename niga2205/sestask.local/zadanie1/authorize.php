<?php
session_start();

// Если уже заблокирован – возвращаем на форму
if (isset($_SESSION['blocked_until']) && time() < $_SESSION['blocked_until']) {
    header("Location: login.php");
    exit;
}

// Сброс блокировки, если время истекло
if (isset($_SESSION['blocked_until']) && time() >= $_SESSION['blocked_until']) {
    unset($_SESSION['blocked_until']);
    unset($_SESSION['login_attempts']);
}

// Инициализация счётчика
if (!isset($_SESSION['login_attempts'])) {
    $_SESSION['login_attempts'] = 0;
}

if (isset($_POST['Submit'])) {
    $login = trim($_POST['user_name'] ?? '');
    $pass  = trim($_POST['user_pass'] ?? '');
    
    // Правильные данные (в реальном проекте проверка через БД)
    $correct_login = "cleo";
    $correct_pass  = "password";
    
    // Увеличиваем счётчик
    $_SESSION['login_attempts']++;
    
    if ($login === $correct_login && $pass === $correct_pass) {
        // Успех
        $_SESSION['logged_user'] = $login;
        unset($_SESSION['login_attempts']);
        unset($_SESSION['blocked_until']);
        header("Location: secretplace.php");
        exit;
    } else {
        // Неудача
        if ($_SESSION['login_attempts'] >= 3) {
            // Блокировка на 60 секунд
            $_SESSION['blocked_until'] = time() + 60;
            $_SESSION['error_message'] = "❌ 3 неудачные попытки! Доступ заблокирован на 1 минуту.";
        } else {
            $left = 3 - $_SESSION['login_attempts'];
            $_SESSION['error_message'] = "❌ Неверный логин или пароль. Осталось попыток: {$left}";
        }
        header("Location: login.php");
        exit;
    }
} else {
    header("Location: login.php");
    exit;
}
?>