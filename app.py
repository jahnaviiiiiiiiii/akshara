import streamlit as st
import streamlit.components.v1 as components

# Page setup
st.set_page_config(
    page_title="Valentine 💌",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Remove Streamlit padding & chrome
st.markdown(
    """
    <style>
    #MainMenu, footer, header {visibility: hidden;}
    .block-container {
        padding: 0 !important;
        margin: 0 !important;
    }
    iframe {
        width: 100vw !important;
        height: 100vh !important;
        border: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

html_code = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<!-- Romantic font -->
<link href="https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap" rel="stylesheet">

<style>
html, body {
    margin: 0;
    padding: 0;
    width: 100vw;
    height: 100vh;
    overflow: hidden;
    background: linear-gradient(135deg, #ffd6e8, #ffb6c1);
}

.card {
    background: white;
    padding: 55px;
    border-radius: 28px;
    box-shadow: 0 25px 60px rgba(0,0,0,0.3);
    text-align: center;
    width: 420px;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}

/* ✒️ Valentine heading */
h1 {
    font-family: 'Great Vibes', cursive;
    font-size: 48px;
    margin-bottom: 35px;
}

button {
    border: none;
    border-radius: 50px;
    font-size: 22px;
    padding: 18px 38px;
    position: absolute;
    cursor: pointer;
}

#yes {
    background: #ff2e63;
    color: white;
    left: 50%;
    transform: translateX(-50%);
}

#no {
    background: #555;
    color: white;
}

.emoji {
    position: fixed;
    font-size: 50px;
    pointer-events: none;
    animation: fly 3s linear forwards;
}

@keyframes fly {
    to {
        transform: translate(var(--dx), var(--dy)) rotate(720deg);
        opacity: 0;
    }
}
</style>
</head>

<body>

<!-- 🎵 Music (unlocked by click) -->
<audio id="music" loop>
  <source src="https://cdn.pixabay.com/audio/2022/03/15/audio_9e46c4b7f2.mp3" type="audio/mpeg">
</audio>

<div class="card" id="card">
    <h1>Will you be my Valentine? 💌</h1>
    <button id="yes">YES ❤️</button>
    <button id="no">NO 💔</button>
</div>

<script>
const yes = document.getElementById("yes");
const no = document.getElementById("no");
const card = document.getElementById("card");
const music = document.getElementById("music");

/* 🎵 Unlock music on FIRST user interaction */
function startMusic() {
    music.play().catch(() => {});
    document.removeEventListener("click", startMusic);
}
document.addEventListener("click", startMusic);

/* ❤️ YES button grows every second */
let scale = 1;
setInterval(() => {
    scale += 0.05;
    yes.style.transform = `translateX(-50%) scale(${scale})`;
}, 1000);

/* 😈 NO button teleports INSIDE card only */
setInterval(() => {
    const maxX = card.clientWidth - no.offsetWidth;
    const maxY = card.clientHeight - no.offsetHeight - 20;

    no.style.left = Math.random() * maxX + "px";
    no.style.top = Math.random() * maxY + "px";
}, 700);

/* 🌪️ Emoji storm */
function storm(symbols) {
    for (let i = 0; i < 80; i++) {
        const e = document.createElement("div");
        e.className = "emoji";
        e.innerText = symbols[Math.floor(Math.random() * symbols.length)];

        const side = Math.floor(Math.random() * 4);
        let x = 0, y = 0;

        if (side === 0) { x = Math.random()*window.innerWidth; y = 0; }
        if (side === 1) { x = Math.random()*window.innerWidth; y = window.innerHeight; }
        if (side === 2) { x = 0; y = Math.random()*window.innerHeight; }
        if (side === 3) { x = window.innerWidth; y = Math.random()*window.innerHeight; }

        e.style.left = x + "px";
        e.style.top = y + "px";
        e.style.setProperty("--dx", (Math.random()*600 - 300) + "px");
        e.style.setProperty("--dy", (Math.random()*600 - 300) + "px");

        document.body.appendChild(e);
        setTimeout(() => e.remove(), 3000);
    }
}

yes.onclick = () => setInterval(() => storm(["🌹","💖","💐","🎉","❤️"]), 200);
no.onclick = () => storm(["😭","💔","🥺","😢"]);
</script>

</body>
</html>
"""

components.html(html_code, height=1000)
