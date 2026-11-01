from pathlib import Path
p=Path('ATTEMPT.md'); t=p.read_text(encoding='utf-8-sig')
a=t.index('At deterministic time s, all net points'); b=t.index('Every canonical-tail witness',a)
t=t[:a]+'''For each p in A, survey Theorem 2.11 bounds the number of outgoing paths of an individual Brownian web at (p,s) by three. In the web definition, outgoing equivalence means equality on the entire future interval, not only equality arbitrarily close to s. The bound therefore counts distinct full tails. It applies simultaneously to every point, including random p, and also to drifted webs after shearing. Combining W^l and W^r gives a set F of at most 6|A| distinct tails on [s,T]. '''+t[b:]
t=t.replace('For an individual Brownian web, Theorem 2.11 says that at a deterministic time every point with an incoming path is of type (1,1).','')
p.write_text(t,encoding='utf8')
