#!/usr/bin/env python3
"""Test harness: validate agent harness output against expected behavior."""

def normalize(line: str) -> str:
    return line.strip().lower()

def expected_sequence(port: str, pin: int, cycles: int):
    seq = []
    for _ in range(cycles):
        seq.append(f"gpio port {port.lower()} pin {pin} on")
        seq.append(f"gpio port {port.lower()} pin {pin} off")
    return seq

def test_sequence(stdout: str, port="A", pin=5, cycles=3):
    actual = [normalize(line) for line in stdout.splitlines() if line.strip()]
    expected = expected_sequence(port, pin, cycles)

    if actual == expected:
        return True, "[TEST] PASS: sequence OK"
    else:
        diffs = []
        for i, (a, e) in enumerate(zip(actual, expected)):
            if a != e:
                diffs.append(f"Line {i+1}: expected '{e}' but got '{a}'")
        if len(actual) != len(expected):
            diffs.append(
                f"Length mismatch: expected {len(expected)} lines, got {len(actual)}"
            )
        return False, "[TEST] FAIL:\n" + "\n".join(diffs)

if __name__ == "__main__":
    # Simple manual run
    sample = """GPIO Port A Pin 5 ON
GPIO Port A Pin 5 OFF
GPIO Port A Pin 5 ON
GPIO Port A Pin 5 OFF"""
    ok, msg = test_sequence(sample, port="A", pin=5, cycles=2)
    print(msg)
