from pathlib import Path
import json,shutil
R=Path(__file__).resolve().parents[1];old=R.parent/'20261022T224007Z-fleet03-A059-decomposition-depth'
for x in ['code','out']:(R/x).mkdir(exist_ok=True)
shutil.copyfile(old/'code/exact.py',R/'code/exact.py')
s=(old/'code/check.py').read_text(encoding='utf-8')
s=s.replace('if sum(ct)<2:continue','if sum(ct)<1:continue').replace('len(wrappers)==33','len(wrappers)==65').replace('else 2178','else 4290')
s=s.replace("E.leconst(E.add(E.add(B,kappa,-1),{2:21*d},-1),-2*d,'B-kappa+channel <=21d')", "tax=E.add({},E.cost(c),(e*q*delta)**2)\n    E.le(E.add(DH,kappa,-1),E.add({2:21*d},tax),'all-c SINGLETON tax')")
s=s.replace("E.le(E.add(DH,kappa,-1),{2:21*d},'full D-kappa <=21d')", "inner=state((1,1,1,1),(0,0,0,0),labels,cores)\n    gg=inner[0];bb=gg[1<<(2+idx)];mm=gg[0];BG={}\n    for ss,zz in enumerate(gg):\n     if not ((ss>>(2+idx))&1):BG=E.add(BG,E.phi(zz*zz,gg[ss|(1<<(2+idx))]**2))\n    packet={}\n    for cc,kk0 in zip(ca,ka):packet=E.add(packet,E.phi((kk0+mm*cc)**2,(bb*cc)**2))\n    E.ok(B==E.add(E.add(E.add({},BG,c),E.phi(mm*mm,bb*bb),-c),packet),'general EMPTY-PAIR identity')\n    E.ok((e*q*delta)**2==bb*bb,'actual singleton square')")
(R/'code/check.py').write_text(s,encoding='utf-8')
print('BOOTSTRAPPED')
