SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B10, 2026-09-23T14:17:19Z.
attacking: the exact-rank-three nonzero near-null physical-coloop collar; splice the completed exact-null partner theorem to the required mixed-Fresnel source on a genuine punctured class, then falsify the tempting one-sided square-peel interpolation on the unpaid two-sheet side.

# account02/B10 r11 — rank-one transverse-compression interpolation and a logarithmic square-peel obstruction

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: rank-three coupled case / complementary constructions  
Status: `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_THEOREM / LOCAL_ROUTE_COUNTEREXAMPLE / FULL_QFORM_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. First unpaid implication

The completed account03/B10 exact-null theorem now pays `a=r^TMr=0`. The required ruled theorem pays the one-sheet side of every indefinite exact-rank-three form. The genuinely unpaid B10 implication is therefore still the nonzero near-null two-sheet collar, but this run removes an entire structural face of it:

`QFORM-NEARNULL-RANKTWO-TRANSVERSE-COLLISION-v1`:

> after the exact-null endpoint and the rank-one transverse-compression case proved below are removed, control the punctured collar in which the retained transverse physical compression has rank two (or mixed longitudinal/transverse physical rows prevent a pure coloop reduction), without a reciprocal power of the small hub pivot and without taking a worst conditional projection-density supremum.

A second conclusion below is negative but useful: the natural one-sided scalar-square kernel majorant itself grows like `log(1/|a|)` on a target-valid family in the strictly two-sheet region, even though a source-valid mixed-Fresnel estimate keeps the true density uniformly bounded. Thus that majorant cannot be the interpolation endpoint.

## 2. Source boundary and completed inputs actually used


`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

under `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`.

Two completed results from that source are used at equations, not merely cited:

1. **Theorem C (ruled one-sheet estimate).** For signature `(2,1)`, with all three absolute eigenvalues at least one, `p_Q(s)<=pi sqrt(2)` for `s>=0`; for signature `(1,2)` the same statement applies to `-Q`, hence to `s<=0`.
2. **Theorem MF (mixed Fresnel).** With one genuine heavy original coordinate and a rank-one receiver square, if the two-dimensional augmented receiver leverage is at most `1/2`, then

`|phi(t)| <= (4*pi)^(3/2)/(2 |t|^(3/2) sqrt(|lambda| det Gamma))`.

The completed designated partner account03/B10 r24 is

`yspennstate/math-open-problems@c0d7e627b3b877fcecc3004a58335658f6541d64`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B10/20260923T114517Z-account03-B10-QFORM-r24/REPORT.md`.

Its theorem `QFORM-NULL-HUB-TRANSVERSE-LEVERAGE-CLOSURE-v1` states that for an exact null physical hub of leverage `h`, determinant currency `D=|det M|`, and complementary transverse leverage at most `1/2`,

`||p_Q||_infinity <= 3*2^(4/3) (hD)^(-1/3)`.                      (2.1)

In particular, at a pure coloop `h=1`, it pays the exact-null point by

`||p_Q||_infinity <= 3*2^(4/3) D^(-1/3)`.                         (2.2)

A newer account03/B10 r25 artifact was only an early checkpoint when this report was prepared. I use its algebraic rank-jump observation only as corroboration, not as a completed theorem.

The immediate account02/B10 predecessor is

`yspennstate/math-open-problems@f81263344356dd37ef7f6323f863ba48b49f1a34`,

which isolated the near-null weak-curvature collar and proved `det(E^TME)=a det(M)/||Mr||^2` for the compression to `(Mr)^perp`.

## 3. Canonical shear-defect identity for every nonzero near-null pivot

Write

`A=UMU^T`, `U^TU=I_3`, `sigma_min(M)>=1`, `D=|det M|>=1`,

and let a physical row be `u_0=sqrt(h)r`, `||r||=1`. Put

`a=r^TMr`, `k=Mr`, `kappa=||k||`.

Define

`z = M k/kappa^2 - (k^T M k) k/(2 kappa^4)`,                       (3.1)

`N = M - k z^T - z k^T`.                                          (3.2)

### Lemma 3.1 — `QFORM-NEARNULL-CANONICAL-SHEAR-DEFECT-v1`

One has

`Nk=0`,                                                            (3.3)

and for every `x,y in k^perp`,

`x^TNy=x^TMy`.                                                     (3.4)

Hence, if `E` has orthonormal columns spanning `k^perp`, the two nonzero eigenvalues of `N` are precisely those of `E^TME`, and

`pdet(N)=det(E^TME)= a det(M)/kappa^2`.                            (3.5)

For indefinite `M` whose three eigenvalues have modulus at least one, one of those two eigenvalues has modulus at least one. Consequently:

- if `a=0`, `N` has rank exactly one;
- if `a!=0`, `N` has rank exactly two.

If `U_L` denotes the leaf rows, set

`g=sqrt(h) U_L k`, `ell=h^(-1/2)U_L z`.                            (3.6)

Then the entire physical leaf block satisfies the exact identity

`A_LL = g ell^T + ell g^T + U_L N U_L^T`.                          (3.7)

#### Proof

From (3.1),

`z^T k = (k^TMk)/(2 kappa^2)`.

Therefore

`Nk = Mk - k(z^Tk)-z kappa^2 =0`,

which proves (3.3). If `x,y` are perpendicular to `k`, both rank-two correction terms in (3.2) vanish between `x` and `y`, proving (3.4). The cofactor identity gives

`det(E^TME)=det(M) (k/kappa)^T M^(-1)(k/kappa)
            =det(M) r^TMr/kappa^2`,

which is (3.5). Interlacing of the two-dimensional compression with an indefinite three-dimensional matrix having spectral gap one shows that one compressed eigenvalue has modulus at least one. If `a=0`, the other eigenvalue is zero; the compression cannot be the zero matrix because that would force `M` to have rank at most two. Thus `rank N=1`. For `a!=0`, (3.5) is nonzero and `rank N=2`.

Finally, `g ell^T+ell g^T = U_L(kz^T+zk^T)U_L^T`, so (3.7) follows from (3.2). QED.

This identifies the exact deterministic rank jump at the null endpoint: the partner's rank-one residual is not a perturbative approximation. A genuinely second residual curvature appears immediately for `a!=0`.

## 4. New positive theorem: rank-one transverse physical compression interpolates uniformly through `a=0`

The previous rank jump concerns the compression to `(Mr)^perp`. A different physical structural face remains much better behaved.

Assume now that the hub is a **pure original-coordinate coloop**:

`u_0=r`,                                                           (4.1)

so its leverage is one. Parseval then forces every leaf row to lie in `r^perp`; in an orthonormal basis of `r^perp`, write the leaf row matrix as `V`, so

`V^TV=I_2`.                                                        (4.2)

Assume the actual transverse compression

`C = P_(r^perp) M P_(r^perp) |_(r^perp)`                           (4.3)

has rank one, and every physical leaf has transverse leverage at most one half:

`||v_j||^2<=1/2`.                                                  (4.4)

### Theorem 4.1 — `QFORM-COLOOP-RANKONE-TRANSVERSE-MF-v1`

Under (4.1)-(4.4), for arbitrary independent original-coordinate input densities bounded by one, **with no restriction on the scalar pivot `a=r^TMr`**, the law of `Q=X^TAX` has a continuous density and

`boxed: ||p_Q||_infinity <= 3*2^(4/3) D^(-1/3).`                  (4.5)

In particular the bound is uniform through the punctured near-null limit `a->0`.

#### Proof

Since `C` has rank one, choose an orthonormal basis `(q,q_perp)` of `r^perp` and a nonzero scalar `lambda` such that

`C=lambda q q^T`.                                                  (4.6)

Put

`b=P_(r^perp)Mr = b_1 q+b_2 q_perp`.                              (4.7)

In the spectral basis `(r,q,q_perp)`,

`M = [[a,b_1,b_2],[b_1,lambda,0],[b_2,0,0]]`.                     (4.8)

Because `M` is invertible, `b_2!=0`, and

`D=|det M|=|lambda| b_2^2`.                                       (4.9)

In physical leaf coordinates define the hub-coupling column and the receiver-square column

`c=Vb`, `s=Vq`.                                                    (4.10)

Then

`A_LL=lambda s s^T`, `A_L0=c`,                                   (4.11)

while `A_00=a` is arbitrary. This is exactly Theorem MF with one heavy coordinate and one receiver Fresnel square. Its augmented Gram is

`Gamma = [[c^Tc,c^Ts],[s^Tc,s^Ts]]
        = [[||b||^2,b_1],[b_1,1]]`,                               (4.12)

so

`det Gamma=b_2^2`.                                                 (4.13)

Moreover `[c,s]=V[b,q]` spans the whole two-dimensional physical transverse subspace because `b_2!=0`. Hence the normalized augmented leverage at leaf `j` is exactly the projection leverage

`(c_j,s_j) Gamma^(-1) (c_j,s_j)^T
 = e_j^T V V^T e_j
 = ||v_j||^2 <=1/2`.                                              (4.14)

Theorem MF therefore gives the **actual characteristic-function inequality**

`|phi_Q(t)|
 <= (4*pi)^(3/2)/(2 sqrt(|lambda| det Gamma)) |t|^(-3/2)
 =  (4*pi)^(3/2)/(2 sqrt(D)) |t|^(-3/2).`                         (4.15)

Together with `|phi_Q|<=1`,

`integral_R min(1,K|t|^(-3/2)) dt=6K^(2/3)`,                     (4.16)

and Fourier inversion yields

`||p_Q||_infinity
 <=(1/(2*pi))*6[(4*pi)^(3/2)/(2 sqrt(D))]^(2/3)
 =3*2^(4/3)D^(-1/3)`.                                             (4.17)

The integrable envelope also gives a continuous `C_0` representative. QED.

### Relation to the completed partner

At `a=0`, equation (4.5) is exactly the `h=1` specialization of the completed account03/B10 inequality (2.1). Theorem 4.1 therefore extends that paid null point across **every** nonzero pivot on the rank-one transverse-compression face, without paying any negative power of `|a|`.

The mechanism is source-valid: the nonzero hub square `aX_0^2` is allowed by Theorem MF and is never declared small. The original hub coordinate stays independent of the leaves, and no spectral projection is declared independent.

## 5. The required ruled theorem removes the opposite side before any near-null work

If `|a|<1`, `M` cannot be definite because `sigma_min(M)>=1` would force `|r^TMr|>=1` for every unit `r` in a definite matrix. Thus the near-null collar is indefinite.

For inertia `(2,1)`, the required source Theorem C gives the real inequality

`boxed: p_Q(s)<=pi sqrt(2) for every s>=0.`                        (5.1)

For inertia `(1,2)`, apply (5.1) to `-Q`, paying `s<=0`. Therefore a near-null proof should never spend effort re-proving that one-sheet side. The remaining geometric debt is the opposite two-sheet side.

## 6. Target-valid obstruction: the one-sided square-peel majorant diverges logarithmically on the strictly two-sheet side

The following family lies inside Theorem 4.1, so the **true** density is uniformly bounded. It nevertheless makes the natural conditional-square majorant diverge.

Fix `0<eps<=1/8` and put

`c_eps=sqrt(1+eps)`,

`M_eps=[[eps,c_eps,0],[c_eps,0,0],[0,0,1]]`.                      (6.1)

Its spectrum is exactly

`{1+eps,-1,1}`.                                                    (6.2)

Use the Parseval physical rows

`e_1`, `e_2/sqrt(2)`, `e_2/sqrt(2)`, `e_3/sqrt(2)`, `e_3/sqrt(2)`. (6.3)

Thus the physical hub has leverage one and every transverse leaf leverage is exactly `1/2`.

Choose independent source laws as follows:

- `X_0` uniform on `[-1/2,1/2]` (density one);
- `Y_1,Y_2,W_1,W_2` uniform on `[-1/sqrt(2),1/sqrt(2)]` (density `1/sqrt(2)<=1`).

Set

`Z_2=(Y_1+Y_2)/sqrt(2)`, `Z_3=(W_1+W_2)/sqrt(2)`.                  (6.4)

The two are independent, and each has the exact triangular density

`f_Z(z)=1-|z|`, `|z|<=1`.                                        (6.5)

The target quadratic form is

`Q_eps=eps X_0^2+2c_eps X_0 Z_2+Z_3^2`.                           (6.6)

Theorem 4.1 applies with `D=1+eps`, giving the actual uniform bound

`boxed: ||p_(Q_eps)||_infinity
 <=3*2^(4/3)(1+eps)^(-1/3)
 <7.560.`                                                         (6.7)

On the source-paid one-sheet side, (5.1) further gives `p_(Q_eps)(s)<=pi sqrt(2)` for `s>=0`.

Now complete the square in the hub coordinate for `eps>0`:

`Q_eps = eps (X_0+(c_eps/eps)Z_2)^2 + R_eps`,                     (6.8)

`R_eps = Z_3^2-L_eps Z_2^2`, `L_eps=(1+eps)/eps`.                 (6.9)

The standard translation-uniform scalar-square kernel says that, conditional on the leaves, the density of the first term is bounded by `(eps u)^(-1/2) 1_(u>0)`. Hence the corresponding one-sided majorant at level `s` is

`K_eps(s):=eps^(-1/2) E[(s-R_eps)_+^(-1/2)]`.                    (6.10)

Take the **strictly two-sheet level**

`s_*=-1/16`                                                       (6.11)

and put `B=1/4`. Since `eps<=1/8`, `L_eps>=9`. On the rectangle

`2B/sqrt(L_eps) <= z_2 <= B`, `|z_3|<=B`,                         (6.12)

one has

`s_*-R_eps=L_eps z_2^2-z_3^2-B^2 >=2B^2>0`,                      (6.13)

while also `s_*-R_eps<=L_eps z_2^2`. Because (6.5) gives `f_Z>=3/4` on `[-B,B]`,

`E[(s_*-R_eps)_+^(-1/2)]
 >=(9/16) int_(2B/sqrt(L_eps))^B int_(-B)^B
      (L_eps z_2^2)^(-1/2) dz_3 dz_2
 = (9B)/(8 sqrt(L_eps)) log(sqrt(L_eps)/2).`                      (6.14)

Therefore

`boxed:
 K_eps(s_*)
 >= 9/[32 sqrt(1+eps)]
      log( (1/2) sqrt((1+eps)/eps) )
 -> infinity as eps->0.`                                         (6.15)

This is **not** a counterexample to QFORM: (6.7) proves the actual density is uniformly bounded. It is a source-valid counterexample to the proposed interpolation step

> "complete the near-null hub square, replace it by the worst translation-uniform square kernel, and then uniformly bound the resulting one-sided half-Riesz expectation on the two-sheet side."

The right-hand side of that very majorant diverges logarithmically on an admissible target family. Any successful punctured-collar proof must preserve more of the joint hub/cross oscillation before taking absolute values. Theorem MF does exactly that on the rank-one transverse-compression face.

## 7. What changed in the proof map

This run makes three concrete changes.

1. The exact-null partner endpoint is joined to a **nonzero** near-null class with no pivot loss: if a pure physical coloop has rank-one transverse compression and transverse leverage at most `1/2`, then (4.5) holds uniformly for all `a`.
2. The source ruled theorem is explicitly consumed: one-sheet levels are already bounded by `pi sqrt(2)` in the indefinite collar.
3. A natural two-sheet scalar-square interpolation is ruled out by (6.15), even though the same family is paid by the mixed-Fresnel inequality (6.7).

The surviving near-null difficulty is therefore not "small nonzero pivot" by itself. It is the genuinely higher-rank collision in which the leaf transverse self-curvature has rank two (or mixed original rows prevent the pure-coloop product split), while the null endpoint collapses to the partner's rank-one mixed-Fresnel geometry.

The full exact-rank-three theorem remains OPEN. The full arbitrary-extra-spectrum owner target remains OPEN. No target counterexample is claimed.

## 8. Integrity / provenance

- Original source coordinates remain independent throughout every probabilistic step.
- Spectral bases are used only for deterministic matrix identities.
- No moment, support, log-concavity, identical-law, Gaussian, or continuity assumption is imposed on the inputs.
- Continuity is proved only in Theorem 4.1 through the integrable characteristic-function envelope; it is not promoted globally.
- The logarithmic construction uses explicit probability densities all bounded by one and an exact target spectrum satisfying the three-large-eigenvalue hypothesis.
- No finite numerical experiment is used as proof.
