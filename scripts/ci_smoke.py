"""Assert the stable teaching verdicts produced by the CI smoke run."""

import argparse
from pathlib import Path


EXPECTED = {
    "make-demo-output": (
        "-> AMBIGUOUS:",
        "-> ATTRIBUTE ENCODED:",
        "group leakage   NOT ASSESSED",
        "-> GROUP LEAKAGE:",
    ),
    "clean-report": (
        "-> ATTRIBUTE ENCODED:",
        "group leakage   NOT ASSESSED",
        "-> NO FLAGS: group leakage NOT ASSESSED",
    ),
    "leaked-report": (
        "-> GROUP LEAKAGE: 1 group(s) span multiple splits",
        "patient0",
    ),
    "worked-output": (
        "AUROC: 0.938",
        "prevalence=1%: PPV=0.154",
        "Fixed operating characteristics are an assumption, not a transfer guarantee.",
    ),
}


def parse_args():
    parser = argparse.ArgumentParser()
    for name in EXPECTED:
        parser.add_argument(f"--{name}", type=Path, required=True)
    return parser.parse_args()


def main():
    args = parse_args()
    missing = []
    for name, expected_fragments in EXPECTED.items():
        path = getattr(args, name.replace("-", "_"))
        text = path.read_text(encoding="utf-8")
        for fragment in expected_fragments:
            if fragment not in text:
                missing.append(f"{path}: missing {fragment!r}")

    if missing:
        raise SystemExit("CI smoke assertions failed:\n" + "\n".join(missing))
    print("CI smoke assertions passed")


if __name__ == "__main__":
    main()
