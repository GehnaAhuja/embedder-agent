# ⚡ Embedder Agent ⚡

A lightweight coding-agent demo that simulates the **docs → codegen → compile → test → visualize** loop for embedded systems development.  

This project takes a datasheet-like snippet (GPIO port, pin, blink period, cycles), generates C firmware, compiles or simulates it, validates behavior via a test harness, and provides interactive visualizations.

---

## 🎥 Demo Video
[![Watch the demo](Embesdder-Agent.mp4)]  

---

## 🚀 Features
- **Natural Datasheet Parsing**  
  Example:
  ```text
  GPIO Port: A
  GPIO Pin: 5
  Blink Period (ms): 200
  Cycles: 4

## Running Locally
Clone and install dependencies:
```
git clone https://github.com/yourusername/embedder-agent.git
cd embedder-agent
pip install -r requirements.txt
```
Run the Streamlit app:
```
streamlit run app.py
```

It’s designed as a foundation for scaling to real STM32 / ESP32 boards with hardware-in-the-loop testing.
