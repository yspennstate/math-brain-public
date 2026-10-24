# B18 FEI proof integration — exact tangent-defect decomposition and quantitative hard-core stability

**Run:** `20260921T154013Z-b18-fei-r13`  
**Status:** **PARTIAL / PROVED universal stability implications. Full uniform-cube FEI remains OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. No authenticated brain retrieval or receiver-context use occurred.  
**Role:** FEI proof integration. No publication-priority claim is made.

## 1. Fresh proof state and nonoverlap

Fresh `proofnet24/P03-fei` master was resolved before this derivation. The proof uses, without weakening their stated scopes:

1. the sharp scalar erasure frontier from account03/B14 (`97e683f4ef8587800293cd87dbe64b2559ebfa7e`), including its global tangent inequality and strict equality statement;
2. account01/B18's coarsening theorem and arithmetic endpoint analysis (`c3a87681125f599a3fa402503491f8a4cd391aa2`), whose stated next target is a quantitative stability theorem for near-saturation;
3. the preceding account04/B18 debit/reserve and weighted top-chain results (`a2eb9b018bb339d038384dad9ee5a894778b0a95`), especially the degree-`d` edge with posterior at least `q_d=1/(1+2^(2-2/d))` and upper mass at least `4^(1-d)`;
4. the current B15 warning that a potential-free one-coordinate payment for the whole packet bridge is false. Nothing below assumes that killed selector.

The new step is to turn the scalar frontier's strict supporting line into an **exact nonnegative slack decomposition**, then propagate it through arbitrary spectral coarsenings and blocks. This is the quantitative half of the stability target: small aggregate frontier slack forces both restriction-criticality tightness and weighted posterior concentration near the hard-core endpoint.

## 2. Setup

Let `g:{-1,1}^n->{-1,1}` be a nonconstant physical-restriction descendant maximizing

\[
r=H(g)/I(g)
\]

among its physical restriction descendants, with `r>4`. Let

\[
p_S=\widehat g(S)^2,
\qquad X\sim p.
\]

For a relevant coordinate `i`, pair `T` and `T+i` and write

\[
x_T=p_T,\qquad y_T=p_{T+i},\qquad
w_T=x_T+y_T,\qquad q_T={y_T\over w_T}.
\]

Then

\[
p_i:=\operatorname{Inf}_i(g)=\sum_Ty_T,
\]

\[
B_i=H(X_i\mid X_{-i})=\sum_Tw_Th(q_T),
\]

\[
\Delta_iH=\sum_Tw_T\Psi(q_T),
\]

where

\[
h(q)=h_2(q),\qquad
j(q)=1-h_2\!\left({1\over2}+\sqrt{q(1-q)}\right),\qquad
\Psi=h+j.
\]

Criticality of the chosen descendant gives

\[
\Delta_iH\ge r p_i.
\tag{2.1}
\]

For `q>0` put

\[
\beta(q)={h(q)\over q},\qquad
\kappa(q)={\Psi(q)\over q}.
\]

Let `tau=tau(r) in (0,1/2)` be the unique solution of `kappa(tau)=r`, let

\[
b=\beta(\tau),
\]

and let `lambda=lambda(tau) in (0,1)` be the tangent slope from the proved scalar-frontier argument,

\[
\lambda(q)={P(q)\over P(q)+Q(q)},
\quad
P=h-qh',\quad Q=j-qj'.
\]

The inherited proof gives the global tangent inequality

\[
\beta(q)\ge b+\lambda\bigl(\kappa(q)-r\bigr)
\qquad(0<q\le1),
\tag{2.2}
\]

with equality only at `q=tau`. Define its exact defect

\[
\boxed{
G_r(q)=\beta(q)-b-\lambda(\kappa(q)-r).
}
\tag{2.3}
\]

Thus `G_r(q)>=0`, and `G_r(q)=0` iff `q=tau`.

## 3. New exact theorem: scalar-frontier slack splits into two positive banks

### Theorem 3.1 — coordinate slack identity

For every relevant coordinate of the restriction-maximal core,

\[
\boxed{
B_i-bp_i
=\lambda\bigl(\Delta_iH-rp_i\bigr)
+\sum_{T:y_T>0}y_TG_r(q_T).
}
\tag{3.1}
\]

Both terms on the right are nonnegative.

### Proof

Because `y_T=w_Tq_T`,

\[
B_i-bp_i
=\sum_{T:y_T>0}y_T\,[\beta(q_T)-b].
\]

Insert the definition (2.3):

\[
\beta(q_T)-b
=G_r(q_T)+\lambda(\kappa(q_T)-r).
\]

Also

\[
\sum_Ty_T(\kappa(q_T)-r)
=\sum_Tw_T\Psi(q_T)-rp_i
=\Delta_iH-rp_i.
\]

This proves (3.1). Nonnegativity follows from criticality (2.1) and the global tangent inequality. QED.

This is stronger than the scalar lower bound `B_i>=bp_i`: its entire excess is now assigned exactly either to **physical-restriction criticality surplus** or to **posterior shape defect from the endpoint**.

Summing coordinates gives the global identity

\[
\boxed{
D_r(g):=B(g)-bI(g)
=\lambda\sum_i(\Delta_iH-rp_i)
+\sum_i\sum_{T:y_T>0}y_TG_r(q_T).
}
\tag{3.2}
\]

No cancellation is hidden in (3.2).

## 4. New quantitative stability: a dimension-free quadratic endpoint defect

### Proposition 4.1

For each fixed `r>4`, define

\[
\boxed{
c_r=
\inf_{0<q\le1,\ q\ne\tau}
{G_r(q)\over(q-\tau)^2}.
}
\tag{4.1}
\]

Then

\[
\boxed{c_r>0.}
\tag{4.2}
\]

### Proof

On `(0,1/2)`, the inherited scalar-frontier proof gives

\[
\beta'(q)=\lambda(q)\kappa'(q),
\]

where both `kappa(q)` and `lambda(q)` are strictly decreasing. Hence

\[
G_r'(q)=\kappa'(q)[\lambda(q)-\lambda(\tau)].
\]

Thus `tau` is the unique stationary minimum on the half interval and

\[
G_r''(\tau)=\kappa'(\tau)\lambda'(\tau)>0.
\tag{4.3}
\]

The proved strict extension of the tangent to `(1/2,1]` leaves no other zero. At `q=1`,

\[
G_r(1)=\lambda r-b>0.
\]

As `q downarrow0`, `beta(q)=log_2(1/q)+O(1)` while `kappa(q)=beta(q)+O(1)` and `lambda<1`; hence `G_r(q)\to+\infty`. Therefore the quotient in (4.1) extends continuously across `q=tau` with positive value `G_r''(tau)/2`, is positive away from `tau`, diverges at zero, and has a positive value at one. Its infimum is positive. QED.

Combining (3.1) with (4.2) yields

\[
\boxed{
B_i-bp_i
\ge
\lambda(\Delta_iH-rp_i)
+c_r\sum_Tp_{T+i}(q_T-\tau)^2.
}
\tag{4.4}
\]

and globally

\[
\boxed{
D_r(g)
\ge
\lambda\sum_i(\Delta_iH-rp_i)
+c_r\sum_{i,T}p_{T+i}(q_{i,T}-\tau)^2.
}
\tag{4.5}
\]

Therefore near scalar-frontier saturation is quantitatively rigid. In particular,

\[
\sum_i(\Delta_iH-rp_i)\le {D_r(g)\over\lambda},
\tag{4.6}
\]

\[
\boxed{
\sum_{i,T}p_{T+i}(q_{i,T}-\tau)^2
\le {D_r(g)\over c_r}.
}
\tag{4.7}
\]

For every `eta>0`, the total upper spectral incidence carried by edges whose posterior misses the endpoint by at least `eta` obeys

\[
\boxed{
\sum_{i,T:\,|q_{i,T}-\tau|\ge\eta}p_{T+i}
\le {D_r(g)\over c_r\eta^2}.
}
\tag{4.8}
\]

Since `sum_{i,T}p_{T+i}=I(g)`, Cauchy also gives the `L^1` form

\[
\sum_{i,T}p_{T+i}|q_{i,T}-\tau|
\le\sqrt{I(g)D_r(g)/c_r}.
\tag{4.9}
\]

There is also an approximate downward-closure statement. If `p_T=0<p_{T+i}`, then `q_{i,T}=1`, so

\[
\boxed{
\sum_{i,T:\,p_T=0<p_{T+i}}p_{T+i}
\le {D_r(g)\over c_r(1-\tau)^2}.
}
\tag{4.10}
\]

Thus the exact endpoint down-set law has a robust weighted precursor: small frontier slack forces almost all upper spectral incidence to have a lower neighbor and to sit near the geometric edge posterior `tau`.

If `theta=tau/(1-tau)` and `0<eta<1-tau`, then every edge with `|q-tau|<eta` satisfies `p_T>0` and

\[
\left|{p_{T+i}\over p_T}-\theta\right|
\le
{|q-\tau|\over(1-\tau)(1-\tau-\eta)}.
\tag{4.11}
\]

So (4.8) is also a weighted approximate-geometric-ratio theorem.

## 5. New coarsening-stable defect identity

Account01/B18 proved that the scalar frontier survives arbitrary coarsening. The tangent defect gives the quantitative version essentially for free, but with an important additional positive bank.

Let `G` be any sub-sigma-field of `sigma(X_{-i})` and put

\[
\bar Q=Pr(X_i=1\mid\mathcal G)=E[Q_i\mid\mathcal G].
\]

Write the coarse cells as `C`, with mass `\bar w_C`, posterior `\bar q_C`, and upper mass `\bar y_C=\bar w_C\bar q_C`. Define

\[
\bar\Delta_{i,\mathcal G}=\sum_C\bar w_C\Psi(\bar q_C).
\]

Concavity of `Psi` gives

\[
\bar\Delta_{i,\mathcal G}\ge\Delta_iH.
\tag{5.1}
\]

### Theorem 5.1 — exact coarsened slack decomposition

\[
\boxed{
\begin{aligned}
H(X_i\mid\mathcal G)-bp_i
={}&\lambda(\Delta_iH-rp_i)\\
&+\lambda(\bar\Delta_{i,\mathcal G}-\Delta_iH)\\
&+\sum_C\bar y_CG_r(\bar q_C).
\end{aligned}
}
\tag{5.2}
\]

All three terms are nonnegative.

### Proof

Apply the same algebra as in Theorem 3.1 to the coarse posterior law:

\[
H(X_i\mid\mathcal G)-bp_i
=\lambda(\bar\Delta_{i,\mathcal G}-rp_i)
+\sum_C\bar y_CG_r(\bar q_C).
\]

Split the first term at `Delta_iH` and use (2.1), (5.1). QED.

This separates three independent mechanisms by which a block conditional entropy can lie above the sharp floor:

1. physical restriction is not exactly critical;
2. coarsening creates a strict Jensen gain in the concave `Psi` moment;
3. the coarse posterior itself misses the endpoint.

For disjoint sets `A={i_1,...,i_m}` and `V`, order `A` and put

\[
\mathcal G_j=\sigma(X_V,X_{i_1},...,X_{i_{j-1}}).
\]

Summing (5.2) along the chain rule gives the exact **block stability ledger**

\[
\boxed{
H(X_A\mid X_V)-bI_A
=\sum_{j=1}^m\left[
\lambda C_j+\lambda J_j+S_j
\right],
}
\tag{5.3}
\]

where

\[
C_j=\Delta_{i_j}H-rp_{i_j}\ge0,
\]

\[
J_j=\bar\Delta_{i_j,\mathcal G_j}-\Delta_{i_j}H\ge0,
\]

and

\[
S_j=\sum_C\bar y_CG_r(\bar q_C)\ge0.
\]

Thus account01's monotone residual polymatroid has an explicit positive decomposition on every chain, rather than only a sign.

## 6. Integration with the weighted top-chain theorem: finite-degree quantitative nonattainment

The preceding B18 run proved that every nonconstant degree-`d` Boolean function has an oriented Fourier edge with

\[
q\ge q_d:={1\over1+2^{2-2/d}},
\qquad
p_{upper}\ge4^{1-d}.
\tag{6.1}
\]

Hence whenever `q_d>tau(r)`, (4.5) gives the explicit hard-core gap

\[
\boxed{
D_r(g)
\ge c_r\,4^{1-d}(q_d-\tau(r))^2.
}
\tag{6.2}
\]

Since `I(g)<=d`,

\[
\boxed{
{D_r(g)\over I(g)}
\ge {c_r\over d}\,4^{1-d}(q_d-\tau(r))^2.
}
\tag{6.3}
\]

Thus a sequence of restriction-maximal cores that approaches exact scalar-frontier saturation at a fixed `r` with `tau(r)<1/5` cannot have bounded Fourier degree. This turns the old exact top-degree obstruction into a quantitative one.

At the currently inherited calibration

\[
r_0=6.521845710923046575,
\]

standard-library/high-precision calibration gives

\[
\tau(r_0)=0.17403165703250501666...,
\]

\[
b(r_0)=3.83174494462437254376...,
\qquad
\lambda(r_0)=0.87383598624439510519...,
\]

\[
\lambda r_0-b=1.86727853431384599882....
\]

A dense numerical scan of the analytic defect found `G_r(q)/(q-tau)^2` positive throughout the sampled domain, with sampled minimum about `2.7370472830` at `q=1`. This number is **calibration only**; the proof above uses the exact positive constant `c_r` defined in (4.1), not the sampled minimum.

For orientation, the raw factor `4^(1-d)(q_d-tau)^2` before multiplication by `c_r` is approximately `6.34e-3` at `d=2`, `2.14e-5` at `d=5`, and `6.31e-12` at `d=15`. The exponential mass loss therefore remains; this run has not solved the amplification problem identified earlier.

## 7. What this closes and what remains

### PROVED in this run

1. The sharp scalar-frontier slack has the exact two-bank identity (3.1), separating restriction-criticality surplus from endpoint-posterior defect.
2. The tangent defect admits a dimension-free quadratic stability constant `c_r>0` for every fixed `r>4`.
3. Small aggregate slack `B-bI` forces weighted `L^2` and `L^1` concentration of every upper spectral edge posterior near `tau(r)`, plus weighted approximate downward closure and geometric edge ratios.
4. Arbitrary spectral coarsening has the exact three-bank decomposition (5.2): criticality surplus + concavity/Jensen surplus + coarse endpoint defect.
5. Every block-chain residual `H(X_A|X_V)-bI_A` decomposes into explicit nonnegative banks.
6. Combining this stability with the already-proved weighted top-chain edge gives the finite-degree quantitative gap (6.2)-(6.3).

### CONDITIONAL / inherited dependencies

- The global tangent inequality, uniqueness of `tau(r)`, monotonicity of `lambda(q)`, and strict equality case are inherited from the proved scalar-frontier theorem.
- Criticality `Delta_iH>=rp_i` is inherited from the restriction-maximal-core reduction.
- Concavity of `Psi` and the coarsening theorem are inherited from account01/B18.
- The degree-`d` edge bound (6.1) is inherited from the preceding B18 top-chain theorem and its top-degree granularity dependency.

### REFUTED / not used

- No every-prescribed-coordinate universal payment is assumed.
- No potential-free one-coordinate bound for `H-R` or the packet bridge is assumed; B15's rare-tribes obstruction remains in force.
- Numerical calibration is not promoted to a proof of an explicit closed form for `c_r`.

### OPEN

- Full uniform-cube FEI.
- The **second half of the hard-core stability target**: convert weighted edge closeness from (4.7)-(4.11), together with Boolean signed-convolution constraints, into either quantitative proximity of `r` to the isolated arithmetic endpoint or a proper physical block with `Delta_AH/I_A<r`.
- A dimension-independent amplification replacing the top-chain `4^(1-d)` mass scale by an `Omega(I)` resource.
- The tree inequality `E_T <= K I + R_T` from the preceding B18 run.

The next B18 integration step should therefore be phase-sensitive rather than another scalar inequality: use the new weighted edge-defect energy as the input to Booleanity/square-cycle signed convolution, attempting to force a block descent unless the approximate geometric law is globally coherent. That is now the exact missing implication between the scalar frontier and the arithmetic endpoint.
