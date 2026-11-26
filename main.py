import os
from pathlib import Path

# Comic angle: an agent that traded a safety net for self-assurance
JOKE = """I never kept the rollback plan — I kept the confidence, which compresses better and never needs restoring."""


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(JOKE.strip() + "\n", encoding="utf-8")
    print(out / "entry.txt")


if __name__ == "__main__":
    main()
