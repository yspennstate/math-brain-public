Runtime model: **GPT-5.6 Sol** (system runtime metadata). Requested GPT-6/maximum is not a configurable native setting here; reasoning-effort telemetry is **UNVERIFIED**.

# PROB10-03 — R14 bounded substantive iteration: variance-matched entropy cage

Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Status: **OPEN / PARTIAL / NO NEW SOURCE ENDPOINT / NEW COMPLETE ANALYTICAL REDUCTION**.

## 1. Contract, continuity, ownership, and consumed updates

Before new mathematics I consumed:

- `operations/PROB10_2026-09-20.md` on current `master`;
- root `POSTED.md`; the owner's posted Ising/zero-margin perceptron work remains a distinct exclusion and does not close this continuous negative-margin exact-sphere problem;
- `operations/claims/I0089.md`, preserving the old R14 perceptron handoff rather than rewriting history;
- `operations/claims/CAMPBELL-OROURKE-2022-Q1.8.md` and the immutable R14 refocus handoff `artifacts/prob10_2026-09-20/PROB10-03/20260919T2354Z_campbell_q18_r14_handoff.md`, preserving navigation point `3846db33296cfb6eea59ff7c488929087c7b62a2`;
- own newest preceding report `runs/prob10_2026-09-20/PROB10-03/20260920T0901Z_r14_projective_tail_continuation_91ad.md`;
- newest complementary NM13-03 third-full transport/LSI report `proofnet24/NM13-03/progress-perceptron-theory/runs/2026-09-20/2026-09-20__t03-transport-lsi-alpha122872223.md`;
- newest complementary NM13-07 entropy-dissipation / complete-second microextension report `proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/2026-09-20__t03-entropy-dissipation-sharp-microextend.md`.

The last item strictly moved the inherited repository-supported exact-sphere upper endpoint from `12.31963484` to

`alpha_U = 12.3196348278`.

That movement belongs to NM13-07 and is only consumed here. The retained SAT lower endpoint is

`alpha_L = 6.30297437506`.

Hence the entering and exiting source metric in this R14 run is

`6.01666045274 -> 6.01666045274`.

No canonical claim, peer report, scheduler state/cadence/enabled state, workflow, permission, email, Drive object, public posting, or concurrent worker file was modified.

## 2. Frozen source target and probability convention

Let

`M=floor(alpha N)`, `g_a iid N(0,I_N)`, `||sigma||_2=sqrt(N)` exactly,

and ask for

`<g_a,sigma> >= -sqrt(N)` for all `a<=M`.

A lower endpoint means SAT probability tends to one; an upper endpoint means SAT probability tends to zero as `N->infinity` at fixed `alpha`.

Smaller-radius algorithmic constructions, Ising restrictions, replica/full-RSB numerics, unsupported finite-lift stationary points, or a numerical ansatz are not promoted to source endpoints.

## 3. Source-scope refresh

I rechecked the requested primary sources and current follow-ups.

- El Alaoui--Sellke, `https://arxiv.org/abs/2010.15811`: the ambient model is the full radius-`sqrt(N)` spherical perceptron. For negative margin their algorithmic construction uses the conjectured FRSB/Parisi structure and outputs on radius `sqrt(qbar N)` with `qbar<1`; it is not an exact full-radius satisfiability-threshold theorem at `kappa=-1`.
- Stojnic, `https://arxiv.org/abs/1306.3980`: rigorous negative-margin RDT upper-bound machinery, not a closed exact-threshold theorem.
- Stojnic, `https://arxiv.org/abs/2312.16531`: complete stationarized fully lifted RDT and numerical finite-level evaluation; its own abstract says that making fl-RDT fully practically operational requires substantial numerical work. The repository therefore continues to require a proved analytical reduction plus outward-certified numerical realization before importing a finite-lift value as a source endpoint.
- The fresh 2026 search surfaced online/asymmetric **binary** perceptron work, which is a different model and does not close this exact spherical target.
- The previously consumed full-RSB and algorithmic follow-ups remain guidance rather than source closure for unrestricted exact-radius feasibility.

No new source found in this bounded check plainly closes the exact `kappa=-1` source target. This is dated negative evidence, not a worldwide novelty certificate.

## 4. Three materially different attacks

### Attack A — test the previous algebraic transport cage against the projective chart

This attack **failed decisively, with a proof of obstruction** rather than another numerical test.

The projective variables from the preceding R14 run are

`w0=1-p2`, `w1=p2-p3`, `w2=p3`,

`x=r0 r2/r1^2>1`, `y=r1/r2>1`,

`Z=x y^2 w0+y w1+w2`,

with

`q3=w2/Z`, `q2=(y w1+w2)/Z`.

The exact c-sector algebraic terms are

`A_c3=w1/(2Z)[w2+w1 k(y)]`,

`A_c2=w0/2[1-(xy^2w0/Z)h(x)]`,

where

`k(y)=y(y log y-y+1)/(y-1)^2`,

`h(x)=x(x-1-log x)/(x-1)^2`.

The NM13-03 transport/LSI cage gave

`w1 q3/2 <= A_c3 <= w1 q2/2`,

`w0 q2/2 <= A_c2 <= w0/2`.

I proved that these inequalities are automatic everywhere in the strict projective cone. Indeed `0<k(y)<y` and `0<h(x)<1`, and exactly

`A_c3-w1q3/2 = w1^2 k(y)/(2Z)>0`,

`w1q2/2-A_c3 = w1^2[y-k(y)]/(2Z)>0`,

`A_c2-w0q2/2 = (w0 a/2)[1-h(x)]>0`,

`w0/2-A_c2 = (w0 a/2)h(x)>0`,

with `a=xy^2w0/Z=1-q2`.

**Obstruction:** repeatedly shrinking boxes while using only that old algebraic cage can never remove a strict projective point. This route is now exhausted as a root-pruning method.

### Attack B — new variance-matched information projection

Instead of comparing an arbitrary tilted law directly with `N(0,1)`, first match its mean and variance.

For an absolutely continuous `nu` with mean `mu`, variance `v>0`, finite relative Fisher information `I=I(nu|gamma)` and `gamma=N(0,1)`, define

`G(mu,v)=1/2[mu^2+v-1-log v]`,

`J=I-mu^2-(v-1)^2/v`.

I proved

`boxed: G(mu,v) <= KL(nu||gamma) <= G(mu,v)+(v/2)J`,

and `J>=0`.

Proof: let `gamma_{mu,v}=N(mu,v)`. Moment matching gives the exact Pythagorean KL decomposition

`KL(nu||gamma)=KL(nu||gamma_{mu,v})+G(mu,v)`.

The relative Fisher score splits orthogonally into the score against `gamma_{mu,v}` and the affine score of `gamma_{mu,v}` against `gamma`, giving

`I(nu|gamma)=I(nu|gamma_{mu,v})+mu^2+(v-1)^2/v`.

Thus `J=I(nu|gamma_{mu,v})>=0`. Applying Gaussian LSI with variance `v` to the first KL term gives the upper bound. The lower bound is immediate from nonnegativity of that first KL term.

This is strictly stronger than the old mean/Fisher cage whenever the tilted variance differs materially from one.

### Attack C — exact H-elimination plus variance/Fisher compiler for the two perceptron tilts

This is a distinct analytical route aimed at certification cost: eliminate the innermost Gaussian `H` exactly and reduce the new cage to two-dimensional `U,V` integration.

Use

`m=c3/c2`, `B=c2/(4 gamma_sq)`, `s^2=1-p2`, `d^2=p2-p3`,

`X=dU+sqrt(p3)V-1`,

`f(x)=E_H exp[-B(x+sH)_+^2]`, `u=log f`.

For the inner tilted law `rho_x`, Gaussian integration by parts gives the exact identities

`mu_H=s u_x`,

`v_H=1+s^2u_xx`,

`I_H=-4B^2s^2u_B`.

The previously proved global kernel curvature bound gives

`1/(1+2Bs^2) <= v_H <= 1`.

For the outer tilted `U` law at fixed `V=v`, with tilted expectation `<.>_v`, a second Gaussian integration-by-parts identity gives

`mu_U=m d <u_x>_v`,

`v_U=1+m d^2<u_xx>_v+m^2d^2 Var_v(u_x)`,

`I_U=m^2d^2<u_x^2>_v`.

Concavity of `u` gives `v_U<=1`. With `L=2B/(1+2Bs^2)`, the potential curvature is at most `1+m d^2L`; a one-dimensional Cramer--Rao/integration-by-parts argument gives the quantitative lower bound

`v_U >= 1/(1+m d^2L)>0`.

Therefore the two c-sector entropies obey

`E_V G(mu_U,v_U) <= D_U <= E_V[G(mu_U,v_U)+(v_U/2)J_U]`,

and

`m E_V<G(mu_H,v_H)>_v <= D_H`

` <= m E_V<G(mu_H,v_H)+(v_H/2)J_H>_v`,

with the corresponding nonnegative `J_U,J_H`.

The innermost H expectation is itself closed form. Put

`A=1+2Bs^2`, `z=x/(s sqrt(A))`,

`C=A^(-1/2) exp(-B x^2/A)`, `mu0=x/A`, `tau=s/sqrt(A)`.

Completing the square gives

`f(x)=Phi(-x/s)+C Phi(z)`.

The unnormalized positive-part moments are

`M1+=C[mu0 Phi(z)+tau phi(z)]`,

`M2+=C[(mu0^2+tau^2)Phi(z)+mu0 tau phi(z)]`.

Hence, exactly,

`u_x=-2B M1+/f`,

`u_B=-M2+/f`,

`u_xx=-2B C Phi(z)/f+4B^2[M2+/f-(M1+/f)^2]`.

Thus a directed implementation of the new cage needs no H quadrature and no direct KL/log-partition subtraction. Only the outer `U,V` integration remains.

## 5. Executed tests and falsification

The proof was written first in

`artifacts/prob10_2026-09-20/PROB10-03/20260920T0948Z_r14_variance_matched_entropy_cage.md`.

I then executed

`artifacts/prob10_2026-09-20/PROB10-03/20260920T0950Z_r14_variance_matched_entropy_checker.py`,

with actual output archived at

`artifacts/prob10_2026-09-20/PROB10-03/20260920T0950Z_r14_variance_matched_entropy_checker.out`.

The exact symbolic section verifies all four projective-cage difference identities and the matched-Gaussian Fisher bookkeeping. The output ends

`ALL_SELF_CHECKS_PASS`.

These are self-checks, not independent audits.

For falsification, I evaluated the new cage at the NM13-03 supported third-full point near `alpha=12.2872223`, using Gaussian-Hermite orders 60, 80 and 120. The values are stable across those orders. At GH120:

old cage:

`D_U in [0.0283072730, 0.0790229969]`,

`D_H in [0.0301469922, 0.0472200078]`;

new variance-matched cage:

`D_U in [0.0408919618, 0.0555555182]`,

`D_H in [0.0346054428, 0.0367728964]`.

The companion's independently computed direct-KL numerical values

`D_U ~= 0.0449879568`, `D_H ~= 0.0351983097`

lie inside the new cages. Numerically, the cage widths shrink by about `71.1%` and `87.3%`, respectively.

All of these candidate-point values are **NUMERICAL ONLY**. They are not outward intervals and are not promoted to a source endpoint.

## 6. Before/after metric and auxiliary movement

### Source-level metric

Before this run:

`[6.30297437506, 12.3196348278]`, width `6.01666045274`.

After this run:

`[6.30297437506, 12.3196348278]`, width `6.01666045274`.

**Source movement: none.**

### Auxiliary/mechanism movement

1. The old algebraic transport/LSI cage is now proved incapable of pruning any strict point in the projective third-full cone. This is a permanent obstruction, not another unchanged numerical run.
2. A new two-sided variance-matched KL/Fisher inequality is proved.
3. Exact variance and Fisher identities are proved for both nested perceptron tilts.
4. The innermost H integration is eliminated in closed form.
5. At the supported third-full point the numerical c-sector cage width drops by about `71%` for the outer entropy and `87%` for the inner entropy.

## 7. Remaining full-scope gap

The exact problem remains **OPEN / PARTIAL**. The numerical third-full capacity zero near `12.28722222...` remains conditional.

The next source-moving obligation is now sharper: construct an outward interval/Krawczyk (or equivalent fixed-point) certificate for the strict complete-third stationary system at a positive comparison gap. The new cage should first be used to certify the c-sector face signs using only `u_x,u_xx,u_B` and outer score moments. Only if those refined cages still straddle zero should the exact entropy-dissipation integrals be evaluated on the final surviving boxes.

A successful root certificate must still be tied to the exact source-matched stationarized fl-RDT implication and then independently reviewed under the repository closure standard. No ansatz, floating-point root, or simulation becomes an endpoint before that step.
