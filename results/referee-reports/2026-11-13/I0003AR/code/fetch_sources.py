"""Independent source retrieval. PDF bytes remain in memory; save text only."""
import os
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[key] = "1"
if os.getpriority(os.PRIO_PROCESS, 0) < 10:
    os.setpriority(os.PRIO_PROCESS, 0, 10)
import argparse
import datetime as dt
import hashlib
import io
import json
from pathlib import Path
import re
import urllib.request
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "sources"

def fetch(name, url):
    OUT.mkdir(exist_ok=True)
    rec = {"name": name, "requested_url": url, "utc": dt.datetime.now(dt.timezone.utc).isoformat()}
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Independent mathematical referee, text retrieval"})
        with urllib.request.urlopen(req, timeout=50) as res:
            raw = res.read(20_000_000)
            rec.update(final_url=res.url, content_type=res.headers.get("Content-Type", ""))
        rec.update(bytes=len(raw), source_sha256=hashlib.sha256(raw).hexdigest())
        if raw.startswith(b"%PDF"):
            reader = PdfReader(io.BytesIO(raw))
            txt = "\n".join(f"\n===== PDF PAGE {n} =====\n" + (page.extract_text() or "")
                            for n, page in enumerate(reader.pages, 1))
            rec["pages"] = len(reader.pages)
            rec["extraction"] = "pypdf, page markers, control characters removed"
        else:
            txt = raw.decode("utf-8", errors="replace")
            if "<html" in txt[:3000].lower():
                from html.parser import HTMLParser
                class Plain(HTMLParser):
                    def __init__(self):
                        super().__init__(); self.parts=[]; self.hidden=0
                    def handle_starttag(self, tag, attrs):
                        if tag in ("script", "style"): self.hidden += 1
                        if tag in ("p", "div", "section", "h1", "h2", "h3", "li", "br"): self.parts.append("\n")
                    def handle_endtag(self, tag):
                        if tag in ("script", "style"): self.hidden = max(0, self.hidden-1)
                    def handle_data(self, data):
                        if not self.hidden: self.parts.append(data)
                parser = Plain(); parser.feed(txt); txt = "".join(parser.parts)
                rec["extraction"] = "HTML text, scripts and styles excluded"
            else: rec["extraction"] = "UTF-8 text"
        txt = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", "", txt)
        header = f"SOURCE: {url}\nRETRIEVED UTC: {rec['utc']}\n\n"
        data = (header + txt).encode()
        (OUT / (name + ".txt")).write_bytes(data)
        rec.update(text_sha256=hashlib.sha256(data).hexdigest(), status="ok")
        print(name, "ok", len(data), flush=True)
    except Exception as exc:
        rec.update(status="error", error=f"{type(exc).__name__}: {exc}")
        print(name, rec["error"], flush=True)
    with (OUT / "MANIFEST.txt").open("a") as stream:
        stream.write(json.dumps(rec, ensure_ascii=False) + "\n")
    return rec

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("name")
    parser.add_argument("url")
    args = parser.parse_args()
    fetch(args.name, args.url)
