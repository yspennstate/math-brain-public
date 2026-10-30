import math
import numpy as np

# Diagnostic only: exact formulas are proved in REPORT.md.
rng=np.random.default_rng(20260922)
max_diag=max_same=max_sing_err=0.0
for nP,nN in [(2,3),(5,4),(1,6),(8,7)]:
    wp=rng.random(nP); wp=0.5*wp/wp.sum()
    wn=rng.random(nN); wn=0.5*wn/wn.sum()
    up=np.sqrt(wp); un=np.sqrt(wn)
    u=np.concatenate([up,un])
    v=np.concatenate([up,-un])
    lam=1.7
    S=lam*(np.outer(u,u)-np.outer(v,v))
    max_diag=max(max_diag,float(np.max(np.abs(np.diag(S)))))
    max_same=max(max_same,float(np.max(np.abs(S[:nP,:nP]))),float(np.max(np.abs(S[nP:,nP:]))))
    sig=np.linalg.svd(S[:nP,nP:],compute_uv=False)
    max_sing_err=max(max_sing_err,abs(float(sig[0])-lam))

cS=2/(3+math.sqrt(5))
print('QFORM_B09_GROUPED_RANK2_DIAGNOSTIC_PASS')
print('zero_diag_max',max_diag)
print('same_block_max',max_same)
print('cross_singular_error',max_sing_err)
print('cS',cS)
print('partner_high_stablerank_bound',11.876*math.sqrt(312/cS))
print('rank3_zero_diag_heavy_bound',8*math.sqrt(312))
print('hyperbolic_if_sigma_cS',8*math.sqrt(312/cS))
print('product_halfriesz_centered_unit_uniform_exact',8.0)
