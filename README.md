# ⚡ Embedder Agent ⚡

A lightweight coding-agent demo that simulates the **docs → codegen → compile → test → visualize** loop for embedded systems development.  

This project takes a datasheet-like snippet (GPIO port, pin, blink period, cycles), generates C firmware, compiles or simulates it, validates behavior via a test harness, and provides interactive visualizations.

---

## 🎥 Demo Video
[![Watch the demo](Embesdder-Agent.mp4)]  
*(Replace `demo-thumbnail.png` and `demo-video-link` with your actual thumbnail and video link)*

---

## 🚀 Features
- **Natural Datasheet Parsing**  
  Example:
  ```text
  GPIO Port: A
  GPIO Pin: 5
  Blink Period (ms): 200
  Cycles: 4
Firmware Generation → Auto-generates a C program for GPIO toggling.

Compilation & Simulation → Uses GCC/Clang if available, otherwise falls back to Python simulation.

Test Harness → Verifies ON/OFF counts and sequence.

Streamlit UI:

Console output viewer

Firmware preview

Pass/fail harness feedback

LED Simulation (glowing circle)

LED Timeline chart

📸 Screenshots
LED Simulation

Timeline Visualization

🛠️ Tech Stack
Python 3.10+

Streamlit for UI

Plotly for timeline visualization

Regex + subprocess for parsing/compilation

C (GCC/Clang) for firmware

📂 Project Structure
bash
Copy code
embedder-agent/
│
├── agent/
│   └── agent_harness.py     # Parses, generates firmware, compiles/simulates
├── test_harness.py          # Validates logs against expected ON/OFF sequence
├── app.py                   # Streamlit UI
├── README.md
└── screenshots/
    ├── led-sim.png
    └── led-timeline.png
▶️ Running Locally
Clone and install dependencies:

bash
Copy code
git clone https://github.com/yourusername/embedder-agent.git
cd embedder-agent
pip install -r requirements.txt
Run the Streamlit app:

bash
Copy code
streamlit run app.py
⚠️ If you don’t have GCC/Clang installed, the app will fall back to simulation mode.

🧪 Example Output
css
Copy code
GPIO Port A Pin 5 ON
GPIO Port A Pin 5 OFF
GPIO Port A Pin 5 ON
GPIO Port A Pin 5 OFF
GPIO Port A Pin 5 ON
GPIO Port A Pin 5 OFF
✨ Why This Matters
This demo showcases how coding agents can go beyond text generation and support a full embedded development workflow:

Structured parsing

Realistic codegen

Build/test loop

Visualization for validation

It’s designed as a foundation for scaling to real STM32 / ESP32 boards with hardware-in-the-loop testing.

👩‍💻 Author
Gehna Ahuja

LinkedIn

GitHub