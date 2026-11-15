from fetch_sources import fetch
from concurrent.futures import ThreadPoolExecutor
papers=[('gotze_jalowy_1807.00489v3','https://arxiv.org/pdf/1807.00489v3'),('jalowy_wasserstein_2111.03595v3','https://arxiv.org/pdf/2111.03595v3'),('jalowy_products_1912.09300','https://arxiv.org/pdf/1912.09300'),('gotze_tikhomirov_0709.3995','https://arxiv.org/pdf/0709.3995'),('tao_vu_0708.2895','https://arxiv.org/pdf/0708.2895'),('williams_small_2020','https://sites.williams.edu/mstoiciu/files/2020/11/Random_Matrix_Theory.pdf')]
with ThreadPoolExecutor(max_workers=3) as ex:
    futures=[ex.submit(fetch,*p) for p in papers]
    for p,f in zip(papers,futures):
        try:f.result()
        except Exception as e:print(p[0],repr(e),flush=True)
