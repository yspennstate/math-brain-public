from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]
p=R/'DERIVATION.md';s=p.read_text(encoding='utf-8')
(R/'out/DERIVATION_FIRST_32_BOUND.md').write_text(s,encoding='utf-8')
s=s.replace('The initial quota below is 2C0+24 (32 structurally), rather than the earlier no-reset quota 2C0+10 (18 structurally). The additional initial allowance pays genuinely specified resets.','The initial quota is the SAME 2C0+10 (18 structurally) as the earlier no-reset result. A sharper complementary likelihood estimate pays the specified resets without enlarging that quota.')
start=s.index('Therefore V(empty)-q*<=')
end=s.index('## 3. One original envelope',start)
s=s[:start]+'''Write v_max=1-mu^2=4s(1-s) and q_max=(mu+e)^2+kappa[(1-e/s)v_max+2et]. For fixed s,t,e the ratio (mu^2+v)/q*(v) increases with v: writing q*(v)=A+Bv, one has A>=mu^2 and 0<=B<=1, so its derivative has numerator A-Bmu^2>=0. Consequently

    log2(V(empty)/q*)<=-log2(q_max).

The bound 1-kappa<=e/s gives, retaining the positive vacuum shift,

    1-q_max<=v_max*2e/s-2mu e<=6e.

For h=e/s in [0,1], the same kappa bound gives

    q_max>=(1-2s+sh)^2+(1-h)^2*4s(1-s)
          =1-sh(6-4h)+s^2 h(4-3h).

This polynomial decreases with s on [0,1/4]: its difference from its value at s=1/4 is

    (1/4-s)h[(6-4h)-(s+1/4)(4-3h)]>=0,

because the bracket is >=4-5h/2>=3/2. Thus

    q_max>=1-5h/4+13h^2/16
          =27/52+(13/16)(h-10/13)^2>=27/52>1/2.

Every denominator is positive. Using ln z<=z-1 and ln2>2/3 now proves the SIGNED bound

    k-c_const<=-log2(q_max)
       <=(1-q_max)/(q_max ln2)<18e.

At v_max the reference remains normalized (possibly zero on other source-support atoms); only this algebraic limit is used, so no infinite-cost reference is supplied to the theorem. In particular q_max<=1. This argument keeps the unchanged complementary child's full entropy plus KL and every reference-only atom. The earlier valid but coarser 48e/initial-rate32 draft is preserved in out/DERIVATION_FIRST_32_BOUND.md.

''' +s[end:]
s=s.replace('W=c+24e(a+b+r)','W=c+10e(a+b+r)')
s=s.replace('<=c+[48e]/2+24e(a+b+r-1)\n+      =W,','<=c+9e+10e(a+b+r-1)\n+      =W-e,') if False else s
s=s.replace('<=c+[48e]/2+24e(a+b+r-1)\n      =W,','<=c+9e+10e(a+b+r-1)\n      =W-e,')
s=s.replace('W_child=c_child+24(2e)(a-1+b+r)','W_child=c_child+10(2e)(a-1+b+r)')
s=s.replace('<=c+10e(a+b+r)<=W','<=c+10e(a+b+r)=W')
s=s.replace('For K=2C0+24','For K=2C0+10')
s=s.replace('K I(F)-[c+24(C+E+J)]','K I(F)-[c+10(C+E+J)]')
s=s.replace('(K+24)E+(K-24)(C+J)','(K+10)E+(K-10)(C+J)')
s=s.replace('gives rate32','gives rate18')
s=s.replace('The earlier no-reset rate18 does not automatically pay these resets; this proof uses rate32 because it bounds the complementary signed likelihood by 48e.','The earlier no-reset rate18 now pays these particular canonical active resets as well. The construction does not prove that every canonical reset has nonpositive cost; all sampled resets were negative, which remains a separate stronger question.')
p.write_text(s,encoding='utf-8')
p=R/'code/check.py';s=p.read_text(encoding='utf-8');s=s.replace('ck(loss[1]<=48*e)','''vmax=1-mu*mu
    qmax=(mu+e)**2+k*((1-e/s)*vmax+2*e*t)
    ck(qstar*1>=V[0]*qmax);ck(qmax>=F(27,52));ck(1-qmax<=6*e)
    ck(loss[1]<=18*e)''')
s=s.replace('(24*e*','(10*e*').replace('(48*e*','(20*e*').replace('K=2*C0+24','K=2*C0+10')
s=s.replace('ck(local[1]<=W[0])','ck(local[1]<=W[0]-e)')
p.write_text(s,encoding='utf-8')
p=R/'code/ResetAccount.lean';s=p.read_text(encoding='utf-8').replace('constc + 24 * e','constc + 9 * e').replace('remainder + 24 * e','remainder + 10 * e').replace('b + childc + remainder + terminal <=','b + childc + remainder + terminal + e <=');p.write_text(s,encoding='utf-8')
p=R/'out/FROZEN_SPEC.json';j=json.loads(p.read_text(encoding='utf-8'));j['helper_version']='A096-active-reset-v2-same-rate18';j['revision_reason']='Analytic likelihood bound sharpened48e to18e; validate same domain at original rate2C0+10 with per-query envelope release>=e';p.write_text(json.dumps(j,indent=2)+'\n',encoding='utf-8')
p=R/'code/intake.py';s=p.read_text(encoding='utf-8');s=s.replace("raw=p.read_bytes();s=raw.decode('utf-8-sig');receipts.append({'path':str(p),'bytes':len(raw),'sha256':sha(raw)});return s", "raw=p.read_bytes();encoding='utf-8-sig'\n    try:s=raw.decode(encoding)\n    except UnicodeDecodeError:encoding='cp1252';s=raw.decode(encoding)\n    receipts.append({'path':str(p),'bytes':len(raw),'sha256':sha(raw),'decoding':encoding});return s")
p.write_text(s,encoding='utf-8')
print('Saved original valid rate32 draft; strengthened original-rate18 proof and same-domain checker; explicit legacy source decoding.')
