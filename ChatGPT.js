// צ'אט רוט - הכל ב-JavaScript בלבד!
const API_KEY = "your-api-key-here";  // 🔴 הכנס את ה-API Key שלך כאן!

// יצירת אלמנטים דינמיים
const body = document.body;
body.style.fontFamily = "Arial, sans-serif";
body.style.textAlign = "center";
body.style.backgroundColor = "#f0f0f0";
body.style.margin = "0";
body.style.padding = "0";

// כותרת הצ'אט
const title = document.createElement("h1");
title.innerText = "צ'אט רוט";
body.appendChild(title);

// יצירת הקונטיינר של הצ'אט
const chatContainer = document.createElement("div");
chatContainer.style.width = "90%";
chatContainer.style.maxWidth = "400px";
chatContainer.style.margin = "30px auto";
chatContainer.style.background = "white";
chatContainer.style.borderRadius = "10px";
chatContainer.style.boxShadow = "0 4px 8px rgba(0, 0, 0, 0.2)";
chatContainer.style.overflow = "hidden";
body.appendChild(chatContainer);

// תיבת הצ'אט
const chatBox = document.createElement("div");
chatBox.style.height = "400px";
chatBox.style.overflowY = "auto";
chatBox.style.padding = "15px";
chatBox.style.display = "flex";
chatBox.style.flexDirection = "column";
chatBox.style.background = "#fff";
chatContainer.appendChild(chatBox);

// אזור ההזנה
const inputContainer = document.createElement("div");
inputContainer.style.display = "flex";
inputContainer.style.borderTop = "1px solid #ccc";
inputContainer.style.background = "white";
inputContainer.style.padding = "10px";
chatContainer.appendChild(inputContainer);

// שדה הטקסט
const userInput = document.createElement("input");
userInput.type = "text";
userInput.placeholder = "הקלד הודעה...";
userInput.style.flex = "1";
userInput.style.padding = "10px";
userInput.style.border = "none";
userInput.style.borderRadius = "5px";
userInput.style.outline = "none";
userInput.addEventListener("keypress", (event) => {
    if (event.key === "Enter") sendM