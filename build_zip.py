import os
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PACK_DIR = ROOT / "resource_pack"
OUTPUT_ZIP = ROOT / "eaglercraft_egyptian_pack.zip"


def main():
    if not PACK_DIR.exists():
        raise FileNotFoundError(
            "The resource_pack folder does not exist yet. Run 'python generate_egyptian_pack.py' first."
        )

    with zipfile.ZipFile(OUTPUT_ZIP, "w", compression=zipfile.ZIP_DEFLATED) as zipf:
        for file_path in PACK_DIR.rglob("*"):
            if file_path.is_file():
                arcname = file_path.relative_to(ROOT)
                zipf.write(file_path, arcname)

    print(f"Created zip archive: {OUTPUT_ZIP}")


if __name__ == "__main__":
    main()
