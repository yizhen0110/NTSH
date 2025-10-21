<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>讀書計畫</title>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;700&display=swap" rel="stylesheet">
    <style>
        * {
            box-sizing: border-box;
        }

        body {
            font-family: "Noto Sans TC", sans-serif;
            background: linear-gradient(to right, #e1f5fe, #f1f8e9);
            color: #333;
            margin: 0;
            padding: 0;
        }

        header {
            background-color: #2196f3;
            color: white;
            text-align: center;
            padding: 50px 20px 30px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.2);
        }

        header h1 {
            margin: 0;
            font-size: 2.8em;
            font-weight: 700;
        }

        header p {
            font-size: 1.2em;
            margin-top: 10px;
            opacity: 0.95;
        }

        main {
            max-width: 900px;
            margin: 50px auto;
            padding: 20px;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 30px;
        }

        .card {
            background-color: white;
            border-radius: 16px;
            padding: 25px 20px;
            box-shadow: 0 6px 20px rgba(0,0,0,0.1);
            text-align: center;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .card a {
            text-decoration: none;
            color: #2e7d32;
            font-weight: 700;
            font-size: 1.1em;
            display: block;
        }

        .card:hover {
            transform: translateY(-6px);
            box-shadow: 0 10px 25px rgba(0,0,0,0.15);
        }

        .card:hover a {
            color: #1b5e20;
        }

        footer {
            text-align: center;
            padding: 25px 15px;
            font-size: 0.9em;
            color: #777;
            margin-top: 60px;
        }

        @media (max-width: 600px) {
            header h1 {
                font-size: 2em;
            }

            .card a {
                font-size: 1em;
            }
        }
    </style>
</head>
<body>
    <header>
        <h1>我的讀書計畫</h1>
        <p>新北高中 30936 陳怡臻</p>
    </header>

    <main>
        <div class="card"><a href="/competition">🏆 競賽經驗</a></div>
        <div class="card"><a href="/activities">🎭 課外活動</a></div>
        <div class="card"><a href="/leadership">👑 幹部經驗</a></div>
        <div class="card"><a href="/club">🎯 社團經驗</a></div>
        <div class="card"><a href="/electives">📚 多元選修課程</a></div>
        <div class="card"><a href="/ai">🤖 AI 應用</a></div>
    </main>
