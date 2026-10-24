# account04/B13 — all boundary faces of the antipodal gate are safe for the stable FEI candidate

**Classification:** `ESSENTIAL_STEP_APPLIED`.  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 0. Live target and why this run changed mechanism

The active source-exact target is the all-gate inequality

\[
D_\Gamma(G;p):=
\sum_i \frac{\operatorname{It}_i(G;p)}{V_{p_i}}
\bigl(\Gamma(p_i)+h_2(V_{p_i})\bigr)
-\Gamma(p_{\rm out})-\widetilde H_G(p)\ge0,
\qquad V_u=4u(1-u).
\tag{0.1}
\]

The stable candidate inherited from account01/B18 is

\[
C_*=6.5218512,
\qquad
\Gamma_*(u)=\Gamma_{\rm RO}(u)+a_*u(1-u),
\qquad a_*=0.2682048.
\tag{0.2}
\]

The newest compatible other-account result consumed in this run is account02/B18,

`proofnet24/P03-fei/fleet-2026-09-21/account02/B18/20260922T040428Z-random-block-currency/REPORT.md`,
report blob `bd4972b11cb13989282f555deb9354509d1da590`.

It proves the exact random fixed-size restriction identity

\[
D_*(G)-\mathbb E_{A,X_A}D_*(G_{A=X_A})
=B_r^{\rm RO}(G)+a_*Q_r
\tag{0.3}
\]

and shows that a minimal counterexample would have to make the right side negative at **every** scale `1<=r<n`. This changes the proof architecture here: I do not try to prove a pointwise one-pivot margin bound. Instead I work at the whole-gate level and, for the antipodal gate, identify the terminal block `r=d-1`, where every child is a constant or a literal, so its stable defect is exactly zero. Thus

\[
B_{d-1}^{\rm RO}(\operatorname{EQ}_d)+a_*Q_{d-1}
=D_*(\operatorname{EQ}_d).
\tag{0.4}
\]

The newest account03/B13 bent-swap report,

`proofnet24/P03-fei/fleet-2026-09-21/account03/B13/20260922T040037Z-bent-swap-local-margin/REPORT.md`,
report blob `3f3e5294853654e0539f2e11fad49a3fed344136`,

independently makes this mechanism choice necessary: it gives genuine Boolean restriction pairs for which the one-pivot local correction request is unbounded. The aggregate block identity survives that refutation; a universal pointwise local cap does not.

This report proves that the terminal block quantity (0.4) is positive in a full neighborhood of **every boundary face** of the bias cube for each fixed antipodal gate `EQ_d`. Hence any stable-candidate counterexample in this family is confined to a compact interior bias box.

## 1. Exact antipodal formulas inherited from the previous B13 run

Let `d>=3` and

\[
\operatorname{EQ}_d=1_{\{0^d,1^d\}}.
\]

For independent biases `p_i in (0,1)`, put

\[
P=\prod_i p_i,\qquad Q=\prod_i(1-p_i),\qquad r=P+Q.
\tag{1.1}
\]

The previous account04/B13 report

`proofnet24/P03-fei/fleet-2026-09-21/account04/B13/20260922T0324Z-arbitrary-bias-eq-boundary/REPORT.md`,
blob `58bc9653da0a1db3514c927bc0a88c78b695e10c`,

proved for every nonempty spectral set `S`

\[
\widehat f(S)=-2\left[
P\prod_{i\in S}\sqrt{\frac{1-p_i}{p_i}}
+(-1)^{|S|}Q\prod_{i\in S}\sqrt{\frac{p_i}{1-p_i}}
\right]
\tag{1.2}
\]

and

\[
\frac{\operatorname{It}_i(\operatorname{EQ}_d;p)}{V_{p_i}}
=P_{-i}+Q_{-i}.
\tag{1.3}
\]

Hence

\[
D_*^{\rm EQ}(p)=
\sum_i(P_{-i}+Q_{-i})
\bigl(\Gamma_*(p_i)+h_2(V_{p_i})\bigr)
-\widetilde H_{\rm EQ}(p)-\Gamma_*(P+Q).
\tag{1.4}
\]

The same report closed every fixed-ratio rare-corner ray. Account01/B16 then closed the remaining hierarchical simultaneous rare-corner escape in

`proofnet24/P03-fei/fleet-2026-09-21/account01/B16/20260922T0350Z-eq-hierarchical-rare-corner/REPORT.md`,
blob `c9948163945cd230dd97cf3b192228dc51df5bdf`: for each fixed `d`, there is a neighborhood of the all-zero corner, and by symmetry of the all-one corner, on which `D_*^{EQ}>0` with no assumption on bias ratios.

The unresolved boundary geometry after those two results is therefore the collection of mixed and lower-dimensional faces.

## 2. Exact whole-gate two-corner decomposition

Let `A_d` be the one-corner gate supported only at `1^d`, and `B_d` the one-corner gate supported only at `0^d`, with the same sign convention used in the source gate functional. Let their spectral entropies be `H_A,H_B`, and write `H_E` for the entropy of `EQ_d`.

Because the normalized influence contribution of `EQ_d` is exactly the sum of the two one-corner contributions, direct subtraction of the three gate defects gives the identity

\[
\boxed{
D_*^{\rm EQ}
=D_*^{A}+D_*^{B}
+\Gamma_*(P)+\Gamma_*(Q)-\Gamma_*(P+Q)
-E_H,
}
\tag{2.1}
\]

where

\[
E_H:=H_E-H_A-H_B.
\tag{2.2}
\]

This identity is global. It keeps the complete read-once slack of both one-corner gates and does not decompose the proof into pointwise pivot margins.

Both `A_d` and `B_d` are read-once AND/OR/NOT formulas. The certified read-once potential is

\[
\Gamma_{\rm cert}=\Gamma_{\rm RO}+0.01u(1-u),
\]

while

\[
\Gamma_* = \Gamma_{\rm cert}+\kappa u(1-u),
\qquad \kappa=0.2582048.
\]

The quadratic-lift identity therefore yields

\[
D_*^A\ge \kappa W_A\ge0,
\qquad
D_*^B\ge \kappa W_B\ge0.
\tag{2.3}
\]

## 3. Entropy interaction is only an `O(PQ log(1/PQ))` term when both corners are rare

Let `mu_A,mu_B,mu_E` be the squared biased-Walsh laws of `A_d,B_d,EQ_d`. Their nonempty spectral masses for the one-corner laws sum to

\[
X=4P(1-P),\qquad Y=4Q(1-Q).
\tag{3.1}
\]

When `X+Y<1`, define a comparison probability law `nu` by

\[
\nu_\emptyset=1-X-Y,
\qquad
\nu_S=\mu_A(S)+\mu_B(S)\quad(S\ne\emptyset).
\tag{3.2}
\]

### Lemma 3.1 — comparator entropy is subadditive

\[
\boxed{H(\nu)\le H(\mu_A)+H(\mu_B).}
\tag{3.3}
\]

#### Proof

Normalize the two nonempty tails. Entropy of a mixture is at most the weighted component entropies plus the binary mixing entropy, giving

\[
(X+Y)H\!\left(\frac{\mu_A^{\ne\emptyset}+\mu_B^{\ne\emptyset}}{X+Y}\right)
\le XH\!\left(\frac{\mu_A^{\ne\emptyset}}X\right)
+YH\!\left(\frac{\mu_B^{\ne\emptyset}}Y\right)
+(X+Y)h_2\!\left(\frac X{X+Y}\right).
\]

Also

\[
h_2(X+Y)+(X+Y)h_2\!\left(\frac X{X+Y}\right)
\le h_2(X)+h_2(Y),
\]

which is ordinary Shannon subadditivity for two mutually exclusive indicator events of probabilities `X` and `Y`. Adding the tail terms gives (3.3). `QED`

### Lemma 3.2 — exact antipodal total-variation interaction

For every nonempty `S`, if `a_S,b_S` are the one-corner biased-Walsh coefficients, then

\[
|2a_Sb_S|=8PQ,
\tag{3.4}
\]

because the two normalized one-bit basis values multiply to `-1`. The empty mass differs by the same absolute amount `8PQ`. Therefore, on the `2^d`-point spectral alphabet,

\[
\boxed{
\|\mu_E-\nu\|_1=8\,2^d PQ,
\qquad
\delta_{TV}=2^{d+2}PQ.
}
\tag{3.5}
\]

For sufficiently small `PQ`, Fannes--Audenaert gives

\[
H_E-H(\nu)
\le
\omega_d(P,Q)
:=h_2(2^{d+2}PQ)
+2^{d+2}PQ\log_2(2^d-1).
\tag{3.6}
\]

Combining (3.3) and (3.6),

\[
\boxed{E_H\le\omega_d(P,Q)=O_d\!\left(PQ\log\frac1{PQ}\right).}
\tag{3.7}
\]

No ambient dimension multiplies a cube-measure error here; for fixed gate arity, the interaction is charged directly to the product of the two exceptional-corner masses.

## 4. The mixed-corner potential term beats the spectral interaction for every relative rate

The source implementation of the stable potential has an exact terminal tail of the form

\[
\Gamma_*(z)=A z\log_2(1/z)+Bz-a_*z^2,
\qquad A=4.9096>0,
\tag{4.1}
\]

once `z` is sufficiently small. Hence, whenever `P,Q,P+Q` are all in this tail,

\[
\boxed{
\Gamma_*(P)+\Gamma_*(Q)-\Gamma_*(P+Q)
=A(P+Q)h_2\!\left(\frac{P}{P+Q}\right)+2a_*PQ.
}
\tag{4.2}
\]

Put

\[
m=\min(P,Q),\qquad M=\max(P,Q),\qquad R=\log_2(M/m).
\]

For `x=m/(M+m)<=1/2`, concavity of binary entropy above its endpoint chord and the first entropy term separately give

\[
(M+m)h_2(x)\ge 2m,
\qquad
(M+m)h_2(x)\ge mR.
\tag{4.3}
\]

On the other hand, (3.7) is at most a fixed `d`-dependent constant times

\[
Mm\left(\log_2\frac1M+\log_2\frac1m+1\right).
\]

Writing `L=log_2(1/M)` and using `log_2(1/m)=L+R`, equations (4.3) imply

\[
\frac{\omega_d(P,Q)}{(P+Q)h_2(P/(P+Q))}
\le C_d M\frac{2L+R+1}{\max\{2,R\}}
\longrightarrow0
\tag{4.4}
\]

whenever `P->0` and `Q->0`, with **no assumption on their relative rate**.

Combining (2.1), (2.3), (3.7), (4.2), and (4.4) proves:

### Theorem 4.1 — complete mixed-face safety

For every fixed `d>=3`, along every interior sequence for which

\[
P=\prod_i p_i\to0,
\qquad
Q=\prod_i(1-p_i)\to0,
\tag{4.5}
\]

we have

\[
\boxed{D_{\Gamma_*}(\operatorname{EQ}_d;p)>0}
\tag{4.6}
\]

for all sufficiently late points of the sequence. Equivalently, at positive Poincare currency,

\[
\boxed{c_{\operatorname{EQ}_d}(p)<0.}
\tag{4.7}
\]

Thus every mixed boundary face containing at least one coordinate tending to `0` and another tending to `1` is safe, including arbitrarily hierarchical approaches.

## 5. Faces with only one orientation fixed

It remains to handle a boundary point at which at least one coordinate is `0`, no coordinate is `1`, and the other coordinates are interior. The all-one case is symmetric.

Suppose first that at least two coordinates remain interior. In the boundary limit the `1^d` exceptional corner disappears and the gate becomes a lower-dimensional one-corner NOR gate. Its stable defect is bounded below by

\[
\kappa W_N,
\qquad \kappa=0.2582048.
\tag{5.1}
\]

For a one-corner NOR gate on at least two genuinely interior coordinates,

\[
W_N=Q_R\left[\sum_j p_j-(1-Q_R)\right]>0,
\tag{5.2}
\]

because `1-prod_j(1-p_j)<sum_j p_j` strictly when at least two of the `p_j` lie in `(0,1)`. Exact biased-Walsh coefficients, gate entropy, and the source potential are continuous at this lower-dimensional limit. Therefore `D_*^{EQ}>0` throughout a neighborhood of every such boundary point.

The only zero-reserve lower-dimensional limit is one active interior coordinate. Let that coordinate have bias `t->t_0 in (0,1)` and let the other `d-1` small biases have sum

\[
\nu=\sum_{j=2}^d p_j\to0.
\]

Compare `EQ_d` with the one-corner NOR gate at the same full bias vector. If

\[
Q=(1-t)\prod_{j=2}^d(1-p_j),
\]

then its exact currency is

\[
W_N=Q\left[t+\nu-(1-Q)\right]
=t_0(1-t_0)\nu+O_d(\nu^2).
\tag{5.3}
\]

Hence

\[
D_*^N\ge \kappa t_0(1-t_0)\nu+O_d(\nu^2).
\tag{5.4}
\]

The omitted antipodal corner has probability

\[
P=t\prod_{j=2}^d p_j.
\]

Since `d>=3`, AM--GM gives

\[
P\le t\left(\frac{\nu}{d-1}\right)^{d-1}=O_d(\nu^2).
\tag{5.5}
\]

The exact two-corner perturbation changes spectral entropy by

\[
O_d\!\left(P\log\frac1P\right)=o(\nu),
\tag{5.6}
\]

while the output potential changes by `O(P)=o(\nu)` because the limiting one-corner output measure is interior. The additional input terms from the missing corner are nonnegative. Therefore

\[
D_*^{EQ}\ge D_*^N-o(\nu)>0
\tag{5.7}
\]

for all sufficiently small `nu`.

If no coordinate remains interior, the boundary point is the all-zero vertex, already covered by the account01/B16 simultaneous rare-corner theorem. The all-one vertex is symmetric.

## 6. Full boundary-collar theorem for the antipodal family

Every boundary point of `[0,1]^d` is now covered by exactly one of:

1. a mixed `0/1` face — Theorem 4.1;
2. a one-orientation face with at least two interior coordinates — strict read-once reserve and continuity;
3. a one-orientation face with exactly one interior coordinate — the `O(nu)` reserve versus `o(nu)` antipodal perturbation in Section 5;
4. an all-zero or all-one vertex — account01/B16.

The boundary is compact. Therefore the positive neighborhoods above have a finite subcover, yielding:

### Theorem 6.1 — compact-interior localization of every antipodal counterexample

For every fixed `d>=3`, there exists `eta_d>0` such that

\[
\boxed{
\min_i\{p_i,1-p_i\}<\eta_d
\quad\Longrightarrow\quad
D_{\Gamma_*}(\operatorname{EQ}_d;p)>0.
}
\tag{6.1}
\]

At positive currency this is equivalently

\[
\boxed{c_{\operatorname{EQ}_d}(p)<0.}
\tag{6.2}
\]

Hence a counterexample to the stable candidate within the entire antipodal family, if one exists at fixed arity `d`, must lie in the compact box

\[
\boxed{[\eta_d,1-\eta_d]^d.}
\tag{6.3}
\]

This closes all bias-boundary mechanisms for `EQ_d`, including fixed rays, hierarchical simultaneous corners, mixed faces, and lower-dimensional one-orientation faces.

## 7. Exact integration with the newest random-block theorem

Every nonempty coordinate restriction of `EQ_d` is a constant or a one-corner AND/NOR gate: fixing even one coordinate eliminates one of the two antipodal exceptional points. In particular, after a block of size `d-1`, every child is a constant or literal and has stable defect zero.

Therefore the newest account02/B18 identity specializes exactly to

\[
\boxed{
B_{d-1}^{\rm RO}(\operatorname{EQ}_d;p)+a_*Q_{d-1}
=D_{\Gamma_*}(\operatorname{EQ}_d;p).
}
\tag{7.1}
\]

Theorem 6.1 consequently proves that `EXACT-RANDOM-BLOCK-RO-DEFICIT-v1` is satisfied for this gate family throughout an entire boundary collar, with the witnessing scale explicitly `r=d-1`.

This is the precise way the newest peer result changes the argument: the relevant object is a terminal **aggregate block residual**, not a pointwise restriction-node correction. It retains all child slack, agrees with the bent-swap obstruction to pointwise local caps, and gives a direct insertion point into the current end-to-end gate induction.

## 8. Verification

A standard-library falsification checker independently reconstructs biased-Walsh laws for `EQ_d` and the two one-corner gates. On 744 deterministic random mixed-face instances in dimensions `3` through `7`, it checked:

- the exact defect decomposition (2.1), maximum floating residual `1.046e-15`;
- the entropy-interaction/Fannes upper bound, maximum observed excess `0`;
- a hierarchical `P/Q` sequence, where the Fannes-error-to-potential-mixing ratio decreased from about `0.951` to `0.00427` over the tested scales;
- the one-active-coordinate currency asymptotic, with `W_N/nu` converging to `t(1-t)=0.2331`.

Executed checker SHA-256:
`11cec8cc35c0826b66a6b096b3ceb1ce09cc8a11ffd0c4255ee0c5f679d7bbdb`.

Captured output SHA-256:
`f330927a5abd42cb6e06f8296991194b4f7b7dfa222024d297eaac84800fe7b9`.

The computation is a falsification check only. The theorem is the analytic argument in Sections 2--7.

## 9. Status and next implication

**New proved inference:** every fixed-arity antipodal gate `EQ_d` is safe for the stable candidate throughout a full boundary collar. Its complete remaining adversarial search is compact interior.

**Full FEI:** still **OPEN / NOT PROVED**. This theorem does not control unrelated composition-prime gates and does not certify `EQ_d` on its compact interior.

**Next exact implication:** for fixed `d`, prove `D_{Gamma_*}(EQ_d;p)>=0` on the compact box (6.3), preferably by a source-exact convexity/interval argument; in parallel, use account02/B18's multiscale bank to rule out simultaneous strict base-deficit inequalities for a general composition-prime gate. The boundary analysis here means no `EQ_d` interval verifier needs open-ended asymptotic tails.

Account04/B18's earlier mixed-curvature conservation, including the `p_{ik}+4o_{ik}` opposite-sign term, and its exact zero-defect classification remain untouched and are not weakened or silently substituted here.

Scoped privacy/provenance review: this package contains FEI mathematics, repository-relative artifact identifiers, and non-sensitive checker output only. It contains no credentials, scheduler identifiers, machine paths, benchmark answers, unrelated private data, email/Drive content or action, paid/remote compute, workflow dispatch, permission changes, or notification changes. No novelty or publication-priority claim is made.
