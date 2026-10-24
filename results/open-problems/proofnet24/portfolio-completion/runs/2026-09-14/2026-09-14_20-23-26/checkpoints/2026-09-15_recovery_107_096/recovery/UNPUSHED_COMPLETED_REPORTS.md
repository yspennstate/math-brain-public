# Root recovery record of completed but unpushed reports

**Provenance:** These are summaries retained from the conversation after the workspace disconnected. They are not the original agent reports. The agents had reached terminal completion, but their unpushed report/code bytes are unavailable. Numerical or exact certificates mentioned below cannot be reconstructed merely from their summary. Claims requiring those bytes are held for fresh proof.

## 069 — perturbed continuous four-type dynamics

Retained claim: for measurable strictly non-Volterra four-type coefficients, admissible Carathéodory forcing and an absolutely continuous instantaneous fixed point p(t), an input-to-state estimate used r=√5−2, c=(3−√5)/2, C1=1+c, C2=(1+c)²=5c:

```text
||x(t)-p(t)||_1 <= C1 exp(-r(t-s)) ||x(s)-p(s)||_1
 + integral_s^t exp(-r(t-v)) (C2 b(v)+||p'(v)||_1) dv.
```
Simplex viability requires the total field to be tangent and inward at each boundary coordinate; tangency alone is insufficient. No smallness condition on the forcing was claimed for the estimate itself. Additional retained topics include explicit perturbed caps, bounded-window tracking conditions and counterexamples distinguishing state convergence from convergence of the instantaneous fixed point. Original exact-check files are unavailable. Report 103 now independently reconstructs the bounded core and audits the archived 012 proof; the original 069 bytes remain unavailable.

## 070 — sufficient three-site entropy region

Retained claim: for an interior three-site L-ensemble whose three normalized off-diagonal magnitudes lie in[1/10,11/100], all Hermitian directions A satisfy

```text
H''(K)[A,A] <= -(3173/2400)(tr A)^2 -(3/4000)||A||_F^2.
```
The original explicit center, ball certificate and code are unavailable; the numeric theorem is not promoted without reconstruction.

Retained derivation lead: expand f=-log p by Möbius coefficients c_{ij},c_{123}; supermodularity gives c_{ij}≥0 and c_{ij}+c_{123}≥0. Put M=diag(c23,c13,c12)+c123 K. Then M≥0, and H''=-FI+2 tr(M adj A). If mI≤M≤uI and u<3m, α=(m+u)/2,η=(3m−u)/2 yield
2tr(M adj A)≤α(tr A)²−η||A||F²,
while FI≥(tr A)²/Var|X|≥4(tr A)²/3. A scalar Schur-complement criterion was claimed for the remaining full problem. Report 097 now independently reconstructs this valid scope, including a newly verified explicit center and radius. **Full three-site and full Lyons concavity were not solved.**

## 072 — positive attracting raw two-cycle

Retained original tensor:11→2;22,33,44→1;12→3;13,14→2;23,24,34→1. Thus V1=(1−x1)², V2=x1²+2x1(x3+x4), V3=2x1x2,V4=0. Mix Wε=(1−ε)V+εE4, with E4 equiprobable on offspring excluding both parents. Every allowed coefficient is at least ε/3.

The archived011 proof gives a positive attracting cycle for ε≤49/5000. Lost072 independently audited it and claimed the extension ε≤1/50 using r=21/1000, return-cap bound ε+2r²<r and two-step contraction24(ε+r)≤123/125. A coordinate lower bound Wε²(x)_i≥25ε³/243 was retained. Report 082 has independently reconstructed this full argument. No optimal threshold or global raw convergence was claimed.

## 074 — six-site projection coupling

Retained result: a rational6×6 orthogonal frame reportedly produced four projection laws with no prescribed-basis labeled diamond coupling, certified by a14-term±1 dual expectation−1/50 nonnegative on180 labeled diamonds. The same laws reportedly had an explicit19-atom unlabeled coupling. **The matrix, dual terms and atom weights were not retained. This record is not an exact witness or its verification.**

The retained theoretical claim is that supermodular mixed-derivative positivity for compressed rank-two projection laws is equivalent to existence of an unlabeled elementary-diamond coupling. A fixed-basis labeled obstruction does not refute positivity, and changing the complex basis can remove that obstruction. Agent107 reconstructs the finite-cone equivalence; agent092 may attempt a fresh bounded six-site result. General six-site mixed positivity and Lyons concavity remain open.

## Unfinished leads from interrupted workers

071 proposed a conditional Bernoulli Fisher decomposition. For history h on F and the next coordinate i, Q_h=K_F−I_abs(h), q_h=Kii−KiF Q_h^{-1} KFi, w_h=(-Q_h^{-1}KFi,1,0), and ω_h=P(h)/(q_h(1−q_h)). The proposed exact identity is
E(tr R_X A)²=Σ_h ω_h(w_h*Aw_h)².
It implies for independent blocks a,b
κ(B)=E[tr(R_a B R_b B*)]²=Σ_hg ω_hω_g|w_h*B w_g|⁴.
The draft claimed strict convexity in every dimension and a uniformly positive quartic Hessian for connected2+2 blocks, leading to a full open entropy-concavity neighborhood there. Report 081 independently reconstructs the complete argument; full independent audit 096 passes.

073 proposed spectral bounds tr h(K)≤H(P_K)≤Σ_i h(Kii), with equality iff K is diagonal, plus total-correlation forest lower bounds8Σ|Kij|⁴ and coherence bounds over disjoint pairs. The quantum conditional/equality arguments were unfinished. Report 085 reconstructs the full stated bounds; independent audit 101 now passes, with its precise equality wording erratum.

076 proposed exact diagonal-direction score/Hessian identities via signed nilpotent shifts, and warned that they are not ordinary coordinate-resampling identities. Same-sign endpoint rectangles can be feasible while mixed-sign rectangles need not be. Agent104 reconstructs the valid identities and a sufficient class.

These recovery leads are credited to their original workers, but the original workers are **interrupted**, not counted as completed.
