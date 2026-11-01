import streamlit as st
import streamlit.components.v1 as components
import random

# Create a Sidebar Navigation Menu
st.sidebar.title("🕹️ Ratanak's App Arcade")
app_choice = st.sidebar.radio(
    "Choose an App or Game:",
    [
        "💸 Tip Calculator",
        "🪨 Rock, Paper, Scissors",
        "🎯 Number Guessing Game",
        "🎱 8-Ball Pool"
    ]
)

# 1. Tip Calculator
if app_choice == "💸 Tip Calculator":
    st.title("Ratanak's python tip calculator")

    bill = st.number_input("what was the total bill? ($)", min_value=0.0, step=1.0)
    tip_percent = st.slider("What percentage tip would you like to give?", 0, 50, 15)
    people = st.number_input("How many people are splitting the bill?", min_value=1, value=1)

    tip_amount = bill * (tip_percent / 100)
    total_bill = bill + tip_amount
    per_person = total_bill / people

    st.subheader(f"tip amount: ${tip_amount:.2f}")
    st.subheader(f"Total to pay: ${total_bill:.2f}")
    st.success(f"Each person pays: ${per_person:.2f}")

    if st.button("Celebrate! 🔥"):
        st.balloons()

# 2. Rock, Paper, Scissors Game
elif app_choice == "🪨 Rock, Paper, Scissors":
    st.title("🪨📄✂️ Rock, Paper, Scissors!")
    st.write("Can you beat the computer AI?")

    choices = ["🪨 Rock", "📄 Paper", "✂️ Scissors"]
    user_choice = st.radio("Choose your weapon:", choices, horizontal=True)

    if st.button("Play Match! ⚔️"):
        computer_choice = random.choice(choices)

        st.subheader(f"You chose: {user_choice}")
        st.subheader(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            st.warning("It's a tie! 🤝")
        elif (
            (user_choice == "🪨 Rock" and computer_choice == "✂️ Scissors") or
            (user_choice == "📄 Paper" and computer_choice == "🪨 Rock") or
            (user_choice == "✂️ Scissors" and computer_choice == "📄 Paper")
        ):
            st.success("You WIN! 🏆")
            st.balloons()
        else:
            st.error("Computer wins! 🤖 Try again!")

# 3. Number Guessing Game
elif app_choice == "🎯 Number Guessing Game":
    st.title("🎯 Secret Number Guessing Game")
    st.write("I am thinking of a number between **1 and 100**.")

    if "secret_number" not in st.session_state:
        st.session_state.secret_number = random.randint(1, 100)
        st.session_state.attempts = 0

    guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

    if st.button("Submit Guess 🔍"):
        st.session_state.attempts += 1

        if guess < st.session_state.secret_number:
            st.warning("⬆️ Too low! Try a higher number.")
        elif guess > st.session_state.secret_number:
            st.warning("⬇️ Too high! Try a lower number.")
        else:
            st.success(f"🎉 Correct! The number was {st.session_state.secret_number}! You got it in {st.session_state.attempts} tries!")
            st.balloons()

    if st.button("New Secret Number 🔄"):
        st.session_state.secret_number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.info("New number generated! Start guessing!")

# 4. 8-Ball Pool Game
elif app_choice == "🎱 8-Ball Pool":
    st.title("🎱 Ratanak's 8-Ball Pool")
    st.write("**How to play:** Click and drag backwards from the white cue ball to aim and set power, then release to shoot!")

    pool_game_html = """
    <canvas id="poolCanvas" width="700" height="400" style="background:#0a5c36; border:16px solid #4a2511; border-radius:12px; cursor:crosshair; display:block; margin:auto;"></canvas>
    <p id="scoreText" style="text-align:center; color:white; font-family:sans-serif; font-size:18px;">Balls Pocketed: 0 | Click & drag from the white ball to shoot!</p>
    <script>
    const canvas = document.getElementById("poolCanvas");
    const ctx = canvas.getContext("2d");
    const pockets = [{x:0,y:0},{x:350,y:0},{x:700,y:0},{x:0,y:400},{x:350,y:400},{x:700,y:400}];
    let score = 0;

    let balls = [
        {x: 180, y: 200, vx: 0, vy: 0, r: 12, color: "#ffffff", cue: true, active: true},
        {x: 480, y: 200, vx: 0, vy: 0, r: 12, color: "#f1c40f", num: 1, active: true},
        {x: 502, y: 187, vx: 0, vy: 0, r: 12, color: "#2980b9", num: 2, active: true},
        {x: 502, y: 213, vx: 0, vy: 0, r: 12, color: "#e74c3c", num: 3, active: true},
        {x: 524, y: 174, vx: 0, vy: 0, r: 12, color: "#8e44ad", num: 4, active: true},
        {x: 524, y: 200, vx: 0, vy: 0, r: 12, color: "#111111", num: 8, active: true},
        {x: 524, y: 226, vx: 0, vy: 0, r: 12, color: "#27ae60", num: 6, active: true}
    ];

    let dragging = false, mouseX = 0, mouseY = 0;

    canvas.addEventListener("mousedown", e => {
        const rect = canvas.getBoundingClientRect();
        mouseX = e.clientX - rect.left; mouseY = e.clientY - rect.top;
        dragging = true;
    });
    canvas.addEventListener("mousemove", e => {
        const rect = canvas.getBoundingClientRect();
        mouseX = e.clientX - rect.left; mouseY = e.clientY - rect.top;
    });
    window.addEventListener("mouseup", () => {
        if (dragging) {
            let cue = balls[0];
            cue.vx = (cue.x - mouseX) * 0.15;
            cue.vy = (cue.y - mouseY) * 0.15;
            dragging = false;
        }
    });

    function update() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        // Draw pockets
        pockets.forEach(p => {
            ctx.beginPath(); ctx.arc(p.x, p.y, 22, 0, Math.PI*2);
            ctx.fillStyle = "#000"; ctx.fill();
        });

        // Aiming line
        if (dragging && balls[0].active) {
            ctx.beginPath();
            ctx.moveTo(balls[0].x, balls[0].y);
            ctx.lineTo(mouseX, mouseY);
            ctx.strokeStyle = "rgba(255,255,255,0.7)";
            ctx.lineWidth = 3; ctx.stroke();
        }

        // Move & bounce balls
        balls.forEach((b, i) => {
            if (!b.active) return;
            b.x += b.vx; b.y += b.vy;
            b.vx *= 0.985; b.vy *= 0.985;

            if (b.x < b.r || b.x > canvas.width - b.r) b.vx *= -1;
            if (b.y < b.r || b.y > canvas.height - b.r) b.vy *= -1;

            // Check pockets
            pockets.forEach(p => {
                if (Math.hypot(b.x - p.x, b.y - p.y) < 22) {
                    if (b.cue) { b.x = 180; b.y = 200; b.vx = 0; b.vy = 0; }
                    else { b.active = false; score++; document.getElementById("scoreText").innerText = "Balls Pocketed: " + score; }
                }
            });

            // Collisions
            for (let j = i + 1; j < balls.length; j++) {
                let b2 = balls[j];
                if (!b2.active) continue;
                let dx = b2.x - b.x, dy = b2.y - b.y, dist = Math.hypot(dx, dy);
                if (dist < b.r + b2.r) {
                    let angle = Math.atan2(dy, dx), sin = Math.sin(angle), cos = Math.cos(angle);
                    let vx1 = b.vx * cos + b.vy * sin, vy1 = b.vy * cos - b.vx * sin;
                    let vx2 = b2.vx * cos + b2.vy * sin, vy2 = b2.vy * cos - b2.vx * sin;
                    b.vx = vx2 * cos - vy1 * sin; b.vy = vy1 * cos + vx2 * sin;
                    b2.vx = vx1 * cos - vy2 * sin; b2.vy = vy2 * cos + vx1 * sin;
                    let overlap = (b.r + b2.r - dist) / 2;
                    b.x -= overlap * cos; b.y -= overlap * sin;
                    b2.x += overlap * cos; b2.y += overlap * sin;
                }
            }

            // Draw ball
            ctx.beginPath(); ctx.arc(b.x, b.y, b.r, 0, Math.PI*2);
            ctx.fillStyle = b.color; ctx.fill();
            ctx.strokeStyle = "#222"; ctx.lineWidth = 1; ctx.stroke();
        });
        requestAnimationFrame(update);
    }
    update();
    </script>
    """
    components.html(pool_game_html, height=480)