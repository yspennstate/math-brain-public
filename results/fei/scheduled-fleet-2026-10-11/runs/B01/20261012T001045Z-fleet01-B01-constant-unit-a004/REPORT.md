# B01 / A004 — convention freeze and sharp local bridge audit

Run: `20261012T001045Z-fleet01-B01-constant-unit-a004`  
Primary packet: `A004` (Constant and unit ledger)  
Related gaps: `G-BOOLEANITY`, `G-R-SELECT`  
Status: **PROVED baseline and local-sharpness claim pending independent review; full FEI remains OPEN**

## 1. Bounded objective and movement

The preceding A003 package proved

\[
C_{\rm FEI}\le C_{\rm step}\le C_{\rm FEI}+2/\ln2,
\qquad C_L\le C_{\rm FEI}\le C_L+3/\ln2,
\]

but did not decide whether the additive losses were scalar artifacts.  This run freezes the A004 conventions and proves a source-valid sharpness result:

> **PROVED (pending independent review).** The fixed-coordinate bounds
> \(E_i-L_i\le I_i/\ln2\), \(J_i\le2I_i/\ln2\), and
> \(\Delta_iH-L_i\le3I_i/\ln2\) are simultaneously asymptotically sharp over genuine Boolean functions.

The witness is a selector between a bent Boolean function and a one-point flip of it.  Consequently, improving the A003 implication `DOWN => FEI` requires a nonlocal or existential-coordinate argument; no refinement of the same pairwise scalar estimate can lower (3/\ln2).

This does **not** show that any global optimal-constant sandwich is sharp.  Full FEI remains open.

## 2. Frozen units and mappings

`CONVENTIONS.json` is the reusable ledger.  In particular:

* campaign entropy is in bits; a natural-log entropy or constant is divided by (\ln2) to convert to bits;
* for (g=(1-f)/2), (\widehat g(S)=-\widehat f(S)/2) only for nonempty (S), and the raw squares of (g)'s coefficients have mass (\mathbb E g), not one;
* (I_i(f)=\Pr[f(x)\ne f(x^{\oplus i})]=\sum_{S\ni i}\widehat f(S)^2).  The same edge probability for a (0/1) indicator equals (4\sum_{S\ni i}\widehat g(S)^2);
* (v=\operatorname{Var}(f)=\sum_{S\ne\varnothing}P(S)), so
  \(I-v=\sum_{S\ne\varnothing}(|S|-1)P(S)\ge0\);
* if (v>0), (H(f)=h_2(v)+vH(P(\cdot\mid S\ne\varnothing))).  At (v=0), no conditional law or (H/I) ratio is formed;
* multiplication by (\chi_U) preserves (H) but sends
  \[
  I(f)\mapsto I(f)+|U|-2\sum_{i\in U}I_i(f).
  \]
  Hence (D(f)=\min_UI(\chi_Uf)=\sum_i\min\{I_i,1-I_i\}), but (I) itself is not invariant.

The imported constants were recomputed without silent base changes:

\[
1/\ln2=1.442695040888963\ldots,
\quad2/\ln2=2.885390081777927\ldots,
\quad3/\ln2=4.328085122666891\ldots,
\]
\[
K_{\rm ref}=3+2\log_2 3+\log_2(6e)
=10.197582543052432\ldots.
\]

For the current threshold paper, the ledger separately records the intentionally mixed expression (L_*=1+\ln2), as well as (C_{\rm reg}=8.936474657877582\ldots), (2+4/\ln2), and (2/\ln2).

## 3. Endpoint calculations

`ENDPOINT_CHECKS.md` contains the full table.  Constants have (H=I=v=0), so FEI is read as (0\le C0).  A nonempty character (\chi_U) has (H=0), (I=|U|), (v=1), (I-v=|U|-1), and (D=0).  Thus parity is a mandatory warning that character multiplication preserves (H) but not (I).

For the one-point defect with rare-output mass (\delta=2^{-n}),

\[
I=2n\delta,qquad v=4\delta(1-\delta),
\qquad H/I\longrightarrow4.
\]

This verifies the empty-atom and rare-log normalization at the nearly constant endpoint.  It is a bounded-ratio family, not an FEI counterexample.

## 4. Exact sharpness derivation

For one coordinate (i), set

\[
a_T=\widehat f(T),\quad b_T=\widehat f(T\cup\{i\}),
\quad x=a_T^2,\quad y=b_T^2,\quad q=x+y.
\]

The conditional-bit and downward pair contributions give

\[
E_i-L_i=\sum_T x\log_2(1+y/x).
\]

The Jensen--Shannon contribution to the restriction entropy decrement is

\[
J_i=\sum_T q\,\phi\!\left(\frac{2|a_Tb_T|}{q}\right),
\quad
\phi(t)=\frac{(1+t)\log_2(1+t)+(1-t)\log_2(1-t)}2,
\]

and (\Delta_iH=E_i+J_i).  With (r=x/y), division by (y) gives

\[
U(r)=r\log_2(1+1/r),
\quad
V(r)=(r+1)\phi\!\left(\frac{2\sqrt r}{r+1}\right).
\]

The elementary bounds (\ln(1+s)\le s) and the A003 minority-mass inequality yield (U(r)\le1/\ln2), (V(r)\le2/\ln2).  Moreover

\[
U(r)\to1/\ln2,qquad
V(r)\to2/\ln2
\]

as (r\to\infty), since (\phi(t)=t^2/(2\ln2)+O(t^4)).

Now let (m) be even and (u:\{-1,1\}^m\to\{-1,1\}) be bent, so every Fourier coefficient has magnitude (2^{-m/2}).  Flip (u) at one point (x_0) to obtain (w), and let (F(x,z)) select (u) or (w).  At the selector coordinate,

\[
b_T=2^{-m}u(x_0)\chi_T(x_0),
\quad a_T=\widehat u(T)-b_T,
\quad I_z(F)=\sum_Tb_T^2=2^{-m}.
\]

Put (Q=2^{m/2}) and (\rho_T=\operatorname{sgn}(\widehat u(T)b_T)).  Parseval gives

\[
\sum_T\widehat u(T)b_T=2^{-m},
\]

so (\sum_T\rho_T=Q).  Hence (r_T=(Q-1)^2) occurs ((Q^2+Q)/2) times and (r_T=(Q+1)^2) occurs ((Q^2-Q)/2) times.  Both tend to infinity, and therefore

\[
\frac{E_z-L_z}{I_z}\to\frac1{\ln2},\qquad
\frac{J_z}{I_z}\to\frac2{\ln2},\qquad
\frac{\Delta_zH-L_z}{I_z}\to\frac3{\ln2}.
\]

All functions in the family are genuine Boolean functions.  The signed autocorrelation condition is automatic; explicitly (\sum_Ta_Tb_T=0).

## 5. Exact first unsupported line

The local bridge cannot be improved.  A smaller global loss would require, for some (c<3/\ln2), a theorem of the form

\[
\forall f\text{ nonconstant }\quad
\min_{i:I_i>0}\frac{\Delta_iH(f)}{I_i(f)}
\le \frac{L(f)}{I(f)}+c,
\]

or another nonlocal amortization that implies it.  The bent-defect selector does not refute this existential statement because a data coordinate may be cheaper.  No such theorem is proved here.  This is the precise OPEN line left after the A004 audit.

## 6. Validation

Command: `python3 verify_a004.py`  
Arithmetic: exact `Fraction` Walsh transforms for Boolean identities, double precision only for displayed asymptotic values  
Seed: none  
Scope: all 256 truth tables on three bits and all eight character shifts; bent constructions at (m=2,4,6,8); analytic formula through (m=40)  
Result: `PASS`, 5908 exact/numeric assertions.  Script and output hashes are recorded in `PROGRESS.json`.

The (m=40) displayed values are

\[
(E_z-L_z)/I_z=1.442695040887,
\quad J_z/I_z=2.885390081787,
\quad(\Delta_zH-L_z)/I_z=4.328085122674.
\]

The limiting claim is analytic and does not rely on floating-point output.

## 7. Sources and scope

Actually read:

* current threshold manuscript, commit `b38ba0ab49618ccbe6d1518a34c141dcec9f247c`, `paper/main.tex`, blob `1a9af8c62a32566a6ad1b7323a84d103a8375e93`, especially equations `HI`, `D`, `constants`, Theorem A, and the elementary gate constants;
* A003 endpoint report, commit `87f7c6267e56e7a0eb5b8dfd572a6eaaecae6907`, report blob `85308728bbfffe5cd3afd554cae783110fc57035`;
* A005 endpoint-admission report, commit `69fdc6d41576bc4921ba44a8acce696103bf6a81`, report blob `a32f008d392e999167eef98e4656dea03ad643fc`;
* current execution protocol blob `457358ff62cbf1141a72096bcabdf95bf18c1be2`, stream index blob `58e3eb0b1f0e9c03ebf709f83ad496ee8f2df704`, and B01 assignment blob `ac038a028831d59ad053dd56b2b527e2a71ffdee`.

No literature novelty claim is made.  Bent functions and one-point surgery are standard objects; the contribution here is the source-bound constant audit and the exact conclusion that A003's three fixed-coordinate losses are simultaneously sharp on this family.

## 8. Handoff

A086 or A094 should independently reconstruct the two exact selector spectra and the limits of (U,V), then verify that the conclusion is only fixed-coordinate sharpness.  Consumers A001, A002, A016, A018, A024, A036, A042, A046, A056, A061, A062, A068, A072, A076, and A081 should reuse `CONVENTIONS.json` rather than rebuild units.  A future B01 run should attack the existential inequality in Section 5, not attempt to sharpen the now-optimal scalar bounds.

