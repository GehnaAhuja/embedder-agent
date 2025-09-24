#!/usr/bin/env python3
"""Agent harness: parse snippet, generate firmware, compile or simulate, return logs + firmware."""

import re
import shutil
import subprocess
import tempfile
from pathlib import Path

# ===============================
# Parser for datasheet snippet
# ===============================
def parse_snippet(text: str):
    port_match = re.search(r"GPIO\s*Port\s*:\s*([A-Z])", text, re.I)
    pin_match = re.search(r"GPIO\s*Pin\s*:\s*(\d+)", text, re.I)
    period_match = re.search(r"Blink\s*Period\s*\(ms\)\s*:\s*(\d+)", text, re.I)
    cycles_match = re.search(r"Cycles\s*:\s*(\d+)", text, re.I)

    if not (port_match and pin_match and period_match and cycles_match):
        raise ValueError(f"Could not parse snippet:\n{text}")

    port = port_match.group(1)
    pin = int(pin_match.group(1))
    period_ms = int(period_match.group(1))
    cycles = int(cycles_match.group(1))

    return port, pin, period_ms, cycles


# ===============================
# C firmware template
# ===============================
C_TEMPLATE = r"""
#include <stdio.h>
#include <time.h>

int main() {{
    int pin = {pin};
    int period = {period};
    int cycles = {cycles};

    struct timespec ts;
    ts.tv_sec = 0;
    ts.tv_nsec = period * 1000000;

    for (int i = 0; i < cycles; i++) {{
        printf("GPIO Port {port} Pin %d ON\n", pin);
        nanosleep(&ts, NULL);
        printf("GPIO Port {port} Pin %d OFF\n", pin);
        nanosleep(&ts, NULL);
    }}
    return 0;
}}
"""


# ===============================
# Generator + Runner with fallback
# ===============================
def generate_and_run(port, pin, period, cycles):
    compiler = shutil.which("gcc") or shutil.which("clang")

    if not compiler:
        # Simulation mode
        out = []
        for i in range(cycles):
            out.append(f"GPIO Port {port} Pin {pin} ON")
            out.append(f"GPIO Port {port} Pin {pin} OFF")
        return "\n".join(out)

    c_code = C_TEMPLATE.format(port=port, pin=pin, period=period, cycles=cycles)

    with tempfile.TemporaryDirectory() as tmpdir:
        c_path = Path(tmpdir) / "firmware.c"
        bin_path = Path(tmpdir) / "firmware.out"
        c_path.write_text(c_code)

        compile_proc = subprocess.run(
            [compiler, str(c_path), "-o", str(bin_path)],
            capture_output=True,
            text=True,
        )
        if compile_proc.returncode != 0:
            return f"Compilation failed:\n{compile_proc.stderr}"

        run_proc = subprocess.run([str(bin_path)], capture_output=True, text=True)
        return run_proc.stdout


# ===============================
# Main API for UI
# ===============================
def main(snippet=None, port=None, pin=None, period=None, cycles=None):
    if snippet:
        port, pin, period, cycles = parse_snippet(snippet)
    logs = generate_and_run(port, pin, period, cycles)
    firmware = C_TEMPLATE.format(port=port, pin=pin, period=period, cycles=cycles)
    return logs, firmware


if __name__ == "__main__":
    snippet = """GPIO Port: A
GPIO Pin: 5
Blink Period (ms): 200
Cycles: 3"""
    logs, firmware = main(snippet=snippet)
    print(logs)
