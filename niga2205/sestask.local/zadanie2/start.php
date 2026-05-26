<?php
session_start();
session_destroy(); // очищаем старые ответы
session_start();
?>
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Тест: Программирование в КС</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            min-height: 100vh;
            background: linear-gradient(135deg, #3a1c2d 0%, #1a0a12 100%);
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        .card {
            background: #fff8f5;
            border-radius: 24px;
            padding: 40px;
            max-width: 600px;
            width: 100%;
            box-shadow: 0 20px 40px rgba(0,0,0,0.3);
            text-align: center;
            border-top: 8px solid #8b1a3a;
        }
        h1 {
            color: #5a1e2e;
            margin-bottom: 20px;
            font-size: 32px;
        }
        p {
            color: #333;
            font-size: 18px;
            line-height: 1.5;
            margin: 20px 0;
        }
        .btn {
            display: inline-block;
            background: #8b1a3a;
            color: white;
            padding: 12px 32px;
            font-size: 18px;
            border: none;
            border-radius: 50px;
            cursor: pointer;
            text-decoration: none;
            transition: 0.3s;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }
        .btn:hover {
            background: #6e122d;
            transform: scale(1.02);
        }
        .badge {
            background: #f0e2e6;
            display: inline-block;
            padding: 6px 14px;
            border-radius: 50px;
            color: #8b1a3a;
            font-weight: bold;
            margin-bottom: 20px;
        }
    </style>
</head>
<body>
    <div class="card">
        <div class="badge">📚 Знание языков программирования и веб-технологий</div>
        <h1>🧠 Тест по программированию в компьютерных сетях</h1>
        <p>Вас ждёт 10 вопросов. Каждый ответ сохраняется в сессии.<br>После последнего вопроса вы увидите результат и оценку.</p>
        <a href="question1.php" class="btn">🚀 Начать тест →</a>
    </div>
</body>
</html>