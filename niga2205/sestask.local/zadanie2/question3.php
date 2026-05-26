<?php
session_start();
$answer2 = $_POST['answer2'];
$_SESSION['answer2'] = $answer2;
?>
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Вопрос 3 из 10</title>
    <style>
        /* стиль как в question2.php, меняем ширину progress-fill на 30% */
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; min-height: 100vh; background: linear-gradient(135deg, #3a1c2d 0%, #1a0a12 100%); display: flex; justify-content: center; align-items: center; padding: 20px; }
        .card { background: #fff8f5; border-radius: 24px; padding: 35px; max-width: 650px; width: 100%; box-shadow: 0 20px 40px rgba(0,0,0,0.3); border-top: 8px solid #8b1a3a; }
        h2 { color: #5a1e2e; }
        .progress { background: #f0e2e6; border-radius: 20px; height: 12px; margin: 20px 0; overflow: hidden; }
        .progress-fill { background: #8b1a3a; width: 30%; height: 100%; border-radius: 20px; }
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
        <h2>📌 Вопрос 3 из 10</h2>
        <div class="progress"><div class="progress-fill" style="width: 30%;"></div></div>
        <div class="question">Где хранятся данные сессии?</div>
        <form action="question4.php" method="post">
            <div class="option"><input type="radio" name="answer3" value="На клиенте (в браузере)" required> <label>На клиенте (в браузере)</label></div>
            <div class="option"><input type="radio" name="answer3" value="На сервере"> <label>На сервере</label></div>
            <div class="option"><input type="radio" name="answer3" value="В базе данных клиента"> <label>В базе данных клиента</label></div>
            <div class="option"><input type="radio" name="answer3" value="В файле .htaccess"> <label>В файле .htaccess</label></div>
            <button type="submit" class="btn">Далее →</button>
        </form>
    </div>
</body>
</html>