# Independent re-derivation of paper 9's hand-typed prose numbers from records/.
import json, glob, os, math, statistics as st, sys
from collections import defaultdict
import numpy as np
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "records")
REC = defaultdict(list)
for f in glob.glob(os.path.join(R, "p9*.json")):
    d = json.load(open(f, encoding="utf-8")); REC[d.get("kind","?")].append(d)
def mse(v):
    m=st.mean(v); se=st.stdev(v)/math.sqrt(len(v)) if len(v)>1 else 0.0; return m,se
def sd(v): return st.stdev(v) if len(v)>1 else 0.0
def q(v,p):
    v=sorted(v); k=(len(v)-1)*p; lo=math.floor(k); hi=math.ceil(k)
    return v[lo] if lo==hi else v[lo]*(hi-k)+v[hi]*(k-lo)
def wls(D,Y,W,ncol):
    basis=lambda d:[1.0,1.0/d,1.0/d**2][:ncol]
    X=np.array([basis(d) for d in D]); y=np.array(Y); w=np.array(W)
    XtWX=X.T@(X*w[:,None]); XtWy=X.T@(w*y); beta=np.linalg.solve(XtWX,XtWy)
    res=y-X@beta; chi2=float((w*res**2).sum()); dof=max(1,len(D)-ncol)
    cov=np.linalg.inv(XtWX)
    return beta, np.sqrt(np.diag(cov)), chi2, dof
def section(t): print("\n"+"="*8, t)

# ---------------- A. Target 3 (p9_gap2)
section("A. Target 3 p9_gap2")
agg=defaultdict(list)
for d in REC["p9_gap2"]:
    for r in d["records"]: agg[(r["d"],r["h"])].append(r)
for (dd,hh) in sorted(agg):
    rs=agg[(dd,hh)]
    v=[r["V_over_sigma2"] for r in rs]; e=[r["V_over_sigma2_exact"] for r in rs]
    gaps=[r["V_rel_gap"] for r in rs]; ts=[r["tau_sum"] for r in rs]
    forms=set(r.get("exact_form","trace") for r in rs)
    wc=defaultdict(list)
    for r in rs:
        for c,dl in zip(r["window_certificates"], r["window_deltas"]): wc[round(dl,4)].append(c)
    bc=[r["best_certificate"] for r in rs]
    print(f"d={dd} h={hh} n={len(rs)} V={st.mean(v):.4f}+-{sd(v):.4f} Vexact={st.mean(e):.4f} maxgap={max(gaps):.2e} meangap={st.mean(gaps):.1e} tau_sum min={min(ts):.6f} mean={st.mean(ts):.6f} forms={forms} best_cert={st.mean(bc):.4f}")
    for dl,cs in sorted(wc.items()): print(f"      window delta_L={dl}: cert mean {st.mean(cs):.4f} sd {sd(cs):.4f} n={len(cs)}")
for hh in (0.5,1.0,2.0):
    m=st.mean([r['V_over_sigma2'] for r in agg[(9,hh)]])
    print(f"d=9 h={hh}: V/0.3106={m/0.31060759756232:.2f}  V/0.2186={m/0.21857955898172504:.2f}")
for key in ((10,1.0),(9,1.0)):
    rs=agg[key]
    print("blocks",key,"designs",len(rs))
    Ls=sorted(set(b["L"] for r in rs for b in r["blocks"]))
    for L in Ls:
        bs=[b for r in rs for b in r["blocks"] if b["L"]==L]
        sr=[b["S_dev_ratio"] for b in bs if b["S_dev_ratio"] is not None]
        g=[b.get("g_of_delta") for b in bs if b.get("g_of_delta") is not None]
        print(f"   L={L} D_L={bs[0]['D_L']:.0f} delta={st.mean([b['delta_L'] for b in bs]):.4f} T/n={st.mean([b['T_L_over_n'] for b in bs]):.4f} cert={st.mean([b['certificate'] for b in bs]):.4f} sd={sd([b['certificate'] for b in bs]):.4f} g(delta)={(st.mean(g) if g else float('nan')):.4f} Sratio={(st.mean(sr) if sr else float('nan')):.3f} inwin={bs[0]['in_window']}")
r0=agg[(10,1.0)][0]
print("tab:t3 uses design rep0 only:", [(b["L"],round(b["certificate"],4)) for b in r0["blocks"]])

# ---------------- B. Target 4 hardedge
section("B. Target 4 p9_hardedge")
agg=defaultdict(list)
for d in REC["p9_hardedge"]:
    for r in d["records"]: agg[r["d"]].append(r)
F=lambda t: 1-math.exp(-math.sqrt(t)-t/2)
def ks(vals):
    v=sorted(vals); n=len(v); m=0
    for i,x in enumerate(v):
        Fx=F(x); m=max(m, abs((i+1)/n-Fx), abs(i/n-Fx))
    return m
fitD,fitY,fitW=[],[],[]
null={20:2.0329,30:2.0258,40:2.0207}
for dd in sorted(agg):
    rs=agg[dd]; t4=[r["d_tr_A4"] for r in rs]; op=[r["sqrtd_op_A"] for r in rs]
    m,se=mse(t4)
    ov=[x for r in rs if r.get("ones_overlap") for x in r["ones_overlap"][:3]]
    sr=[r["smin_ratio"] for r in rs if r.get("smin_ratio")]
    ovs = f"{st.mean(ov):.2f}+-{sd(ov):.2f} p90={q(ov,0.9):.2f}" if ov else "n/a"
    print(f"d={dd} n={len(rs)} dTrA4={m:.4f}+-{se:.4f} (sd {sd(t4):.3f}) sqrtd_op={st.mean(op):.4f}+-{sd(op)/math.sqrt(len(op)):.4f} overlap={ovs} smin_ratio mean={st.mean(sr):.3f} sd={sd(sr):.3f} med={st.median(sr):.3f} p10={q(sr,0.1):.3f} p90={q(sr,0.9):.3f}")
    print(f"      KS to 1-exp(-sqrt t-t/2): Z {ks([r['stat_Z'] for r in rs]):.3f}  [b,H] {ks([r['stat_BH'] for r in rs]):.3f}  H {ks([r['stat_H'] for r in rs]):.3f}  crit95={1.36/math.sqrt(len(rs)):.3f}")
    inv=[1/math.sqrt(r["stat_Z"]) for r in rs]
    B=150; means=[st.mean(inv[i:i+B]) for i in range(0,len(inv)-B+1,B)]; meds=[st.median(inv[i:i+B]) for i in range(0,len(inv)-B+1,B)]
    if len(means)>=2:
        print(f"      blocks of {B}: means {[round(x,1) for x in sorted(means)]} cv={st.stdev(means)/st.mean(means):.3f} spread x{max(means)/min(means):.1f}; medians {min(meds):.2f}..{max(meds):.2f} cv={st.stdev(meds)/st.mean(meds):.3f}")
    bh=[r["stat_BH"] for r in rs]
    print(f"      lower tail of p s_min([b,H])^2: F(q2,q5,q10,q20)= {[round(F(q(bh,p)),3) for p in (0.02,0.05,0.10,0.20)]}")
    if dd in null:
        ex=m-null[dd]; print(f"      excess over GOE null {null[dd]}: {ex:.3f}+-{se:.3f} = {ex/se:.0f} se; d*excess={dd*ex:.2f}")
        fitD.append(dd); fitY.append(m); fitW.append(1/se**2)
    print(f"      op^2/TrA4 ratio: {st.mean([r['sqrtd_op_A']**2/r['d_tr_A4'] for r in rs]):.3f}")
if len(fitD)>=3:
    a2,b2=np.linalg.solve(np.array([[1,1/fitD[0]],[1,1/fitD[-1]]]),np.array([fitY[0],fitY[-1]]))
    print(f"two-point fit d TrA4 = {a2:.3f} + {b2:.2f}/d ; predicts middle {a2+b2/fitD[1]:.4f} vs {fitY[1]:.4f} ({(a2+b2/fitD[1]-fitY[1])*math.sqrt(fitW[1]):.2f} se)")
    beta,se,chi2,dof=wls(fitD,fitY,fitW,2); print(f"weighted 3-pt fit a={beta[0]:.3f}+-{se[0]:.3f} b={beta[1]:.2f}+-{se[1]:.2f} chi2={chi2:.3f} dof={dof}")
    ex=[fitY[i]-null[fitD[i]] for i in range(3)]; dex=[fitD[i]*ex[i] for i in range(3)]
    a2,b2=np.linalg.solve(np.array([[1,1/fitD[0]],[1,1/fitD[-1]]]),np.array([dex[0],dex[-1]]))
    se_mid=fitD[1]/math.sqrt(fitW[1])
    print(f"d*excess: {[round(x,2) for x in dex]}; two-point fit {a2:.2f} + {b2:.1f}/d predicts middle {a2+b2/fitD[1]:.3f} vs {dex[1]:.3f} ({(a2+b2/fitD[1]-dex[1])/se_mid:.2f} se, se_mid={se_mid:.3f})")

# ---------------- C. moments (Veronese only)
section("C. p9_moments Veronese-only + controls")
agg=defaultdict(list)
for d in REC["p9_moments"]:
    law=d.get("rowlaw") or "veronese"
    for r in d["records"]: agg[(law,r["d"])].append(r)
cat={"m4":2,"m6":5,"m8":14,"m10":42}
for (law,dd) in sorted(agg):
    rs=agg[(law,dd)]
    s=f"{law} d={dd} n={len(rs)}"
    for k in ("m4","m6","m8","m10"):
        m,se=mse([r[k] for r in rs]); s+=f" {k}={m:.4f}+-{se:.4f}"
    m,se=mse([r["edge"] for r in rs]); s+=f" edge={m:.4f}+-{se:.4f}"
    if "ks_semicircle" in rs[0]:
        m,se=mse([r["ks_semicircle"] for r in rs]); s+=f" KS={m:.4f}+-{se:.4f}"
    s+=f" op2/m4={st.mean([r['edge']**2/r['m4'] for r in rs]):.3f}"
    print(s)
ver={dd:rs for (law,dd),rs in agg.items() if law=="veronese"}
print("Veronese-only momentfit:")
for k,ck in cat.items():
    ds=sorted(ver); Y=[st.mean([r[k] for r in ver[d]]) for d in ds]; SE=[sd([r[k] for r in ver[d]])/math.sqrt(len(ver[d])) for d in ds]
    sel=[i for i,d in enumerate(ds) if 40<=d<=140]
    b2,s2,c2,_=wls([ds[i] for i in sel],[Y[i] for i in sel],[1/SE[i]**2 for i in sel],2)
    b3,s3,c3,dof3=wls(ds,Y,[1/s**2 for s in SE],3)
    b2b,s2b,c2b,dof2b=wls(ds,Y,[1/s**2 for s in SE],2)
    print(f"  k={k} C={ck}: two-term(40-140) a={b2[0]:.3f}+-{s2[0]:.3f} ({(b2[0]-ck)/s2[0]:+.1f} se); two-term(all) a={b2b[0]:.3f}+-{s2b[0]:.3f} chi2={c2b:.1f}/{dof2b}; three-term(all) a={b3[0]:.3f}+-{s3[0]:.3f} b={b3[1]:.2f}+-{s3[1]:.2f} e={b3[2]:.1f}+-{s3[2]:.1f} chi2={c3:.1f}/{dof3} ({(b3[0]-ck)/s3[0]:+.1f} se)")
    b3c,s3c,_,_=wls(ds,Y,[len(ver[d]) for d in ds],3)
    print(f"        (count-weighted 3-term as refresh_p9 does: a={b3c[0]:.3f}+-{s3c[0]:.3f})")
d200=ver[200]; m,se=mse([r["m4"] for r in d200]); print(f"d=200 m4={m:.4f}+-{se:.4f} -> {(m-2)/se:.1f} se above 2")
# excess model c/d + e/d^2 on veronese-only excess over Catalan (for the sphere comparison)
for k,ck in cat.items():
    ds=sorted(ver); Y=[st.mean([r[k] for r in ver[d]])-ck for d in ds]; SE=[sd([r[k] for r in ver[d]])/math.sqrt(len(ver[d])) for d in ds]
    X=np.array([[1/d,1/d**2] for d in ds]); w=np.array([1/s**2 for s in SE]); y=np.array(Y)
    beta=np.linalg.solve(X.T@(X*w[:,None]),X.T@(w*y))
    print(f"  excess model k={k}: {beta[0]:.3f}/d + {beta[1]:.2f}/d^2 ; at d=16,24,32,40: {[round(beta[0]/d+beta[1]/d**2,4) for d in (16,24,32,40)]}")

# ---------------- D. Target 1 cgec
section("D. Target 1 p9_cgec")
agg=defaultdict(list)
for d in REC["p9_cgec"]:
    for r in d["records"]: agg[(r["d"],r["delta"],r["normalize_F"])].append(r)
for k in sorted(agg):
    rs=agg[k]; qv=[r["d_q11_var"] for r in rs]; lg=[r["L_rel_gap"] for r in rs]; rg=[r["risk_end_to_end_gap"] for r in rs]
    print(f"d={k[0]} delta={k[1]} normF={k[2]} n={len(rs)} dVar(q11)={st.mean(qv):.3f}+-{sd(qv):.3f} Lgap={st.mean(lg):.3f}+-{sd(lg):.3f} riskgap={st.mean(rg):.2e} F_colnorm_dev={st.mean([r['F_colnorm_dev'] for r in rs]):.3f} eps_d={REC['p9_cgec'][0].get('eps_d')}")

# ---------------- E. correction
section("E. p9_correction")
by=defaultdict(list)
for d in REC["p9_correction"]:
    lab=d["corpus"]+" "+(d.get("comp") if d["corpus"]=="emit" else d.get("band"))
    by[lab].append(d)
lams=None
for lab in sorted(by):
    ds=sorted(by[lab],key=lambda d:d["seed"]); gains=[];pg=[];hurt=0;ident=[];etas=[];bounds=[];signs=[];pm=[];pc=[]
    print(lab,"lanes",len(ds))
    for d in ds:
        rows=d["rows"]; lams=[r["lam"] for r in rows]
        best=min(rows,key=lambda r:r["R1_con"])
        g=100*(d["R0"]-best["R1_con"])/d["R0"]; gains.append(g)
        pgain=100*(best["phys_mean"]-best["phys_con"])/best["phys_mean"]; pg.append(pgain); pm.append(best["phys_mean"]); pc.append(best["phys_con"])
        hurt+=sum(1 for r in rows if not r["helps"]); ident.append(max(abs(r["identity_rel_err"]) for r in rows))
        etas.append(best["eta"]); bounds.append(best["eta_bound"]); signs.append((g>0)==(pgain>0))
        print(f"   seed {d['seed']}: R0={d['R0']:.4f} best lam={best['lam']:.0e} R1={best['R1_con']:.4f} gain={g:.1f}% phys {best['phys_mean']:.4f}->{best['phys_con']:.4f} ({pgain:.1f}%) margins: "+" ".join(f"{r['sign_margin']:+.3f}" for r in rows)+f" eta={best['eta']:.2f} bound={best['eta_bound']:.0f} identmax={max(abs(r['identity_rel_err']) for r in rows):.1e}")
    print(f"   => gain {st.mean(gains):.1f}+-{sd(gains):.1f}%  phys gain {st.mean(pg):.1f}+-{sd(pg):.1f}% (phys {st.mean(pm):.4f}->{st.mean(pc):.4f})  hurt {hurt}/{8*len(ds)}  worst ident {max(ident):.1e}  eta {min(etas):.2f}-{max(etas):.2f} bound {min(bounds):.0f}-{max(bounds):.0f} slack {min(b/e for b,e in zip(bounds,etas)):.0f}-{max(b/e for b,e in zip(bounds,etas)):.0f} sign-agree {sum(signs)}/{len(signs)}")
print("ridges:",lams)
allid=[abs(r["identity_rel_err"]) for d in REC["p9_correction"] for r in d["rows"]]; print("global worst identity rel err", max(allid), "n lanes", len(REC["p9_correction"]), "n (lane,ridge)", len(allid))
emit=[d for d in REC["p9_correction"] if d["corpus"]=="emit"]
print("EMIT all comps: hurt", sum(1 for d in emit for r in d["rows"] if not r["helps"]), "of", 8*len(emit))
for lab in sorted(by):
    ds=by[lab]
    print(lab, "helps by ridge (count of lanes helped / lanes):", [ (f"{lam:.0e}", sum(1 for d in ds for r in d['rows'] if r['lam']==lam and r['helps'])) for lam in lams], "lanes", len(ds))

# ---------------- F. prune
section("F. p9_prune")
blk=defaultdict(list); ad=defaultdict(list)
for d in REC["p9_prune"]:
    for r in d["records"]:
        if d["mode"]=="block": blk[(r["law"],r["n"],r["r"],r.get("aspect",0.5))].append(r)
        else: ad[(r["n"],r["theta"])].append(r)
for k in sorted(blk, key=lambda k:(k[0],k[3],k[1],k[2])):
    rs=blk[k]; be=[r["beta"] for r in rs]; ra=[r["ratio"] for r in rs]
    m,se=mse(be); rn=k[2]/k[1]
    print(f"{k[0]} n={k[1]} r={k[2]} asp={k[3]} N={len(rs)} beta={m:.4f}+-{se:.4f}(se) sd={sd(be):.4f} ratio={st.mean(ra):.3f} sqrt(r/n)={math.sqrt(rn):.4f} excess={m-math.sqrt(rn):+.4f} = {(m-math.sqrt(rn))/rn:.2f} x r/n")
def beta(law,n,r):
    rs=blk.get((law,n,r,0.5)); return st.mean([x["beta"] for x in rs]) if rs else None
for law in ("rademacher","bern02","gauss","exp1","t5"):
    for (r1,r2) in ((4,16),(16,64),(64,256),(16,256)):
        b1,b2=beta(law,1000,r1),beta(law,1000,r2)
        if b1 and b2: print(f"  {law} n=1000 exponent {r1}->{r2}: {math.log(b2/b1)/math.log(r2/r1):.3f}")
c=1.14
for (r,n) in ((16,1000),(32,2000),(64,4000),(64,1000),(128,2000),(256,4000),(16,4000),(16,2000)):
    b=beta("rademacher",n,r)
    if b: print(f"  ray r={r} n={n} r/n={r/n:.4f}: beta={b:.4f} law sqrt(r/n)+{c} r/n = {math.sqrt(r/n)+c*r/n:.4f}")
for k in sorted(ad):
    rs=ad[k]; print(f"adapt n={k[0]} theta={k[1]} N={len(rs)} indep overlap={st.mean([r['indep_overlap_u'] for r in rs]):.3f} adapt overlap={st.mean([r['adapt_overlap_u'] for r in rs]):.4f} min={min(r['adapt_overlap_u'] for r in rs):.4f} KS*n indep={k[0]*st.mean([r['indep_ks_bulk'] for r in rs]):.3f} adapt={k[0]*st.mean([r['adapt_ks_bulk'] for r in rs]):.3f} outlier adapt={st.mean([r['adapt_outlier'] for r in rs]):.3f} smax+theta={st.mean([r['smax'] for r in rs])+k[1]:.3f}")

# ---------------- G. gap (tab:gap)
section("G. p9_gap d=8 h=0.5")
agg=defaultdict(list)
for d in REC["p9_gap"]:
    for r in d["records"]:
        if r["d"]==8 and r["h"]==0.5: agg[r["k"]].append(r)
tot_n=set()
for k in sorted(agg):
    by=defaultdict(list); iso=defaultdict(list)
    for r in agg[k]: by[round(r["delta"],2)].append(r["risk_noise"]); iso[round(r["delta"],2)].append(r["tail_isotropy"]); tot_n.add(r["n"])
    ds=sorted(by); risks=[st.mean(by[x]) for x in ds]; isos=[st.mean(iso[x]) for x in ds]
    mono_r=all(risks[i]>risks[i+1] for i in range(len(risks)-1)); mono_i=all(isos[i]>isos[i+1] for i in range(len(isos)-1))
    print(f"k={k} deltas={ds} n/cell={[len(by[x]) for x in ds]} risk={[round(x,3) for x in risks]} mono={mono_r} iso={[round(x,3) for x in isos]} mono={mono_i}")
print("distinct n:",len(tot_n), "all (d,h) in p9_gap:", sorted(set((r['d'],r['h']) for d in REC['p9_gap'] for r in d['records'])))
print("p9_gap records per (d,h):", sorted(((k, sum(1 for d in REC['p9_gap'] for r in d['records'] if (r['d'],r['h'])==k))) for k in set((r['d'],r['h']) for d in REC['p9_gap'] for r in d['records'])))

# ---------------- H. regpath / gate / delta
section("H. regpath/gate/delta")
for d in REC["p9_regpath"]:
    for r in d["records"]:
        a_,r_=r["alpha_hat"],r["r_hat"]; e=2*a_*min(r_,1)/(1+2*a_*min(r_,1))
        print("regpath",r["corpus"],r["n"],"noise",r["noise"],"alpha",round(a_,3),"r",round(r_,3),"exp",round(r["crossover_exponent"],3),"lam_best",r["lam_best"],"interp/best",r["interp_over_best"],"rate exp",round(e,3),"10^exp",round(10**r["crossover_exponent"],2))
for d in REC["p9_gate"]:
    for r in d["records"]: print("gate",r["corpus"],r["mean"],"wd",r.get("wd"),"lam",r["lam"],"n",r["n"],"seed",r["seed"],"train_mse",r.get("mean_train_mse"),"theta",round(r["theta_hat"],3),"captured",round(r["gain_captured"],3),"risk mean/full/gated/best",r["risk_mean"],r["risk_full"],r["risk_gated"],r["risk_best"],"worsens",r["gated_worsens"],r["full_worsens"])
for d in REC["p9_delta"]:
    for r in d["records"]: print("delta",r["corpus"],"n",r["n"],"seed",r["seed"],"noise",r["noise"],"d_eff",r["d_eff0"],"part",round(r["participation"],2),"delta_eff",round(r["delta_eff"],3),"cert",round(r["certificate"],4),"risk interp",r["risk_interp"],"ridge",r["risk_ridge"],"lam_best",r["lam_best"],"adv",round(r["interp_advantage"],3))
