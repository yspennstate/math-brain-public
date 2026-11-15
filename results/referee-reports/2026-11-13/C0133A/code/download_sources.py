"""Download selected primary papers sequentially and save a source manifest."""
import hashlib
import json
import os
import subprocess
import urllib.request
from pathlib import Path

if os.getpriority(os.PRIO_PROCESS, 0) < 10:
    os.setpriority(os.PRIO_PROCESS, 0, 10)
ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "sources"
papers = {
    "1204.1895": "https://arxiv.org/pdf/1204.1895",
    "kosygina-zerner-2013-journal": "https://www.math.sinica.edu.tw/bulletins/20131/2013106.pdf",
    "1304.7287": "https://arxiv.org/pdf/1304.7287",
    "1307.6052": "https://arxiv.org/pdf/1307.6052",
    "1504.06280": "https://arxiv.org/pdf/1504.06280",
    "1001.1741": "https://arxiv.org/pdf/1001.1741",
    "0901.4393": "https://arxiv.org/pdf/0901.4393",
    "1105.5105": "https://arxiv.org/pdf/1105.5105",
    "1105.5157": "https://arxiv.org/pdf/1105.5157",
    "1311.6158": "https://arxiv.org/pdf/1311.6158",
    "1311.7439": "https://arxiv.org/pdf/1311.7439",
    "2103.05570": "https://arxiv.org/pdf/2103.05570",
    "2201.10666": "https://arxiv.org/pdf/2201.10666",
    "math-0601233": "https://arxiv.org/pdf/math/0601233",
    "0706.0614": "https://arxiv.org/pdf/0706.0614",
    "0705.0658": "https://arxiv.org/pdf/0705.0658",
    "0803.1881": "https://arxiv.org/pdf/0803.1881",
    "1909.03159": "https://arxiv.org/pdf/1909.03159",
    "oberwolfach-2007-27": "https://publications.mfo.de/bitstream/handle/mfo/3013/OWR_2007_27.pdf?isAllowed=y&sequence=1",
    "zerner-2002": "https://www.maths.tcd.ie/EMIS/journals/EJP-ECP/article/download/1060/1060-3485-1-PB.pdf",
}
manifest = []
for name, url in papers.items():
    path = SOURCES / (name + ".pdf")
    record = {"name": name, "url": url}
    try:
        if not path.exists():
            with urllib.request.urlopen(url, timeout=45) as response:
                content = response.read(10_000_000)
            if not content.startswith(b"%PDF"):
                raise ValueError("response is not PDF")
            path.write_bytes(content)
        subprocess.run(["pdftotext", "-layout", str(path), str(path.with_suffix(".txt"))], check=True)
        record.update(bytes=path.stat().st_size, sha256=hashlib.sha256(path.read_bytes()).hexdigest())
        print(name, record["bytes"], flush=True)
    except Exception as error:
        record["error"] = f"{type(error).__name__}: {error}"
        print(name, record["error"], flush=True)
    manifest.append(record)
    (SOURCES / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
