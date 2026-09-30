"""Check local Markdown targets and excluded artifact types.

This is not a secret scanner or a disclosure-authorization check.
"""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
PROHIBITED = {".csv", ".tsv", ".parquet", ".xlsx", ".pptx", ".pdf", ".ipynb", ".pkl", ".pickle", ".joblib", ".onnx", ".pem", ".key"}


def main():
    errors = []
    files = [p for p in ROOT.rglob("*") if p.is_file() and ".git" not in p.relative_to(ROOT).parts]
    for path in files:
        relative = path.relative_to(ROOT)
        if path.suffix.lower() in PROHIBITED or path.name.startswith(".env") or any(part in {"private", "raw", "data", "artifacts"} for part in relative.parts):
            errors.append(f"Excluded artifact: {relative}")
        if path.suffix == ".md":
            for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", path.read_text()):
                if target.startswith(("https://", "http://", "mailto:", "#")):
                    continue
                target = target.split("#", 1)[0]
                destination = (path.parent / target).resolve()
                if not destination.is_relative_to(ROOT) or not destination.exists():
                    errors.append(f"Invalid local link in {relative}: {target}")
    if errors:
        print("\n".join(errors))
        return 1
    print(f"Checked {len(files)} files: local links and artifact checks passed.")
    print("Manual confidentiality and rights review remains necessary.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
