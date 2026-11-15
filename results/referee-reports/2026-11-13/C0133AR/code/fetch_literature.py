"""Independent primary-source downloads; at most three download threads."""
import concurrent.futures, hashlib, json, subprocess, requests
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
ITEMS={"journal":"https://www.math.sinica.edu.tw/bulletins/20131/2013106.pdf", "holmes2012":"https://arxiv.org/pdf/0901.4393", "holmes_salisbury_rwre":"https://arxiv.org/pdf/1105.5105", "holmes_salisbury_arrows":"https://arxiv.org/pdf/1105.5157", "mprv":"https://arxiv.org/pdf/1001.1741", "zerner2006":"https://arxiv.org/pdf/math/0601233", "berard_ramirez":"https://arxiv.org/pdf/0705.0658", "kosygina_peterson":"https://arxiv.org/pdf/1504.06280", "pham":"https://arxiv.org/pdf/1311.6158", "letterhos":"https://arxiv.org/pdf/2103.05570", "kosygina_zerner2008":"https://arxiv.org/pdf/0801.1924"}
def fetch(item):
 name,url=item
 try:
  r=requests.get(url,timeout=45);r.raise_for_status();assert r.content.startswith(b"%PDF")
  p=ROOT/"sources"/(name+".pdf");p.write_bytes(r.content)
  subprocess.run(["pdftotext","-layout",str(p),str(p.with_suffix(".txt"))],check=True)
  return dict(name=name,url=url,bytes=len(r.content),sha256=hashlib.sha256(r.content).hexdigest())
 except Exception as exc:return dict(name=name,url=url,error=str(exc))
if __name__=="__main__":
 with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
  results=list(pool.map(fetch,ITEMS.items()))
 (ROOT/"sources/literature_manifest.json").write_text(json.dumps(results,indent=2))
 for row in results:print(row,flush=True)
