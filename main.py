"""Museum of the Year 3000 — label QR Code, c. 2023.

Menulis satu label museum fiktif dari tahun 3000 ke berkas entry.txt
di dalam direktori keluaran yang ditunjuk $MAKEFUN_OUTPUT_DIR.

Program ini sengaja kecil: tidak ada dependensi, tidak ada jaringan,
dan tidak pernah menulis ke mana pun selain direktori keluaran.
"""

from __future__ import annotations

import os
import sys

LABEL = (
    "QR Code, c. 2023. Sacred maze, printed on tables. "
    "Humans pointed their glowing slabs at it and waited, "
    "faithfully, for food to appear."
)

OUTPUT_NAME = "entry.txt"


def target_dir() -> str:
    """Direktori keluaran dari environment, atau direktori kerja saat ini."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", os.getcwd())


def save_label(directory: str) -> bool:
    """Tulis label ke entry.txt; kembalikan False kalau tidak bisa ditulis."""
    try:
        os.makedirs(directory, exist_ok=True)
        path = os.path.join(directory, OUTPUT_NAME)
        with open(path, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(LABEL + "\n")
    except OSError:
        return False
    return True


def main() -> int:
    # Kegagalan menulis bukan alasan untuk crash: diam-diam selesai.
    save_label(target_dir())
    return 0


if __name__ == "__main__":
    sys.exit(main())
