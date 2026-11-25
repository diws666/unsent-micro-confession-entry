import os

TO_LINE = "To: my old team lead"
MESSAGE = "I quit because the work stopped scaring me. I never told you it was the best job I ever had."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
ENTRY_TEXT = TO_LINE + "\n" + MESSAGE

os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(ENTRY_TEXT)
