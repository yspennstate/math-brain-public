SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B14, 2026-09-23T04:03:21Z.
attacking: unnormalized-overlap localization—derive a mass-preserving fractional-potential/compiler for conjugate fibers, then test it against the remaining kernel-leakage/volume exits without support or moment assumptions.

# fleet02/B14 r25 — the k=3 volume gate survives on good normalized fibers, but averaging still loses N^2

Programme: `QFORM-DENSITY-3EIG-20260922`. Role: translations and localization / complementary constructions and source-valid counterexamples. Status: `NEW TARGET-VALID PROOF-MECHANISM BARRIER / FULL QFORM OPEN / CONTINUITY SEPARATE`. Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Sources actually used

The owner-controlled target is unchanged: independent one-dimensional densities bounded by one, arbitrary real symmetric A with at least three eigenvalues of modulus at least one, and a universal essential bound for the density of X^TAX, or a valid counterexample. No moment, support, log-concavity, connectedness, identical-law, or post-rotation-independence assumption is introduced here.

The required newest-Claude source is
`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837:proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`.
I use its proved k=3 volume-sampling theorem D in the exact form

`||p_Q||_infinity <= 6 sqrt(e) Z^(-1/6)`,

for an original-coordinate cross block M with `Z=e_3(M^T M)>0` and row volume marginals at most 1/2; all self blocks and affine terms are allowed.

The assigned completed partner actually used is fleet03/B14 r24,
`yspennstate/math-open-problems@2fe2734d7fc9a7e9a29edd26cbeda837fee10900:proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B14/20260923T023535Z-fleet03-B14-QFORM-r24/REPORT.md`.
It proves the exact conjugate-fiber identity: for iid X,X' with density `1_E`, |E|=1,

`U=X-X'`, `V=X+X'`, `m_E(u)=|E intersect (E-u)|`,

one has `p_U(u)=m_E(u)` and, on positive-overlap fibers,

`||p_(V|U=u)||_infinity = 1/(2m_E(u))`.

I use that identity below, not a surrogate conditional cap.

## 2. First unpaid implication attacked

The preceding B14 run showed that normalizing thin conjugate fibers and only then applying the no-marginal-condition D_k theorem (k>=5) can lose N^2 on legal fragmented inputs. One possible escape remained: perhaps the original k=3 theorem D can still be applied on a positive-probability set of fibers on which its nontrivial row-marginal gate survives, and perhaps that restriction restores uniformity.

The calculation below disproves that proof strategy. The row-marginal gate survives pointwise on a constant-mass good-fiber set, yet the averaged reciprocal third-volume certificate still grows quadratically.

## 3. A target-valid cross block with robust row-volume marginals

Fix N>=2 and the unit-measure separated set

`E_N = union_(j=1)^N [4^j, 4^j+1/N]`.

For every active coordinate take an independent pair `(X,X')` iid with density `1_(E_N)`, and write

`U=X-X'`, `V=X+X'`.

Different coordinate pairs are independent. Every V has density cap at most one, because

`p_V(v)=integral 1_(E_N)(x) 1_(E_N)(v-x) dx <= |E_N|=1`.       (3.1)

Use 15 left V-variables indexed `(g,r)`, `g=1,2,3`, `r=1,...,5`, and 3 right V-variables indexed `g=1,2,3`. Define the 15-by-3 cross matrix

`M0_((g,r),h) = delta_(g,h)/sqrt(5)`.                           (3.2)

Then `M0^T M0=I_3`, so its three singular values are all one and

`Z=e_3(M0^T M0)=1`.                                             (3.3)

The exact-rank-three volume marginal of every left row is its leverage, namely `1/5<=1/2`.

Consider

`Q_N(V)=2 V_I^T M0 V_J`.                                       (3.4)

Its symmetric matrix is `[[0,M0],[M0^T,0]]`. Hence its spectrum is `+1` three times, `-1` three times, and zero otherwise. This is inside the exact QFORM target.

Applying Claude theorem D directly to the original cap-one V variables gives the dimension- and fragment-uniform inequality

`boxed: ||p_(Q_N)||_infinity <= 6 sqrt(e) < 9.893.`             (3.5)

This is the required equation-level application of the newest-Claude result.

## 4. Normalize the conjugate fibers first

For a left difference value write

`a_(g,r)=m_N(u_(g,r))`,

and for a right difference write

`b_g=m_N(v_g)`.

By the partner theorem, conditional on all differences, each corresponding sum variable has density cap `(2a_(g,r))^(-1)` or `(2b_g)^(-1)`. To obtain cap-one variables put

`Y_(g,r)=V_(g,r)/(2a_(g,r))^(-1) = V_(g,r)/(1/(2a_(g,r)))`,

and similarly on the right; equivalently `V_(g,r)=2a_(g,r)Y_(g,r)` and `V_g=2b_gY_g`.

Thus the conditional cap-one cross block is

`M(u)=diag(2a_(g,r)) M0 diag(2b_g)`.                            (4.1)

For group g let

`S_g=sum_(r=1)^5 a_(g,r)^2`.                                   (4.2)

The three columns of M(u) remain orthogonal, and

`M(u)^T M(u)` has diagonal entries `(16 b_g^2/5) S_g`.          (4.3)

Therefore

`Z(u)=e_3(M(u)^T M(u))
     =(16^3/5^3) product_(g=1)^3 b_g^2 S_g`.                   (4.4)

## 5. A constant-mass good-fiber set where the k=3 marginal gate still holds

Put `ell=1/N`. For every ordered off-diagonal fragment pair `j!=k`, the partner overlap is exactly triangular around the center `4^j-4^k`:

`m_N(4^j-4^k+w)=ell-|w|`, `|w|<ell`.                           (5.1)

All these nonzero difference supports are disjoint. Let A_N be the union of only their central halves,

`A_N = union_(j!=k) [4^j-4^k-ell/2, 4^j-4^k+ell/2]`.           (5.2)

On A_N,

`ell/2 <= m_N(u) <= ell`.                                       (5.3)

Restrict all 18 differences to the product good set `G_N=A_N^18`.

For a left row `(g,r)`, the exact row volume marginal of the rank-three scaled matrix (4.1) is

`alpha_(g,r)=a_(g,r)^2/S_g`.                                   (5.4)

By (5.3), the worst case occurs when one a equals ell and the other four equal ell/2, so

`alpha_(g,r) <= ell^2/[ell^2+4(ell/2)^2] = 1/2`.               (5.5)

Hence Claude theorem D is valid on **every** fiber of G_N after normalization. The loss below cannot be blamed on failure of the row-marginal gate.

From (4.4), the pointwise normalized-fiber D certificate is

`C_D(u)=6 sqrt(e) Z(u)^(-1/6)
       =(3/2)sqrt(5e) product_g b_g^(-1/3) S_g^(-1/6).`        (5.6)

## 6. Exact good-set overlap integrals

The difference density is m_N itself. The total difference mass of A_N is

`P_N := integral_(A_N) m_N(u) du
     = N(N-1) * [3 ell^2/4]
     = (3/4)(1-1/N).`                                          (6.1)

The fractional overlap integral needed for the right variables is

`J_N := integral_(A_N) m_N(u)^(2/3) du
     = N(N-1) * 2 integral_0^(ell/2) (ell-w)^(2/3) dw
     = (6/5)(1-1/N) N^(1/3)(1-2^(-5/3)).`                     (6.2)

For one left group, define

`L_N = integral_(A_N^5)
       [product_(r=1)^5 a_r] [sum_(r=1)^5 a_r^2]^(-1/6)
       du_1...du_5`.                                            (6.3)

On A_N, `sum a_r^2 <= 5/N^2`; hence

`L_N >= 5^(-1/6) N^(1/3) P_N^5`.                              (6.4)

## 7. The normalized-good-fiber D certificate still loses N^2

The joint density of all 18 difference variables is

`product_(g,r) a_(g,r) * product_g b_g`.                       (7.1)

If one follows the proof order

`condition on all differences -> normalize every sum fiber -> apply k=3 theorem D pointwise on G_N -> average`,

the contribution from G_N alone to the resulting upper-bound certificate is

`B_N^(good)
 = integral_(G_N) C_D(u)
   [product_(g,r) a_(g,r)] [product_g b_g] du`.                 (7.2)

Using (5.6), independence of the integration variables, (6.2), and (6.4),

`B_N^(good)
 >= (3/2)sqrt(5e) [5^(-1/6)N^(1/3)P_N^5]^3 J_N^3
 =  (3/2)sqrt(e) N P_N^15 J_N^3`.                              (7.3)

Substitution of (6.1)-(6.2) yields

`boxed:
B_N^(good)
 >= c_* (1-1/N)^18 N^2,`                                      (7.4)

where

`c_*=(3/2)sqrt(e)(3/4)^15[(6/5)(1-2^(-5/3))]^3
    =0.0183573692706076... .`                                  (7.5)

For example, at N=100 the good-set contribution alone is at least

`153.1947...`,                                                  (7.6)

whereas the direct theorem-D bound (3.5) is below `9.893` for the exact same target-valid output.

Thus the pointwise-normalized proof certificate diverges at least quadratically even after throwing away every fiber on which the k=3 marginal gate might fail.

## 8. Localization conclusion

### `QFORM-D3-GOOD-FIBER-NORMALIZATION-BARRIER-v1`

There is a fully target-valid family of independent cap-one inputs and symmetric matrices with three +1 and three -1 eigenvalues such that:

1. Claude theorem D applied before conjugate conditioning gives the uniform bound `6 sqrt(e)`;
2. a positive-mass family of conjugate fibers remains inside theorem D's exact row-marginal regime after cap normalization;
3. nevertheless, applying theorem D separately to those normalized fibers and then averaging the resulting reciprocal-volume constants incurs an `Omega(N^2)` loss.

This does **not** refute QFORM and does **not** refute theorem D. It refutes the proof operation of moving the reciprocal third-volume inversion outside the unnormalized difference integral, even when one first restricts to fibers that satisfy the full k=3 analytic gate.

The mechanism is the same invariant exposed by the assigned partner: the original difference density contributes one full overlap power. Normalization consumes a fractional overlap power through `Z(u)^(-1/6)`. Keeping only geometrically good fibers does not restore that mass. The overlap must remain inside the Brascamp-Lieb/determinant aggregation until after reciprocal inversion.

## 9. First remaining implication

`QFORM-PREINVERSION-AGGREGATE-OR-KERNEL-LEAKAGE-v1`:

For every surviving no-pivot/heavy-star branch under `s_3(A)>=1`, either obtain a volume/ridge/bank exit on whole original-coordinate factors **before** normalizing any conjugate fiber, or prove an unnormalized kernel-leakage/positive-copy inequality in which every newly introduced disintegration variable retains a full mass/overlap power through the reciprocal curvature or determinant operation.

The present calculation rules out a weaker substitute: it is not enough to prove that a fixed positive fraction of normalized fibers satisfy theorem D's marginal gate.

Full QFORM remains OPEN. No unrestricted continuity claim is made.
