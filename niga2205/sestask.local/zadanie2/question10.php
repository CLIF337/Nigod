<?php
session_start();
$answer9 = $_POST['answer9'];
$_SESSION['answer9'] = $answer9;
?>
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Вопрос 10 из 10</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; min-height: 100vh; background: linear-gradient(135deg, #3a1c2d 0%, #1a0a12 100%); display: flex; justify-content: center; align-items: center; padding: 20px; }
        .card { background: #fff8f5; border-radius: 24px; padding: 35px; max-width: 650px; width: 100%; box-shadow: 0 20px 40px rgba(0,0,0,0.3); border-top: 8px solid #8b1a3a; }
        h2 { color: #5a1e2e; }
        .progress { background: #f0e2e6; border-radius: 20px; height: 12px; margin: 20px 0; overflow: hidden; }
        .progress-fill { background: #8b1a3a; width: 100%; height: 100%; border-radius: 20px; }
        .question { font-size: 22px; font-weight: 600; color: #2d1a22; margin: 25px 0 15px; }
        .option { background: white; border: 1px solid #e0c8cf; border-radius: 16px; padding: 12px 18px; margin: 10px 0; cursor: pointer; transition: 0.2s; }
        .option:hover { background: #f7eef1; border-color: #8b1a3a; }
        input[type="radio"] { margin-right: 12px; transform: scale(1.1); accent-color: #8b1a3a; }
        label { font-size: 17px; color: #2d1a22; font-weight: 500; cursor: pointer; }
        .btn { background: #8b1a3a; color: white; border: none; padding: 12px 28px; font-size: 18px; border-radius: 50px; cursor: pointer; margin-top: 25px; transition: 0.3s; font-weight: bold; }
        .btn:hover { background: #6e122d; }
    </style>
</head>
<body>
    <div class="card">
        <h2>📌 Вопрос 10 из 10</h2>
        <div class="progress"><div class="progress-fill" style="width: 100%;"></div></div>
        <div class="question">Для чего используется протокол OAuth 2.0?</div>
        <form action="result.php" method="post">
            <div class="option"><input type="radio" name="answer10" value="Для авторизации через сторонние сервисы" required> <label>Для авторизации через сторонние сервисы</label></div>
            <div class="option"><input type="radio" name="answer10" value="Для шифрования данных"> <label>Для шифрования данных</label></div>
            <div class="option"><input type="radio" name="answer10" value="Для ускорения загрузки сайта"> <label>Для ускорения загрузки сайта</label></div>
            <div class="option"><input type="radio" name="answer10" value="Для кэширования страниц"> <label>Для кэширования страниц</label></div>
            <button type="submit" class="btn">Завершить тест ✅</button>
        </form>
    </div>
</body>
</html>