from fetch_sources import fetch
from concurrent.futures import ThreadPoolExecutor
papers=[('bordenave_chafai_garcia_2012.05602v2','https://arxiv.org/pdf/2012.05602v2'),('bcct_1607.05484','https://arxiv.org/pdf/1607.05484'),('bourgade_yau_yin_1206.1449v3','https://arxiv.org/pdf/1206.1449v3'),('alt_erdos_kruger_1612.07776','https://arxiv.org/pdf/1612.07776'),('tao_vu_local_1206.1893','https://arxiv.org/pdf/1206.1893'),('cipolloni_erdos_schroder_1912.04100','https://arxiv.org/pdf/1912.04100')]
with ThreadPoolExecutor(max_workers=3) as ex:
    futures=[ex.submit(fetch,*p) for p in papers]
    for p,f in zip(papers,futures):
        try:f.result()
        except Exception as e:print(p[0],repr(e),flush=True)
