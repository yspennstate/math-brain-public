SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B18, 2026-09-24T11:03:00Z.
attacking: the overlapping near-rank-one cross tail — a flat target family where source-separated convolution is genuinely unavailable, the pinned three-large-eigenvector Fresnel gate breaks discontinuously, and the latest fleet03/B18 physical-pair currency vanishes diffusely.

# fleet02/B18 r11 — maximally overlapping Hadamard tail: exact source-overlap and proof-interface obstruction

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: literature-to-proof transfer / complementary constructions  
Status: **PROVED TARGET-VALID STRUCTURAL OBSTRUCTION + EQUATION-LEVEL PARTNER APPLICATION / FULL QFORM OPEN**  
Continuity: not claimed for the full family by this report.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. First unpaid implication

The preceding fleet02/B18 run separated a harmless case from the current near-rank-one collar: if the small second cross direction lives on original coordinates disjoint from a paid rank-one-cross/transverse-square packet, then it is retained exactly by independent convolution. The genuinely unpaid case is when the small tail shares the same original sources as the core.

The latest completed designated-partner theorem is fleet03/B18 `QFORM-COLLINEAR-TWOCOLUMN-TRANSVERSE-L4-v1`, canonical source

`yspennstate/math-open-problems@08274cd0a9c7b71793e75bc71281f66694bfd441`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B18/20260924T095710Z-fleet03-B18-QFORM-auto24/REPORT.md`.

For an original zero-self bank and two physical complement coordinates whose cross columns are collinear, if `kappa_0` is the Euclidean size of those two columns and `tau` is the retained pair curvature transverse to the cross direction, it proves

`||p_Q||_infinity <= 2^(9/4) 3^(3/4) kappa_0^(-3/4) |tau|^(-1/4)`.       (1.1)

The proof keeps the rotated pair dependent. Its only external anti-concentration input is Rudelson--Vershynin, arXiv:1402.4492, Theorem 1.2: for independent real coordinates with density cap `K` and an l2-normalized coefficient vector, the resulting scalar linear form has density cap at most `sqrt(2) K`. This theorem has no moment, support, iid, centering, symmetry, log-concavity or smoothness assumption. I rechecked this primary statement; no broader regularity theorem is transferred.

This run constructs a literal QFORM family showing that the remaining overlap is not bookkeeping. The small tail uses every source used by the core, is detectably dependent on the core projections for an admissible law, destroys the natural pinned Theorem-F diagonal-twist gate for every spanning physical set, and leaves every exact-collinear partner pair with a certificate diverging as `m^(5/8)`.

## 2. The flat overlapping family

Let `m>=4` be divisible by four. Use two disjoint original-coordinate banks `I,J`, each of size `m`. On `I` define

`u  = m^(-1/2) (1,...,1)`,

`u2 = m^(-1/2) ( +1 on the first m/2 coordinates, -1 on the second m/2 )`.

On `J` define

`v  = m^(-1/2) (1,...,1)`,

`v2 = m^(-1/2) ( +1 on the first m/2 coordinates, -1 on the second m/2 )`,

and, by quarters,

`w = m^(-1/2) (+1,-1,+1,-1)`

where each displayed sign occupies `m/4` consecutive coordinates. Then

`u perpendicular u2`, and `v,v2,w` are pairwise orthonormal.                        (2.1)

For `0<eps<1`, set

`D_eps = u v^T + eps u2 v2^T`,

`A_eps = [[0, D_eps], [D_eps^T, w w^T]]`,                              (2.2)

and write

`U=u^T X_I`, `U2=u2^T X_I`, `V=v^T X_J`, `V2=v2^T X_J`, `W=w^T X_J`.

Thus

`Q_eps = X^T A_eps X = 2 U V + 2 eps U2 V2 + W^2`.                     (2.3)

### Proposition 2.1 — exact target spectrum

The nonzero spectrum is

`boxed: spec_nonzero(A_eps) = {-1, +1, +1, -eps, +eps}.`               (2.4)

Hence every `0<eps<1` has exactly three eigenvalues of modulus at least one.

**Proof.** In the orthonormal ordered basis `(u,v,u2,v2,w)`, the restriction of `A_eps` is block diagonal with blocks

`[[0,1],[1,0]]`, `[[0,eps],[eps,0]]`, `[1]`.

All orthogonal directions are killed. QED.

So the family lies literally in the owner's unrestricted target; it is not a limiting non-target surrogate.

## 3. The small tail is maximally source-overlapping, not an independent convolution

The paid core

`Q_0=2UV+W^2`                                                         (3.1)

uses every original coordinate in `I` through `U` and every original coordinate in `J` through `V,W`. The tail

`R_eps=2 eps U2 V2`                                                   (3.2)

also uses every coordinate in both `I` and `J`, because every entry of `u2,v2` is nonzero. Thus the source supports coincide exactly; there is no partition of the original coordinates that makes (3.2) a disjoint-source remainder of (3.1).

This is not merely a formal warning. Take every original input iid `Uniform[-1/2,1/2]`, an admissible density-one law. Put `sigma^2=1/12` and let `kappa_4=E X_i^4-3 sigma^4=-1/120`. For any two orthogonal unit coefficient vectors `a,b`, independence of the original coordinates gives the exact fourth-moment identity

`E[(a.X)^2 (b.X)^2] = sigma^4 + kappa_4 sum_i a_i^2 b_i^2`.             (3.3)

For the flat pair `u,u2`,

`sum_i u_i^2 u2_i^2 = 1/m`,

so

`boxed: E[U^2 U2^2] = 1/144 - 1/(120m) != 1/144 = E[U^2] E[U2^2].`    (3.4)

Therefore `U` and `U2` are not independent. The same calculation shows `V` and `V2` are not independent. One may not replace the overlapping tail by the independent-convolution argument of the preceding B18 run, nor infer independence from the orthogonality of the coefficient vectors.

This is exactly the owner correction `no independence after rotation`, exhibited here inside the live near-rank-one collar rather than as a generic warning.

## 4. Small matrix norm is still not a small random perturbation

The tail matrix has operator norm `eps`, but its random effect cannot be deleted uniformly over the allowed law class.

Translate the density-one coordinate intervals on `I` so that their center vector is `R u2`, and translate those on `J` so that their center vector is `R v2`. Translation preserves every one-dimensional density cap. By orthogonality, the centers of `U,V,W` remain zero while

`U2 = R + Xi`, `V2 = R + Eta`,                                      (4.1)

where `Xi,Eta` are centered projected noises. Hence

`2 eps U2 V2 = 2 eps R^2 + 2 eps R (Xi+Eta) + 2 eps Xi Eta`.          (4.2)

Taking `R=eps^(-1)`, and discarding only the deterministic output translation `2/eps`, leaves the order-one random affine term

`2(Xi+Eta) + 2 eps Xi Eta`.                                          (4.3)

Thus even this explicit rank-one-size `eps` cross tail is not a uniformly small random perturbation under arbitrary translated cap-one laws. Any bridge must retain it algebraically.

## 5. Required pinned result: Theorem F pays eps=0, but its actual-large-eigenvector gate fails for every eps>0

Use the completed pinned source

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md` and `FOURIER_ROUTE_REPORT.md`.

Pinned Theorem F permits a rank-three spectral part plus a residual `B`, provided there is an original-coordinate set `S` on which `B_SS` is diagonal and the three spectral rows have an invertible Gram matrix with normalized row leverages at most `1/2`. Its conclusion is the genuine whole-line density estimate

`||p_Q||_infinity <= 12 (|lambda_1 lambda_2 lambda_3| det G_S)^(-1/3)`. (5.1)

### 5.1 At eps=0: a real target inequality

The actual three nonzero eigenvectors of `A_0` can be chosen as

`r_+ = (u+v)/sqrt(2)`, lambda `+1`,

`r_- = (u-v)/sqrt(2)`, lambda `-1`,

`r_w = w`,             lambda `+1`.                                 (5.2)

With the full active original-coordinate set, their Gram is `I_3`. Each `I`-coordinate has spectral leverage `1/m`; each `J`-coordinate has leverage `2/m`. For `m>=4` all leverages are at most `1/2`. There is no residual. Therefore pinned Theorem F applies literally and yields

`boxed: ||p_{Q_0}||_infinity <= 12`                                  (5.3)

for every allowed rough product law.

This is the required application of a completed `e5f71d79...` result to a genuine target matrix, not a citation-only use.

### 5.2 At every eps>0: the direct spectral-tail transfer is impossible

Keep the **actual three large eigendirections** (5.2). Their large spectral subspace is unchanged when `eps>0`. The exact residual is

`B_eps = eps (u2 v2^T + v2 u2^T)`.                                  (5.4)

Every mixed physical entry of `B_eps` between `I` and `J` is nonzero, of magnitude `eps/m`. Consequently, if an original-coordinate set `S` has `(B_eps)_(S,S)` diagonal, then `S` cannot contain a coordinate from both banks: necessarily `S subset I` or `S subset J`.                              (5.5)

But on `I` the rows of `(r_+,r_-,r_w)` are all proportional to `(1,1,0)`, so their Gram has rank one. On `J` they lie in the two-dimensional plane `{(a,-a,b)}`, so their Gram has rank at most two. Thus

`boxed: for every eps>0, no physical set S simultaneously makes (B_eps)_(S,S) diagonal and gives an invertible three-row Gram for the actual three large eigendirections.`     (5.6)

Hence the pinned Theorem-F proof interface that gives (5.3) at `eps=0` fails **discontinuously** for every nonzero overlapping tail, however small. This does not say that no alternative decomposition or theorem can control `Q_eps`; it says precisely that the completed actual-three-large-eigenvector Fresnel certificate cannot simply absorb this tail as its diagonal twist.

On the natural bank cut `I|J`, pinned Theorem D and its unconditional fifth-volume extension also do not fire:

`rank(D_eps)=2`, hence `e_3(D_eps^T D_eps)=e_5(D_eps^T D_eps)=0`.        (5.7)

Again this is a statement about this physical cut, not a claim that every possible cut has zero volume.

The pinned counterexample search found no valid QFORM counterexample; that search miss is not used as novelty evidence or as evidence for any claim above.

## 6. Equation-level application of the latest fleet03/B18 theorem

For a coordinate `j` in `J`, write

`s_j = sqrt(m) (v2)_j in {+1,-1}`,
`t_j = sqrt(m) w_j in {+1,-1}`.

The cross column from the zero-self bank `I` to `j` is

`d_j = m^(-1/2) (u + eps s_j u2)`.                                  (6.1)

Take a physical pair `{j,k}` with `s_j=s_k`. Then the two columns are exactly collinear and equal, so the newest partner theorem applies. Its cross currency is

`kappa_0 = sqrt(||d_j||^2+||d_k||^2)
         = sqrt(2(1+eps^2)/m)`.                                      (6.2)

The retained pair block comes from `ww^T`. The transverse pair direction is `(-1,1)/sqrt(2)`, and

`tau_jk = (w_j-w_k)^2/2
        = 0` if `t_j=t_k`,
`        = 2/m` if `t_j=-t_k`.                                      (6.3)

Thus the **best applicable exact-collinear physical pairs** are those with equal `v2` sign and opposite `w` sign, and every such pair gives exactly

`boxed:
 ||p_Qeps||_infinity
 <= 2^(13/8) 3^(3/4) (1+eps^2)^(-3/8) m^(5/8).`                      (6.4)

There are such pairs, but (6.4) diverges as `m->infinity`. Pairs with equal `v2` sign and equal `w` sign have `tau=0`; pairs with opposite `v2` signs have linearly independent cross columns for `eps>0`, so the collinear two-column theorem does not apply to them.

The raw partner currency for each useful pair is

`kappa_0^3 |tau_jk|
 = 2^(5/2) (1+eps^2)^(3/2) m^(-5/2)`.                               (6.5)

There are exactly `m^2/8` useful pairs: in each `v2`-sign half, `m/4` coordinates have each `w` sign. Even summing **all** raw currencies of all exact-collinear useful pairs gives only

`boxed:
 sum_useful kappa_0^3 |tau_jk|
 = (1+eps^2)^(3/2) / sqrt(2m) -> 0.`                                 (6.6)

Therefore a fixed-pair selection rule, or a naive linear aggregation of the newest pair currency, cannot supply the missing dimension-free bridge on this maximally overlapping family.

For example, at `m=8, eps=0.01`, (6.4) is `25.7887113173...`, while the nonzero spectrum is exactly `{-1,-0.01,0.01,1,1}` and the raw-currency sum is `0.2500375009...`.

## 7. What this family proves and what it does not

The family is **not** a counterexample to QFORM. No lower bound on its true density is claimed. It is a source-valid obstruction to four proof shortcuts at once:

1. the small second cross direction is not source-separated, so the preceding B18 convolution lemma is unavailable;
2. the tail cannot be deleted perturbatively under arbitrary translated cap-one laws, by (4.2)--(4.3);
3. pinned Theorem F pays the exact endpoint `eps=0` by `12`, but the actual-large-eigenvector diagonal-residual gate fails for every `eps>0` by (5.6);
4. the latest fleet03/B18 exact-collinear physical-pair certificate and even the sum of its raw currencies vanish/deteriorate diffusely by (6.4)--(6.6).

The natural cross cut is only rank two, so the pinned three- and five-volume receivers on that cut are also silent.

The sharpened first unpaid implication is therefore

`QFORM-OVERLAPPING-RANK2-TAIL-AGGREGATE-STABILITY-v1`:

> Starting from a paid rank-one-cross plus transverse-curvature packet, control a nonzero second cross direction which shares all original sources with the packet, without reciprocal loss in its small singular value and without requiring the residual to be diagonal on a spanning physical set. Equivalently, find a genuinely aggregate product-preserving receiver stable through the family (2.2), or prove that every such survivor is forced into another already-paid grouped-hub/projected-crossing/ridge/volume branch with uniform parameters.

The family shows why the word **overlapping** is essential: the exact endpoint is easy by pinned Theorem F, and a disjoint copy of the same small tail is easy by convolution, but a same-source tail of arbitrarily small coefficient simultaneously breaks both interfaces.

Globally, the bare condition `s_3(A)>=1` still does not force this two-bank packet; the full structural compiler remains unpaid.

## 8. Deterministic checks and correction discipline

For `m=8`, direct diagonalization gives:

- `eps=0`: `{-1,1,1}`;
- `eps=0.01`: `{-1,-0.01,0.01,1,1}`;
- `eps=0.5`: `{-1,-0.5,0.5,1,1}`.

For `m=8, eps=0.01`, the exact partner quantities for a useful pair are

`kappa_0=0.500024999375...`, `tau=0.25`, and bound `25.7887113173...`, matching (6.4).

No step uses or infers independence after rotation, arbitrary-joint coarea, a worst conditional-density cap, law-uniform pointwise phase decay, deletion of a small matrix coefficient, a universally good fixed minor, or novelty from a search miss. Every independence statement is tied to disjoint original banks; the within-bank projected dependence is explicitly certified by (3.4).
