SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B12, 2026-09-24T09:19:54Z.
attacking: sign-preserving spectral clipping — normalize arbitrary large eigenvalue magnitudes down to a threshold while proving that every spectral-square/original-coordinate carrier can only improve when the discarded spectrum is restored.

# account01/B12 — sign-preserving spectral clipping and square-receiver transfer

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Additional eigenvalue control  
Run: `20260924T091954Z-account01-B12-QFORM-auto11`  
Status: **PROVED SUPPORTING STABILITY/REDUCTION THEOREM / FULL QFORM OPEN**  
Continuity: **not proved by this branch**. The concrete end-to-end receiver below establishes essential boundedness only.
Execution: `WITHOUT_VERIFIED_BRAIN`.


## 1. First missing implication attacked

The additional-eigenvalue problem has two logically different parts:

1. whether very large or very small extra eigenvalues can destroy a deterministic physical-coordinate certificate; and
2. whether the bare hypothesis `s3(A)>=1` forces some paid physical-coordinate certificate in the first place.

The second problem is still the global structural gap. This run isolates the first problem much more sharply for every proof route whose deterministic premise is monotone in `A^2`.

A previous account01/B12 result handled *disjoint* selected spectral support: if `A=A_S+A_{S^c}` with orthogonal spectral supports, then `A^2=A_S^2+A_{S^c}^2>=A_S^2`. The new point here is that the selected eigenmodes themselves may also be clipped continuously. The residual then has the **same spectral support** as the retained core and the product is generally nonzero; nevertheless its interaction has the favorable sign. This permits arbitrary magnitude inflation on the very carrier eigenvectors themselves.

## 2. Main theorem: sign-preserving spectral clipping

Let `A=A^T` on `R^n`. Choose an orthonormal eigenbasis and write

`A = sum_i lambda_i u_i u_i^T`.

Choose arbitrary clipping coefficients

`0 <= t_i <= 1`

and define

`C = sum_i t_i lambda_i u_i u_i^T`,
`R = A-C = sum_i (1-t_i) lambda_i u_i u_i^T`.                 (2.1)

The choices can be made independently on the spectral modes; within a repeated eigenspace one may first choose any orthonormal eigenbasis, which leaves all formulas valid.

### Theorem 2.1 — `QFORM-SIGN-PRESERVING-SPECTRAL-CLIPPING-v1`

For the decomposition (2.1),

`CR=RC >= 0`,                                                   (2.2)

and

`A^2-C^2 >= 0`.                                                (2.3)

Consequently, for every ORIGINAL-coordinate isometry `P:R^m -> R^n` and every `1<=j<=m`,

`P^T A^2 P >= P^T C^2 P`,                                     (2.4)

and hence

`boxed( s_j(A P) >= s_j(C P) ).`                              (2.5)

More generally, every positive semidefinite certificate `G` satisfying

`0 <= G <= C^2`                                                (2.6)

also satisfies `0<=G<=A^2`. Therefore **any completed density receiver whose only spectral-carrier premise is a lower bound certified by some `G<=C^2` transfers unchanged to the actual final matrix `A`, provided its other hypotheses are verified for `A`.**

### Proof

Because `A,C,R` are diagonal in the same orthonormal eigenbasis,

`CR = sum_i t_i(1-t_i) lambda_i^2 u_i u_i^T >= 0`,             (2.7)

which proves (2.2). Likewise

`A^2-C^2
 = sum_i (1-t_i^2) lambda_i^2 u_i u_i^T >= 0`,              (2.8)

proving (2.3). Compression preserves Loewner order, so (2.4) follows. Finally

`s_j(AP)^2 = lambda_j(P^T A^2 P)`,
`s_j(CP)^2 = lambda_j(P^T C^2 P)`,                             (2.9)

with eigenvalues ordered decreasingly. Min-max monotonicity applied to (2.4) gives (2.5). Equation (2.6) plus (2.3) proves the receiver-transfer statement. QED.

No probabilistic comparison between `X^TAX` and `X^TCX` is asserted. In particular, **this is not a density-monotonicity theorem**. It is a deterministic compiler for square/carrier hypotheses only.

## 3. Exact reduction of arbitrary extra eigenvalues under the owner's hypothesis

Suppose now only that the actual final matrix `A` has at least three eigenvalues of modulus at least one. Pick any three corresponding orthonormal eigenvectors `u_1,u_2,u_3`, with eigenvalues `lambda_j`, `|lambda_j|>=1`, and set

`epsilon_j = sign(lambda_j)`.

Choose clipping coefficients

`t_j=1/|lambda_j|` for `j=1,2,3`,
`t_i=0` for every other spectral mode.                               (3.1)

Then

`C = sum_{j=1}^3 epsilon_j u_j u_j^T`,
`C^2 = P_E`,                                                        (3.2)

where `E=span{u_1,u_2,u_3}`. Theorem 2.1 gives the exact operator inequality

`boxed( A^2 >= P_E ).`                                             (3.3)

Thus every smaller eigenvalue, every larger eigenvalue, every sign, every multiplicity and every number of extra eigenvalues disappear from **square-carrier verification**. For every original-coordinate bank `H`,

`lambda_k((A^2)[H,H])
 >= lambda_k(P_E[H,H])`, `k=1,2,3`.                               (3.4)

Equivalently, if `P_H` is the coordinate isometry,

`s_k(A P_H) >= s_k(P_E P_H)`, `k<=3`.                            (3.5)

The remaining debt is therefore geometric rather than spectral-magnitude based: a rank-three projection `P_E` can be extremely diffuse, so (3.3) alone does not manufacture the five/six physical directions required by several existing receivers. The global theorem still needs a product-preserving structural argument for that rank-three orientation.

This is a useful simplification of the full programme: for all `A^2`-monotone receiver routes, **one may normalize the three chosen large eigenvalues to signs `+/-1` and delete the rest when proving the deterministic carrier lower bound**, then restore the complete actual spectrum at zero carrier cost.

## 4. Equation-level application of the newest account02/B12 theorem

The newest designated partner result read in full is

`QFORM-ORTHOGONAL-TWO-CHANNEL-MODE-STABILITY-v1`,

`yspennstate/math-open-problems@4cc6fbf96ef099a1492e043882219496509e94ba`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B12/20260924T085711Z-account02-B12-r13/REPORT.md`.

Its exact input is a full-column carrier `M`, an arbitrary addition `N`,

`G=M^T M`,
`K=G^{-1/2}M^T N G^{-1/2}`,
`Z=(I-P_Ran(M))N`,                                               (4.1)

and it proves, in particular at zero spent directions,

`s_m(M+N)^2 >= g^2 s_m(I+K)^2 + s_m(Z)^2`,                     (4.2)

where `g=s_m(M)`.

Apply it to the clipping decomposition with

`M=C P`, `N=R P`.                                                (4.3)

Assume `M` has full column rank. Since `CR>=0`,

`K
 = G^{-1/2} P^T C R P G^{-1/2} >=0`.                           (4.4)

Therefore `s_m(I+K)>=1`, and (4.2) yields the actual inequality

`boxed( s_m(A P)^2 >= g^2 + s_m(Z)^2 >= g^2 ).`                (4.5)

This is a direct application of the completed partner theorem to the actual final matrix. It also gives a geometric interpretation of Theorem 2.1: sign-preserving spectral inflation has no destructive longitudinal resonance because its whitened relative action is positive semidefinite; any transverse action is an additional nonnegative square channel.

## 5. Concrete target-class family with arbitrary signs, arbitrary magnitude inflation, and arbitrary spectator spectrum

Take fourteen original coordinates split into

`H={h_1,...,h_7}`, `F={f_1,...,f_7}`,

and append any number of spectator coordinates if desired. Define

`u_j=(h_j+f_j)/sqrt(2)`, `j=1,...,7`,                           (5.1)

and let `U=span{u_1,...,u_7}`.

Choose independently

`epsilon_j in {+1,-1}`, `a_j>=1`,                              (5.2)

and let `S=S^T` be **arbitrary on `U^perp`**:

`S U=0`.                                                        (5.3)

There is no restriction on the dimension, rank, eigenvectors, signs, multiplicities, or eigenvalue magnitudes of `S`. Put

`A = sum_{j=1}^7 epsilon_j a_j u_j u_j^T + S`,                 (5.4)

and clip to

`C = sum_{j=1}^7 epsilon_j u_j u_j^T`.                         (5.5)

Then

`C^2=P_U <= A^2`.                                               (5.6)

The actual matrix has seven eigenvalues of modulus at least one, so

`s3(A)>=1`.                                                     (5.7)

On the original-coordinate bank `H`,

`C h_j = epsilon_j u_j/sqrt(2)`,                               (5.8)

so the seven columns are orthogonal and

`G=(C P_H)^T(C P_H)=(1/2)I_7`,
`g=s_7(C P_H)=1/sqrt(2)`.                                     (5.9)

For the newest partner theorem, the residual is

`R=A-C
 = sum_j epsilon_j(a_j-1)u_j u_j^T + S`.                      (5.10)

Since `CS=0`, direct calculation gives

`K=diag(a_1-1,...,a_7-1)>=0`.                                  (5.11)

Thus the partner inequality (4.2) gives, for the **actual final matrix**,

`boxed( s_7(A P_H)^2 >= 1/2 ).`                                (5.12)

The signs `epsilon_j` disappear, every `a_j` may be arbitrarily large, and all spectator eigenvalues in `S` are completely unrestricted. This is precisely the desired additional-eigenvalue stability phenomenon without any post-rotation independence claim.

## 6. End-to-end density inequality via the completed six-mode receiver

To turn the stability result into an actual law-uniform density bound, apply the completed partner theorem

`QFORM-SIX-MODE-SPECTRAL-SQUARE-CARRIER-v1`,

`yspennstate/math-open-problems@e6c20a6e5a077c71e1ae7ac27e71d889a5e6a004`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B12/20260923T145451Z-account02-B12-QFORM-r36/REPORT.md`.

That theorem states: if the actual final symmetric `A` has `s3(A)>=s>0`, an ORIGINAL-coordinate bank `H` of size `m>=6`, and a certificate `0<=G_cert<=A^2` with

`lambda_6(G_cert[H,H])>=g^2`,                                  (6.1)

then, with `N=binom(m,2)`, parameters `0<a<b/N`, `0<b<g`, and `kappa=b/N-a`,

`||p_Q||_(infinity,ess) <= max {`
`  2 sqrt(6 pi m)/a,`
`  pi/kappa,`
`  3*400^(1/3)*kappa^(-5/6)*s^(-1/6),`
`  5 sqrt(2e)/sqrt(g^2-b^2)`
`}.`                                                            (6.2)

For the family (5.4), take

`m=7`, `s=1`, `G_cert=C^2=P_U`, `g^2=1/2`, `N=21`.             (6.3)

Indeed `P_U<=A^2` by (5.6), and

`P_U[H,H]=(1/2)I_7`,                                           (6.4)

so the sixth eigenvalue is exactly `1/2`.

Choose

`b=7/10`, `a=23/1000`,
`kappa = b/21-a = 1/30-23/1000 = 31/3000`.                    (6.5)

These satisfy `0<a<b/21` and `b<1/sqrt(2)`. The four terms in (6.2) are

`T1 = 2000 sqrt(42 pi)/23 = 998.8533745750...`,
`T2 = 3000 pi/31          = 304.0250955087...`,
`T3 = 3*400^(1/3)*(3000/31)^(5/6)
                             = 998.3302236565...`,
`T4 = 50 sqrt(2e)          = 116.5821990799...`.               (6.6)

Therefore every independent cap-one product source obeys

`boxed( ||p_(X^T A X)||_(infinity,ess) < 999 )`                (6.7)

for every matrix in the family (5.4), uniformly in all selected signs, all `a_j>=1`, the entire arbitrary spectator spectrum, and the ambient dimension.

The numerical decimals in (6.6) are only arithmetic evaluations of the displayed exact expressions; no simulation enters the proof.

This end-to-end branch proves an essentially bounded density. The six-mode receiver does not establish continuity in every one of its exit regimes, so no continuous representative is claimed here.

## 7. What this removes and what remains

### Removed spectral debt

For every square/carrier-monotone proof route, additional eigenvalue magnitudes are now fully normalized away:

- a selected large eigenvalue may be clipped continuously to any smaller same-sign magnitude;
- all unselected spectral modes may be deleted for the purpose of proving `G<=A^2`;
- restoring any of them, of either sign and arbitrary magnitude, cannot weaken the square certificate;
- restoring magnitude on a selected mode also cannot weaken it;
- the newest partner theorem identifies this restoration as an accretive longitudinal channel plus nonnegative transverse square energy.

Thus the phrase “arbitrary smaller and larger eigenvalues” no longer creates a separate obstacle **inside any receiver whose spectral premise is monotone in `A^2`**.

### Remaining full-target implication

The full QFORM conjecture remains open. From bare `s3(A)>=1`, clipping reduces the deterministic spectral content to a signed rank-three partial isometry

`C=sum_{j=1}^3 epsilon_j u_j u_j^T`, `C^2=P_E`,                (7.1)

but a rank-three projection can be highly diffuse over the original independent coordinates. What remains is to prove that every such orientation of `E` activates one of the completed product-preserving receivers — localized physical core, grouped-bank/hub, ridge-window, physical pair, diffuse aggregation, Schur, common-plane, or a related crossing certificate — with a universal quantitative constant.

The live correction set rules out replacing that step by a universal single good minor, a rank-three cross-cut dichotomy, naive fiber supremum, or post-rotation independence.

## 8. Scope and correction compliance

- No rotation of the random vector is performed.
- No claim that `X^T R X` is independent of `X^T C X` is made.
- No density monotonicity under `A^2>=C^2` is claimed; only deterministic receiver hypotheses transfer.
- No support, moment, log-concavity, Gaussianity, or connected-support hypothesis is introduced.
- Signs are arbitrary throughout.
- Repeated eigenvalues cause no degeneracy issue.
- The final density receiver is applied only after verifying its premises on the actual final matrix through the valid certificate `P_U<=A^2`.
- The full target and full continuity request remain open.

## 9. Sources

Fresh control source before publication:
`yspennstate/math-research-brain@05c16f25613411cb0ffbdec941273528d45e8116`, including `scheduled_tasks/README.md` and the live `CORRECTION_INBOX.json`.

Newest designated partner theorem actually applied:
`yspennstate/math-open-problems@4cc6fbf96ef099a1492e043882219496509e94ba`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B12/20260924T085711Z-account02-B12-r13/REPORT.md`.

Completed six-mode receiver applied to obtain (6.7):
`yspennstate/math-open-problems@e6c20a6e5a077c71e1ae7ac27e71d889a5e6a004`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B12/20260923T145451Z-account02-B12-QFORM-r36/REPORT.md`.

Earlier orthogonal-support precursor distinguished from this theorem:
`proofnet24/QFORM-density/fleet-2026-09-22/account01/B12/20260923T151555Z-account01-B12-QFORM-auto11/REPORT.md`.
