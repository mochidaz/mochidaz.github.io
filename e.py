import sys

a = sys.argv[1]
b = sys.argv[2]

filename = "_posts/2021-1-22-Bahasa-Pemrograman-Rust-3-Fungsi-Prosedur-Return-Type.md"
with open(filename, "r+") as f:
    data = f.read()
    f.seek(0)
    f.write(data.replace(a, b))
    f.truncate()
