import subprocess, sys
from pathlib import Path
items = [
('locality-1412.0150','https://arxiv.org/pdf/1412.0150'),
('height-1501.00476','https://arxiv.org/pdf/1501.00476'),
('lindorfer-1902.08493','https://arxiv.org/pdf/1902.08493'),
('panagiotis-1908.00127','https://arxiv.org/pdf/1908.00127'),
('cubic-1610.00107','https://arxiv.org/pdf/1610.00107'),
('lehner-lindorfer-panagiotis-2403.13121','https://arxiv.org/pdf/2403.13121'),
('aubrun-bitar-2402.13944','https://arxiv.org/pdf/2402.13944'),
('grimmett-2608.19349','https://arxiv.org/pdf/2608.19349'),
('percolation-couplings-2504.02427','https://arxiv.org/pdf/2504.02427'),
('patterns-2611.00816','https://arxiv.org/pdf/2611.00816'),
('amenability-1510.08659','https://arxiv.org/pdf/1510.08659'),
('cubic-published','https://www.statslab.cam.ac.uk/~grg/papers/cubic-published.pdf'),
]
root = Path(__file__).resolve().parents[1]
for name, url in items:
    if (root/'sources'/f'{name}.txt').exists(): continue
    ret = subprocess.run([sys.executable, str(root/'code'/'fetch_text.py'), name, url], cwd=root)
    if ret.returncode: print('FAILED', name, flush=True)
