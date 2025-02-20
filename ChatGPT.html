<!DOCTYPE html>
<html lang="he">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ChatGPT - צ'אט בוט</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            text-align: center;
            margin: 0;
            padding: 0;
        }
        .chat-container {
            width: 90%;
            max-width: 400px;
            margin: 30px auto;
            background: white;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            overflow: hidden;
        }
        .chat-box {
            height: 400px;
            overflow-y: auto;
            padding: 15px;
            display: flex;
            flex-direction: column;
            background: #fff;
        }
        .chat-box div {
            margin: 5px 0;
            padding: 10px;
            border-radius: 5px;
            max-width: 75%;
        }
        .user {
            align-self: flex-end;
            background: #4CAF50;
            color: white;
        }
        .bot {
            align-self: flex-start;
            background: #ddd;
        }
        .input-container {
            display: flex;
            border-top: 1px solid #ccc;
            background: white;
            padding: 10px;
        }
        input {
            flex: 1;
            padding: 10px;
            border: none;
            border-radius: 5px;
            outline: none;
        }
        button {
            padding: 10px 15px;
            margin-left: 10px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <h1>ChatGPT - צ'אט בוט</h1>
    <div class="chat-container">
        <div class="chat-box" id="chat-box"></div>
        <div class="input-container">
            <input type="text" id="user-input" placeholder="הקלד הודעה...">
            <button onclick="sendMessage()">שלח</button>
        </div>
    </div>

    <script>
        const apiKey = "your-api-key-here";  // הכנס את ה-API Key שלך כאן
        
        async function sendMessage() {
            const userInput = document.getElementById('user-input').value;
            if (!userInput) return;
            
            const chatBox = document.getElementById('chat-box');
            chatBox.innerHTML += `<div class='user'>${userInput}</div>`;
            document.getElementById('user-input').value = '';
            chatBox.scrollTop = chatBox.scrollHeight;
            
            const response = await fetch('https://api.openai.com/v1/completions', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${apiKey}`,
                },
                body: JSON.stringify({
                    model: "text-davinci-003",
                    prompt: userInput,
                    max_tokens: 150,
                    temperature: 0.7,
                }),
            });
            
            const data = await response.json();
            const botResponse = data.choices[0].text.trim();
            chatBox.innerHTML += `<div class='bot'>${botResponse}</div>`;
            chatBox.scrollTop = chatBox.scrollHeight;
        }
    </script>
</body>
</html>
