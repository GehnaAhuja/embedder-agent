import time
import streamlit as st
import plotly.graph_objects as go
from agent.agent_harness import main as run_agent
from agent.test_harness import test_sequence

st.set_page_config(page_title="Embedder Agent Demo", layout="wide")

# ===============================
# App Title
# ===============================
st.markdown(
    "<h1 style='text-align: center; font-size: 50px;'>⚡ Embedder Agent ⚡</h1>",
    unsafe_allow_html=True,
)

st.sidebar.header("Parameters")
port = st.sidebar.text_input("GPIO Port", "A")
pin = st.sidebar.number_input("GPIO Pin", value=5, step=1)
period = st.sidebar.number_input("Blink Period (ms)", value=200, step=50)
cycles = st.sidebar.number_input("Cycles", value=3, step=1)

if st.sidebar.button("🚀 Run Agent"):
    logs, firmware = run_agent(port=port, pin=pin, period=period, cycles=cycles)

    # ===============================
    # LED Simulation (on top)
    # ===============================
    st.subheader("🔴 LED Simulation")

    led_placeholder = st.empty()
    parsed_lines = [line.strip().lower() for line in logs.splitlines() if line.strip()]

    for line in parsed_lines:
        if "on" in line:
            led_placeholder.markdown(
                """
                <div style='text-align:center;'>
                    <div style='width:120px; height:120px; margin:auto;
                                border-radius:50%; background-color:limegreen;
                                box-shadow:0 0 40px limegreen;'>
                    </div>
                    <p style='font-size:22px; color:limegreen;'>LED ON</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            led_placeholder.markdown(
                """
                <div style='text-align:center;'>
                    <div style='width:120px; height:120px; margin:auto;
                                border-radius:50%; background-color:darkred;
                                box-shadow:0 0 30px red;'>
                    </div>
                    <p style='font-size:22px; color:red;'>LED OFF</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
        time.sleep(period / 1000.0)

    # ===============================
    # Console Output
    # ===============================
    st.subheader("Console Output")
    st.code(logs)

    # ===============================
    # Generated Firmware
    # ===============================
    st.subheader("Generated Firmware (C)")
    st.code(firmware, language="c")

    # ===============================
    # Test Harness
    # ===============================
    st.subheader("Test Harness")
    ok, msg = test_sequence(logs, port=port, pin=pin, cycles=cycles)
    if ok:
        st.success(msg)
    else:
        st.error(msg)

    # ===============================
    # LED Timeline
    # ===============================
    st.subheader("📈 LED Timeline")

    timeline_states = []
    for line in parsed_lines:
        state = 1 if "on" in line else 0
        timeline_states.append(state)

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=list(range(len(timeline_states))),
            y=timeline_states,
            mode="lines+markers",
            line_shape="hv",
            name="LED State",
        )
    )
    fig.update_layout(
        xaxis_title="Cycle Step",
        yaxis=dict(
            tickmode="array",
            tickvals=[0, 1],
            ticktext=["OFF", "ON"],
            title="LED State",
        ),
        template="plotly_dark",
    )
    st.plotly_chart(fig, use_container_width=True)
