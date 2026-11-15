"""Download primary papers to memory; retain pdftotext output only."""
import os
os.environ.update(OPENBLAS_NUM_THREADS="1", OMP_NUM_THREADS="1", VECLIB_MAXIMUM_THREADS="1")
import argparse
import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path
import requests

ROOT = Path(__file__).resolve().parents[1]
PAPERS = {
    "knowles_yin": "1102.0057v4",
    "benigni_cipolloni": "2212.10694v1",
    "benigni_feyzabady_2026": "2509.19581v1",
    "aggarwal_lopatto_marcinek": "2002.09355v3",
    "rivin_spheres_minima": "math/0305252v1",
    "nguyen_tao_vu_gaps": "1504.00396v2",
    "survey": "1601.03678v3",
    "bourgade_yau": "1312.1301v6",
    "benigni_deformed": "1711.07103v3",
    "benigni_fermionic": "1908.10855v2",
    "benigni_lopatto_delocalization": "2007.09585v2",
    "benigni_lopatto_que": "2103.12013v3",
    "marcinek_yau": "2005.08425v1",
    "ces_eth": "2012.13215v4",
    "ces_normality": "2103.06730v3",
    "rudelson_vershynin": "1506.04012v1",
    "luh_orourke": "1810.00489v2",
    "tao_vu_simple": "1412.1438v1",
    "tao_vu_eigenvectors": "1103.2801v2",
    "benigni_lopatto_2026": "2606.06419v2",
    "bao_bucht_schnelli_2026": "2606.17425v1",
    "osman_2026": "2609.11630v1",
    "fyodorov_shcherbina_2026": "2611.12858v1",
}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("names", nargs="*")
    args = parser.parse_args()
    out = ROOT / "sources"
    out.mkdir(exist_ok=True)
    for name in args.names or PAPERS:
        target = out / (name + ".txt")
        if target.exists():
            print(name, "already saved", flush=True)
            continue
        url = "https://arxiv.org/pdf/" + PAPERS[name]
        try:
            r = requests.get(url, timeout=80)
            r.raise_for_status()
            assert r.content.startswith(b"%PDF"), (url, r.headers.get("content-type"))
            proc = subprocess.run(["pdftotext", "-layout", "-", "-"], input=r.content,
                                  capture_output=True, check=True)
            body = proc.stdout.decode("utf-8")
            meta = {"url": url, "retrieved_utc": datetime.now(timezone.utc).isoformat(),
                    "pdf_sha256": hashlib.sha256(r.content).hexdigest(),
                    "pdf_bytes": len(r.content), "pages": body.count("\f")}
            target.write_text(json.dumps(meta) + "\n\n" + body)
            print(name, meta, flush=True)
        except Exception as e:
            print(name, type(e).__name__, str(e), flush=True)

if __name__ == "__main__":
    main()
