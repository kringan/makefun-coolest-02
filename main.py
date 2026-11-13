# Coolest art entry v2 (Python 3.13, standard library only): the art is the
# entry.png beside this file, and the program copies it to /output/entry.png.
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# The image is a cyberpunk samurai on a neon rooftop at night, holding a
# glowing katana under a rain of light, with a futuristic city behind it.
# The program validates the PNG magic bytes and the 1 MiB size cap before
# reporting success, so a bad or oversized image fails loudly instead of
# silently producing a wrong entry.

import os
import shutil

here = os.path.dirname(os.path.abspath(__file__))
src = os.path.join(here, "entry.png")
out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
dst = os.path.join(out_dir, "entry.png")
shutil.copyfile(src, dst)
size = os.path.getsize(dst)
assert size <= 1_048_576, f"entry.png too big: {size} bytes"
with open(dst, "rb") as f:
    magic = f.read(8)
assert magic == b"\x89PNG\r\n\x1a\n", "entry.png is not a PNG"
# v2: cyberpunk samurai, 819x546, 892744 bytes
print(f"wrote {dst} ({size} bytes, PNG verified)")
