<?php
session_start();
$answer10 = $_POST['answer10'];
$_SESSION['answer10'] = $answer10;

$correct = [
    1 => 'HyperText Transfer Protocol',
    2 => 'GET',
    3 => 'На сервере',
    4 => 'Внедрение вредоносного JavaScript-кода',
    5 => 'Использовать prepared statements',
    6 => 'HttpOnly',
    7 => 'session_start()',
    8 => 'Подделка межсайтового запроса',
    9 => 'JSON Web Token',
    10 => 'Для авторизации через сторонние сервисы'
];

$score = 0;
for ($i = 1; $i <= 10; $i++) {
    if (isset($_SESSION["answer$i"]) && $_SESSION["answer$i"] == $correct[$i]) {
        $score++;
    }
}
$percent = round(($score / 10) * 100);
if ($percent >= 90) $grade = 5;
elseif ($percent >= 75) $grade = 4;
elseif ($percent >= 60) $grade = 3;
else $grade = 2;
?>
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Результаты теста</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            min-height: 100vh;
            background: linear-gradient(135deg, #3a1c2d 0%, #1a0a12 100%);
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 30px 20px;
        }
        .card {
            background: #fff8f5;
            border-radius: 28px;
            padding: 30px;
            max-width: 950px;
            width: 100%;
            box-shadow: 0 25px 45px rgba(0,0,0,0.3);
            border-top: 8px solid #8b1a3a;
        }
        h2 { color: #5a1e2e; text-align: center; margin-bottom: 15px; }
        .result-score {
            background: #f2e6ea;
            padding: 20px;
            border-radius: 20px;
            text-align: center;
            margin-bottom: 30px;
        }
        .score-number { font-size: 48px; font-weight: bold; color: #8b1a3a; }
        .grade {
            display: inline-block;
            background: #8b1a3a;
            color: white;
            padding: 8px 24px;
            border-radius: 40px;
            font-size: 28px;
            font-weight: bold;
            margin-top: 10px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            background: white;
            border-radius: 20px;
            overflow: hidden;
            box-shadow: 0 5px 10px rgba(0,0,0,0.05);
        }
        th {
            background: #5a1e2e;
            color: white;
            padding: 12px;
            font-weight: 600;
        }
        td {
            border-bottom: 1px solid #f0dbe1;
            padding: 10px 12px;
            color: #2d1a22;
        }
        .correct-row { background: #e8f5e9; }
        .wrong-row { background: #ffebee; }
        .restart-btn {
            display: inline-block;
            background: #8b1a3a;
            color: white;
            text-decoration: none;
            padding: 12px 28px;
            border-radius: 50px;
            margin-top: 30px;
            font-weight: bold;
            transition: 0.3s;
        }
        .restart-btn:hover { background: #6e122d; transform: scale(1.02); }
        .footer { text-align: center; }
    </style>
</head>
<body>
    <div class="card">
        <h2>📊 Результаты тестирования</h2>
        <div class="result-score">
            <div class="score-number"><?php echo $score; ?> из 10</div>
            <div style="font-size: 18px; margin: 8px 0;">(<?php echo $percent; ?>%)</div>
            <div class="grade">Оценка: <?php echo $grade; ?></div>
        </div>

        <table>
            <thead>
                <tr><th>№</th><th>Ваш ответ</th><th>Правильный ответ</th><th>Результат</th></tr>
            </thead>
            <tbody>
                <?php for ($i = 1; $i <= 10; $i++):
                    $user = $_SESSION["answer$i"] ?? '—';
                    $isCorrect = ($user == $correct[$i]);
                    $rowClass = $isCorrect ? 'correct-row' : 'wrong-row';
                ?>
                <tr class="<?php echo $rowClass; ?>">
                    <td><strong><?php echo $i; ?></strong></td>
                    <td><?php echo htmlspecialchars($user); ?></td>
                    <td><?php echo $correct[$i]; ?></td>
                    <td><?php echo $isCorrect ? '✓' : '✗'; ?></td>
                </tr>
                <?php endfor; ?>
            </tbody>
        </table>
        <div class="footer">
            <a href="start.php" class="restart-btn">🔄 Пройти тест заново</a>
        </div>
    </div>
</body>
</html>