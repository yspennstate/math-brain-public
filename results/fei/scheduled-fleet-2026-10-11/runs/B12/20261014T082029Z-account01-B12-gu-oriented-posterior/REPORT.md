# B12 / A058 — oriented posterior kernel and rare-activation separation

**Run:** `20261014T082029Z-account01-B12-gu-oriented-posterior`  
**Stable gap:** `B12-A058-SHARED-COORDINATE-OVERLAP`  
**Attempt:** `A058-GU-ORIENTED-POSTERIOR-12`  
**Status:** exact oriented decomposition PROVED pending independent review;
posterior-only projection REFUTED parametrically; universal GU OPEN.

## Frozen candidate

Candidate: carry the companion factor label through the two-sign posterior
tree and use its root KL plus restriction drift to pay the realized-sign
projection.  Quantitatively, seek a dimension-free coefficient controlling
the oriented `U/G` projection by `K` and `LK`.

Prior status: the unordered two-sign center was exactly `M-K`, but a finite
three-bit pair had `K=0`, positive active companion, and adverse `LK`.  The
remaining product remainder was known exactly, but the sign-selected part had
not been written coefficientwise.

Universal implication: for fixed `a>=0,0<=b<1`, the new exact split is

\[
D_{a,b}(f_\pm)=\mathcal C_{a,b}\pm\mathcal O_{a,b}.
\]

Thus the dimension-free condition

\[
\mathcal C_{a,b}+|\mathcal O_{a,b}|\le0
\]

for a companion construction covering every Boolean function proves
universal GU, then
`H<=(2+2a/(1-b))I`.  No overlap, activation, depth, bias or fresh-variable
hypothesis appears in this implication.

## Result

Writing

\[
t=(p_+-p_-)/(p_++p_-),\qquad
u=(\pi_+-\pi_-)/(\pi_++\pi_-),
\]

the exact sign-oriented kernel is

\[
\Omega(t,u;L)=tL+
\frac{1+t}{2}\log_2\frac{1+u}{1+t}
-\frac{1-t}{2}\log_2\frac{1-u}{1-t}.
\]

With `Z_U=sum q Omega` and
`Z_I=(I_+-I_-)/2`,

\[
U(f_\pm)=M-K\pm Z_U,
\]

\[
G(f_\pm)=LM-LK\pm LZ_U,
\]

and

\[
\mathcal C_{a,b}=LM-a\bar I-bM+bK-LK,
\quad
\mathcal O_{a,b}=LZ_U-aZ_I-bZ_U.
\]

The KL kernel is even under swapping actual and companion, while `Omega` is
odd.  Consequently a branchwise reserve constructed only from the unordered
pair, `K`, or its restriction drift cannot encode which physical sign is the
actual one.

## Parametric falsifier

Let `f_n` be the Boolean function with one negative point on the `n`-cube and
let its companion be constant.  For `N=2^n` and
`p_0=(1-2/N)^2`, exact formulas give

\[
U_n=p_0\log_2(1/p_0)+\frac4{N^2}(n2^{n-1}-n),
\]

\[
K_n=\frac12\left[p_0\log_2\frac{2p_0}{1+p_0}
+\log_2\frac2{1+p_0}\right],
\]

\[
G_n=n(U_n-U_{n-1}/2),\qquad
LK_n=n(K_n-K_{n-1}/2).
\]

As `n` grows,

\[
K_n\sim\frac{2}{\ln2}N^{-2},
\quad Z_U\sim(n+2/\ln2)N^{-1},
\]

\[
LK_n\sim-\frac{2n}{\ln2}N^{-2},
\quad LZ_U\sim nN^{-1}.
\]

Therefore both `|Z_U|/K` and
`|LZ_U|/(K+|LK|)` diverge exponentially.  At `n=12` the certified ratios are
`21119.468...` and `1319.534...`, respectively.  No finite multiplier of the
root posterior or complete posterior drift can pay the selected sign.

This is not a GU or FEI counterfamily: `Z_I=n/N` and `LZ_U/Z_I ->1`, so
source influence remains at the correct first-order rare scale.  The
mechanism failure is specifically the quadratic posterior reserve versus the
linear oriented activation cost.

## Verification

The checker verifies the complete oriented `U/G/GU` decomposition on all
65,808 ordered Boolean pairs through dimension three and 240 deterministic
random pairs through dimension seven.  It directly constructs the rare
family through dimension twelve and checks the closed-form asymptotics at
dimension thirty without enumerating that cube.

## Next unpaid step

Replace the sign-even KL martingale by a signed likelihood-score/influence
martingale based on `Omega`.  Freeze an inequality paying
`LZ_U-bZ_U` from `aZ_I` plus one terminal oriented score; test its constant on
the one-point-defect family, the positive three-bit collision tensor, and the
zero-`K` isometric pair.

Full details are in `PROOF.md`; commands and source pins are archived.
Independent review and native Brain ingestion are not observed.
