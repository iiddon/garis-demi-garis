"""Gabungkan src/shell.html dan src/data.js menjadi index.html (satu file mandiri)."""
from pathlib import Path

root = Path(__file__).parent
shell = (root / "src" / "shell.html").read_text(encoding="utf-8")
data = (root / "src" / "data.js").read_text(encoding="utf-8")
assert "/*DATA*/" in shell, "penanda /*DATA*/ tidak ditemukan di shell.html"
(root / "index.html").write_text(shell.replace("/*DATA*/", data), encoding="utf-8")
print("index.html diperbarui")
