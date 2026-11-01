from pathlib import Path
p=Path('PROOF.md'); t=p.read_text(encoding='utf8')
t=t.replace('Thus J(B), with J(x,t)=(x,-t), has the same law as B.','In its original precise formulation, the space-time rotation J(x,t)=(-x,-t) sends B to a set with the same law as B. We use this rotation and exchange the labels of the two curves to preserve their spatial ordering.')
t=t.replace('Theorem 1.12(b), PDF p.13, with the outgoing configuration','Theorems 1.11(b) and 1.12(b), PDF pp.12–13, with the outgoing configuration')
t=t.replace('Apply J(x,t)=(x,-t).','Apply J(x,t)=(-x,-t).')
t=t.replace('The left/right spatial order is unchanged by time reflection. The contact point becomes (x,-t),','Exchanging the two curve labels restores their left/right spatial order after the spatial reflection. The contact point becomes (-x,-t),')
t=t.replace('Reflection is a bijection between that latter observable','Space-time rotation, with this exchange of curve labels, is a bijection between that latter observable')
p.write_text(t,encoding='utf8')
