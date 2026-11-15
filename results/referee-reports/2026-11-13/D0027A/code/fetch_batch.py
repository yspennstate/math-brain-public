import concurrent.futures
from fetch_sources import fetch
ITEMS = [
 ('CMST2010.txt','https://arxiv.org/pdf/0810.4237'),
 ('CFM2016.txt','https://arxiv.org/pdf/1404.7257'),
 ('MV2019.txt','https://arxiv.org/pdf/1609.01364'),
 ('Ertul2022.txt','https://alea.impa.br/articles/v19/19-20.pdf'),
 ('BDT2019.txt','https://arxiv.org/pdf/1803.08761'),
 ('Blondel2013.txt','https://arxiv.org/pdf/1212.4435'),
 ('Mareche2019.txt','https://arxiv.org/pdf/1907.05844'),
 ('HartarskyToninelli2022.txt','https://arxiv.org/pdf/2212.08437'),
]
def run(item):
 try: fetch(*item)
 except Exception as exc: print(item[0],type(exc).__name__,str(exc),flush=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
 list(pool.map(run, ITEMS))
