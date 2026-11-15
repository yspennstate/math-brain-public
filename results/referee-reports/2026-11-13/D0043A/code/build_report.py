"""Assemble the self-contained report, evidence summary and original plots."""
import os
for key in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS','MKL_NUM_THREADS']:
    os.environ[key]='1'
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
os.environ['MPLCONFIGDIR']=str(ROOT/'data/.mplconfig')
os.environ['XDG_CACHE_HOME']=str(ROOT/'data/.cache')
import csv,json,platform,resource,sys
import numpy as np
import scipy
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from collections import defaultdict
from datetime import datetime

assert os.getpriority(os.PRIO_PROCESS,0)>=10
DATA=ROOT/'data'
groups=defaultdict(list)
for r in csv.DictReader((DATA/'artificial_eigenvalues.csv').open()):
    groups[(r['model'],int(r['beta']),int(r['n']))].append(-float(r['lambda0']))
quartic=json.loads((DATA/'quartic_banded_diagnostics.json').read_text())
qraw=list(csv.DictReader((DATA/'quartic_banded_eigenvalues.csv').open()))
gamma=2**(-6/7);c=6**(2/7);ratio=gamma/c
lines=['# Numerical evidence and checks','',
'The proof is independent of these computations. Random seeds and numerical settings are in the code; individual eigenvalues and diagnostics are in data/. All calculations ran at inherited nice10 with one numerical thread, below4GB. The largest recorded RSS among the experiment processes was204MB; the spectral/HMC runs used at most142MB. No dense n×n matrix was used for n=10000 or100000. Tridiagonal bisection computes the first three eigenvalues in linear storage; a sparse shift-invert calculation independently checked an artificial sample.',
'','## Independent critical profile and operator discretization','',
'The artificial matrices in SCALING.md use standardized centered χ₁ diagonal noise and exact integrated variance in each cell. There are96 independent samples at each β,n. The operator discretization uses Gaussian increments with that same exact cell variance, not a singular point evaluation at t=0. Meshes h=.025 and.0125 span length128. Entries below are sample means of −λ₀, followed by sample standard deviations in parentheses. These are Monte Carlo summaries, not exact limiting means.','',
'| β | χ profile n=10000 | χ profile n=100000 | Gaussian h=.025 | Gaussian h=.0125 |',
'|---|---:|---:|---:|---:|']
def fmt(v):return f'{np.mean(v):.4f} ({np.std(v,ddof=1):.4f})'
for beta in [1,2,4]:
    keys=[('chi',beta,10000),('chi',beta,100000),('gaussian',beta,5120),('gaussian',beta,10240)]
    lines.append('| '+str(beta)+' | '+' | '.join(fmt(groups[k]) for k in keys)+' |')
mesh=json.loads((DATA/'coupled_mesh.json').read_text())
lines+=['','A separate96-sample coupled-Brownian refinement check aggregates pairs of fine increments to build the coarse mesh. The root-mean-square changes in the ground eigenvalue from h=.025 to.0125 were '+', '.join(f'β={r["beta"]}: {r["mesh_rms"][0]:.5f}' for r in mesh)+'. Restricting the same paths from length128 to64 changed the first three eigenvalues by at most '+f'{max(max(r["boundary_max"]) for r in mesh):.2g}'+'. This last number is an observed finite-sample boundary check at numerical precision, not a uniform probabilistic bound. The deterministic mesh/boundary check is also saved.','',
'## Genuine critical quartic','',
'The target is exactly the KRV entry density with V=U/2, U=x⁴/20−4x³/15+x²/5+8x/5. In q_i=log b_i coordinates its negative log density is nβ trU(T)/2−βΣ(n−i)q_i; the Jacobian is included. Metropolis-corrected HMC updates all2n−1 entry variables. A fixed pentadiagonal Hessian mass at the finite-n mode accounts for the coefficient correlations. Cholesky factors and triangular solves use linear storage. The mass matrix is fixed throughout a chain; its use does not approximate the target. At each n=256,1000,10000 and β=1,2,4, two chains used300 warm-up trajectories, then400 retained draws per chain, thinning2. Step-size adaptation ends before retained sampling. Last sampled a,b vectors are saved in NPZ files.',
'',
'An earlier diagonal-preconditioned run failed mixing diagnostics (split R-hat as high as2.60 and ESS below20); its raw data and diagnostics are retained but excluded from the summaries below. The banded run had split R-hat0.9995–1.0323 and within-chain autocorrelation ESS118–601 per800 draws. These basic diagnostics support exploratory comparisons but are not proof of stationarity, independence or rare-tail accuracy. There were no recorded divergent trajectories, and no Hessian diagonal shift was needed.','',
'| n | β | mean c n^(2/7)(λmax−2) | sample SD | split R-hat | estimated ESS |',
'|---:|---:|---:|---:|---:|---:|']
for r in quartic:
    dg=r['diagnostics']
    lines.append(f'| {r["n"]} | {r["beta"]} | {r["mean_cv"]:.4f} | {r["sd_cv"]:.4f} | {dg["split_rhat"]:.4f} | {dg["ess_within_chains"]:.1f} |')
lines+=['','Here c=6^(2/7) is the Claeys–Vanlessen kernel normalization. To compare with the displayed operator using the *formal deterministic drift* calculation, multiply these scaled eigenvalues by γ/c, where γ=2^(−6/7). This constant is derived algebraically in SCALING.md and is not fitted. For n=10000:','',
'| β | quartic formal-scale mean | approximate MC SE | Gaussian operator mean | independent-sample SE |',
'|---|---:|---:|---:|---:|']
for beta in [1,2,4]:
    r=next(v for v in quartic if v['n']==10000 and v['beta']==beta)
    v=groups[('gaussian',beta,10240)]
    lines.append(f'| {beta} | {ratio*r["mean_cv"]:.4f} | {ratio*r["sd_cv"]/np.sqrt(r["diagnostics"]["ess_within_chains"]):.4f} | {np.mean(v):.4f} | {np.std(v,ddof=1)/np.sqrt(len(v)):.4f} |')
fu=json.loads((DATA/'finite_unitary_check.json').read_text())
checks=json.loads((DATA/'model_checks.json').read_text())
lines+=['','The mismatch of sample means under this formal normalization is evidence only. It cannot exclude another constant normalization; the rigorous tail argument excludes every fixed positive normalization.','',
'## Independent β=2 finite-n check and limiting-law computation','',
f'For n=256, a separate quadrature projection-kernel computation approximated the largest-eigenvalue CDF of the genuine unitary quartic ensemble. It used fully reorthogonalized weighted polynomials on [−3.5,6], with4096 and8192 Gauss–Legendre nodes. The maximum CDF change on45 comparison points was {fu["cdf_max_grid_difference"]:.5f}; the orthogonality residual was below {max(fu["orthogonality"]):.2g}. The800 HMC draws differed from the finer-grid CDF by at most {fu["empirical_max_grid_difference"]:.5f} on this grid. This is a quadrature consistency and sampler check, not an independent-sample goodness-of-fit test. Domain truncation and quadrature error are not certified.',
'',
'An initial quadrature attempt formed exp(−n(U−minU)) before taking its square root; this underflowed near the edge and was rejected. The corrected code exponentiates half the exponent before normalizing. The final projection is checked for finiteness and orthogonality. This matters even at n=256.',
'',
'The limiting higher-order TW₂ Fredholm determinant itself was not evaluated. Claeys–Olver1111.3527 describes numerical RH/Fredholm evaluation, but a verified implementation was not available in this workspace. The finite-n determinantal CDF above is explicitly distinguished from that limiting law. The rigorous comparison uses the published critical-kernel right-tail estimate, not an ordinary TW₂ approximation.',
'',
'## Algebra, solver and tail checks','',
f'- Direct trace-vs-dense-eigenvalue action error: {checks["trace_error"]:.3g}.',
f'- Exact quartic gradient vs centered finite differences: maximum error {checks["gradient_max_error"]:.3g}.',
f'- The banded analytic Hessian vs independently differenced gradients: maximum error {checks["hessian_max_error"]:.3g}.',
f'- Tridiagonal eigenvalue solver vs sparse shift-invert, n=10000: maximum error {checks["eigensolver_error"]:.3g}.',
'- SymPy rederived the edge powers, the local quartic equations, x=D³/8+O(D⁴), c=2, and γ=2^(−6/7). Direct integration of the equilibrium density gives total mass0.9999999999916908; its Stieltjes transform independently has leading term1/z.',
'- Exact Gaussian log probabilities of the trial-function events are tabulated for k=0,1,2, β=1,2,4 and s=1,…,4096 in rayleigh_tail.csv. These are probabilities of a variational *sufficient event*, hence rigorous-formula lower bounds on an operator tail, not sampled eigenvalue-tail probabilities or estimates of its exact exponent.',
'',
'Original plots: `data/eigenvalue_comparison.png`, `data/unitary_cdf_check.png`, and `data/trial_tail_powers.png`. No paper images or scans are present.','',
'The final integrity audit (`code/audit.py`, results in `data/audit.json`) checks source-text hashes, PDF absence, report control characters, all saved row counts and sampled-matrix dimensions, numerical summary consistency, and the Gaussian trial-event power calculations. Mathematical proof steps were audited separately and matched to Baslingker\'s theorem.','',
'## Reproduction','',
'From this directory, with nice≥10 and one numerical thread:',
'','```sh',
'OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 code/check_algebra.py',
'OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 code/verify_models.py',
'OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 code/run_experiments.py artificial --draws 96',
'OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 code/run_experiments.py quartic --ns 256 1000 10000 --banded --burn 300 --draws 400 --thin 2',
'OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 code/coupled_mesh.py',
'OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 code/finite_unitary.py',
'OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 code/run_experiments.py tail',
'OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 code/build_report.py',
'```','',
'If the shell is not already at nice10, prefix the Python command with `nice -n 10`; the scripts check inherited priority. Sources can be regenerated with code/acquire.py and the URLs in sources/manifest.json. Versions and resource metadata are saved in data/environment.json.']
num='\n'.join(lines)+'\n'
(ROOT/'NUMERICS.md').write_text(num)

plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})
fig,axs=plt.subplots(1,3,figsize=(12,3.6),sharex=True,sharey=True)
for ax,beta in zip(axs,[1,2,4]):
    curves=[('operator h=.0125',groups[('gaussian',beta,10240)]),
            ('artificial chi n=100000',groups[('chi',beta,100000)]),
            ('quartic n=10000, formal scale',[ratio*float(r['cv_scaled_top0']) for r in qraw if int(r['n'])==10000 and int(r['beta'])==beta])]
    for label,v in curves:
        v=np.sort(v);ax.step(v,np.arange(1,len(v)+1)/len(v),where='post',label=label)
    ax.set_title(f'beta = {beta}');ax.set_xlim(-4,3);ax.set_xlabel('scaled top eigenvalue');ax.grid(alpha=.2)
axs[0].set_ylabel('empirical CDF');axs[2].legend(fontsize=7,loc='lower right')
fig.suptitle('Finite samples; quartic normalization is derived from the formal drift')
fig.tight_layout();fig.savefig(DATA/'eigenvalue_comparison.png',dpi=160);plt.close(fig)
tab=np.genfromtxt(DATA/'finite_unitary_cdf.csv',delimiter=',',names=True)
fig,ax=plt.subplots(figsize=(6,4))
ax.plot(tab['cv_scaled_s'],tab['cdf_8192'],label='quartic n=256, projection quadrature')
ax.step(tab['cv_scaled_s'],tab['hmc_empirical'],where='mid',label='quartic n=256, HMC')
ax.set(xlabel='Claeys–Vanlessen scaled top eigenvalue',ylabel='CDF',title='Finite-n unitary sampler check')
ax.legend(fontsize=8);ax.grid(alpha=.2);fig.tight_layout();fig.savefig(DATA/'unitary_cdf_check.png',dpi=160);plt.close(fig)
tab=np.genfromtxt(DATA/'rayleigh_tail.csv',delimiter=',',names=True)
fig,ax=plt.subplots(figsize=(6,4))
for k in [0,1,2]:
    rows=tab[(tab['k']==k)&(tab['beta']==2)]
    ax.loglog(rows['s'],-rows['log_probability'],marker='.',label=f'k={k}, trial event; power {(4*k+3)/(4*k+2):.3g}')
ax.set(xlabel='s',ylabel='minus log(trial-event probability)',title='Exact Gaussian variational lower-bound events')
ax.legend(fontsize=8);ax.grid(alpha=.2);fig.tight_layout();fig.savefig(DATA/'trial_tail_powers.png',dpi=160);plt.close(fig)

env=dict(date=datetime.now().astimezone().isoformat(),python=sys.version,numpy=np.__version__,
 scipy=scipy.__version__,matplotlib=matplotlib.__version__,platform=platform.platform(),
 nice=os.getpriority(os.PRIO_PROCESS,0),thread_environment={k:os.environ.get(k) for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS']},
 builder_maxrss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
try:
    from threadpoolctl import threadpool_info
    env['threadpools']=threadpool_info()
except ImportError:pass
(DATA/'environment.json').write_text(json.dumps(env,indent=2)+'\n')

lead=r'''COUNTEREXAMPLE

# D0043: the displayed exotic-edge operator is already disproved

The conjecture fails for k=1, β=2. This is a known result: Jnaneshwar Baslingker, *Stochastic domination in beta ensembles*, J. Math. Phys. 66, 053303 (2025), DOI [10.1063/5.0254593](https://doi.org/10.1063/5.0254593), **Theorem 4 in [arXiv:2304.09236v2](https://arxiv.org/abs/2304.09236v2), PDF p. 7**, with proof on pp. 10–12. The theorem number and pages here are verified against the saved arXiv text; the journal abstract confirms the result, but the journal PDF was inaccessible. No new resolution is claimed.

The obstruction is in the right tail. The displayed Gaussian operator gives P(−λ₀>s)≥exp(−Cs^(7/6)), while the critical unitary quartic kernel forces any largest-eigenvalue limit to have P(X>s)≤Cexp(−cs^(7/2)). Fixed positive rescaling cannot reconcile these powers. We give complete proofs of the operator construction and contradiction, explain what survives the formal scaling argument, and prove convergence of an artificial independent-chi model to this operator. Numerical comparisons are evidence only.

## Exact statement and meaning

Virág, *Operator limits of random matrices*, [arXiv:1804.06953](https://arxiv.org/abs/1804.06953), PDF p.14, states exactly:

> **Conjecture 5.** After scaling, T_n converges to the random operator
>
> $S_{\beta,k}=-\partial_t^2+t^{1/(2k+1)}+\frac{2}{\sqrt\beta}t^{-k/(2k+1)}b'_t.$

Here T_n is the KRV random Jacobi matrix of a polynomial-potential β-ensemble with independent Dirichlet spectral weights. KRV's more precise formulation is Conjecture45 in the saved arXiv version, PDF p.57 (published numbering13.1). It stipulates the half-line, Dirichlet boundary and Theorem9(i) convergence: the ordered low eigenvalues and embedded eigenvectors of the scaled EI−T_n converge jointly. This entails convergence of the scaled largest matrix eigenvalue to −λ₀ of the proposed operator. The explicit counterexample below uses the confining quartic U with V=U/2 in KRV's convention; it has one-cut equilibrium density vanishing to order5/2 at its right edge.

The status is COUNTEREXAMPLE rather than RESOLVED_IN_LITERATURE because the stipulated positive-theorem early-stop condition is not met: the printed theorem disproves the proposed limit. The correct general critical-edge random operator is not identified here. The certified negative scope is k=1,β=2; no classification for all k or β is claimed.

'''
parts=[lead,(ROOT/'PROOF.md').read_text(),(ROOT/'SCALING.md').read_text(),num,(ROOT/'LITERATURE.md').read_text(),
       '\nTask: “Open problem D0043” — 13 November2026, approximately10:40 Asia/Tbilisi (first recorded session time).\n']
(ROOT/'REPORT.md').write_text('\n\n'.join(parts))
print('Wrote REPORT.md, NUMERICS.md and three original PNG plots',flush=True)
