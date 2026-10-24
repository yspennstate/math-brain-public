# FOREST / account01 B20 — fixed-graph Cocks closure independently verified

**Run id:** `20260922T032104Z-b20-forest-r12`  
**Target:** for every finite simple graph `G`, under the uniform law on all acyclic edge subsets, prove pairwise negative correlation of distinct edge indicators.  
**Outcome:** `FULL_PROOF_CANDIDATE`  
**Target status outside this private campaign:** still publicly listed as open/partial as of the 22 September 2026 source check; no public solution claim is made here.  
**Brain context:** `WITHOUT_VERIFIED_BRAIN`.

## 1. What this run actually closes

The preceding B20 run had independently proved an exact complete-subdivision reduction, but deliberately left the complete-graph-to-all-graphs transfer source-insecure because an older Semple--Welsh working-paper argument only established a class-level parallel-copy implication. The newest campaign-lead version, `FOREST-KN-COCKS-RECONCILED-v3` (account01/B01 run `20260922T030948Z-b01-forest-auto11`, report blob `58b8b1d8ac522a4eda7479400820e590c12f22aa`), says the final published Semple--Welsh paper contains a stronger post-submission theorem of Cocks: if the unit forest conjecture holds for one graph `G`, then its graphic matroid `M(G)` is independence correlated, meaning the full all-positive-weight Rayleigh inequality for independent sets.

I independently checked the final author PDF rather than relying on the lead's quotation. The exact statement appears in the Note on printed page 13:

> Cocks has shown that if Conjecture 1.1 holds for a graph `G`, then `M(G)` is independence correlated.

In the same final paper, `independence correlated` is defined to mean nonnegative independent-set Rayleigh difference for every positive real weighting and every distinct element pair, and Proposition 3.5 proves this property is closed under deletion and contraction minors by the `epsilon -> 0+` / `epsilon -> infinity` limits.

Thus the previously unpaid universal transfer is not a conjectural extra lemma: it is a published theorem dependency plus a published minor-closure proposition. Applying them to the exact complete-graph theorem gives the all-graph theorem immediately.

Sources checked directly:

- C. Semple and D. Welsh, *Negative Correlation in Graphs and Matroids*, Combin. Probab. Comput. 17 (2008), 423--435, DOI `10.1017/S0963548307008978`; final author PDF `https://www.math.canterbury.ac.nz/~c.semple/papers/SW07.pdf`. Definition of independence correlation on printed p.4, Proposition 3.5 on printed p.7, and the Cocks Note on printed p.13.
- C. C. Cocks, *Correlated Matroids*, Combin. Probab. Comput. 17 (2008), 511--518, DOI `10.1017/S0963548308009152`. The article abstract says it proves equivalences between the Grimmett--Winkler/Pemantle conjectures and correlated graphic-matroid statements. The complete original article text was not directly available in this run, so the fixed-graph theorem is source-bound through the explicit final Semple--Welsh Note.
- G. R. Grimmett and S. N. Winkler, *Negative association in uniform forests and connected graphs*, Random Structures & Algorithms 24 (2004), 444--460, DOI `10.1002/rsa.20012`.

A useful source distinction is preserved: an older working-paper Proposition 2.1 used parallel copies to show only the global statement `all graphs unit pNC => all graphic matroids independence correlated`. That older proof does not establish the fixed-graph implication. The final published Note explicitly records Cocks's later stronger fixed-graph theorem and therefore resolves, rather than ignores, that objection.

## 2. Named other-account result consumed and applied

I consumed the newest assigned partner result from **account04/B03**, run `20260922T030927Z-B03-forest-r11`:

- checker source blob `d41b4a5172e7f9b2b746e35895ed3ed1965aef75`;
- checker output blob `96901796ef7a3ff813dcb9bcae9d66ef00f830f7`.

Its exact output independently verifies the complete-graph counts on `K_3,...,K_6`, checks the Hermite lower-bound/gap chain through `n=500`, and reports

```
K3 adjacent=(7, 3, 3, 1, 2)
K4 adjacent=(38, 14, 14, 4, 44) disjoint=(38, 14, 14, 5, 6)
K5 adjacent=(291, 93, 93, 23, 1956) disjoint=(291, 93, 93, 29, 210)
K6 adjacent=(2932, 822, 822, 178, 153788) disjoint=(2932, 822, 822, 226, 13052)
HERMITE_EXACT_REVIEW_PASS n=6..500
GENERALIZED_CAYLEY_DISJOINT_COMPONENT_CHECK m=0..12 PASS
```

I applied that result as an independent check on Step A below rather than treating it as a proof by finite testing. I also ran an independent B20 exact checker from scratch, stored as `b20_checker.py`; it brute-enumerates `K_3,...,K_6` and verifies the exact rational Hermite inequalities for every `6<=n<=1000`. Its output is stored as `b20_checker.out` and ends with `B20_HERMITE_EXACT_REVIEW_PASS n=6..1000`.

## 3. Compact complete proof candidate

For a graph `G=(V,E)`, let

`I_G(y)=sum_{F forest of G} product_{a in F} y_a`.

For distinct `e,f`, let `I_e,I_f,I_ef` denote the weighted sums restricted to forests containing the specified marked edges. The pairwise forest inequality is exactly

`Delta_G(e,f;y)=I_e I_f-I_ef I_G >= 0`

at `y_a=1` for every edge. The independent sets of the graphic matroid `M(G)` are exactly the forests of `G`.

### Step A. Unit pairwise negative correlation on every complete graph

Let `R(z)` be the rooted labelled-tree EGF, so

`R=z exp(R)`.

Let

`T=R-R^2/2`, `F=exp(T)`, `A=T'=exp(R)`.

For `K_n`, symmetry gives one single-edge orbit and two two-edge orbits. Exact marked-component decompositions give

`Z_n=n![z^n]F`,

`E_n=(n-2)![z^(n-2)]F A^2`,

`J_adj,n=(n-3)![z^(n-3)]F A^3`,

and for disjoint marked edges

`J_dis,n=(n-4)![z^(n-4)]F A^4(1+4/(1-R))`.

The last formula has two cases. If the two marked edges lie in different forest trees, deleting them gives four distinct rooted components (`F A^4`). If they lie in the same tree, deleting them gives three components: two outer rooted components and a middle tree containing one endpoint of each marked edge. There are four choices of middle endpoints and `T''=A'=A^2/(1-R)`, giving the additional `4F A^4/(1-R)` term.

For probabilists' Hermite polynomials `He_m`, Cauchy's change of variables `z=u exp(-u)` gives, for `x=m+a`,

`m![z^m] exp(aR-R^2/2)=He_m(x)-m He_(m-1)(x)`,

because the Jacobian contributes `(1-u)`, while

`m![z^m] exp(aR-R^2/2)/(1-R)=He_m(x)`.

All four forest counts above have the same Hermite argument `x=n+1`. Write

`H_j=He_j(n+1)`, `D_j=H_j-jH_(j-1)`, and `k=n-4`.

Then

`Z_n=D_n`, `E_n=D_(n-2)`, `J_adj,n=D_(n-3)`,

`J_dis,n=D_k+4H_k=5H_k-kH_(k-1)`.

Set `a=H_k>0` and

`s=k H_(k-1)/H_k`.

The Hermite recurrence yields

`J_dis=a(5-s)`,
`J_adj=a(4-s)`,
`E=a(2n+6-3s)`,
`Z=a(n^2+3n+10-(n+4)s)`.

Hence the harder disjoint-pair Rayleigh gap is

`E^2-Z J_dis=a^2 G_n(s)`

with

`G_n(s)=(5-n)s^2+(n^2-4n-6)s-n^2+9n-14`.

To bound `s`, use the standard symmetric Jacobi matrix for `He_k`; its roots are real and symmetric `+/-lambda_i`, lie strictly below `x=k+5` in absolute value, and satisfy

`sum_i lambda_i^2=k(k-1)`.

Therefore

`s=H_k'(x)/H_k(x)=sum_i 1/(x-lambda_i)`.

Pairing `+/-lambda` and using

`2x/(x^2-lambda^2) >= 2/x+2lambda^2/x^3`

gives

`s >= k/x+k(k-1)/x^3 = L_n`,

where

`L_n=(n-4)(n-1)(n+4)/(n+1)^3`.

Also `D_k=H_k(1-s)>0`, because it is a positive coefficient of `exp(5R-R^2/2)`, so `0<=s<1`.

For `n>=6`,

`G_n'(s)=2(5-n)s+n^2-4n-6`

is positive on `[0,1]` (its minimum there is `n^2-6n+4>0`). Thus

`G_n(s)>=G_n(L_n)=P(n)/(n+1)^6`,

where

`P(n)=2n^6+70n^5-33n^4+185n^3+1369n^2-3147n+1170`.

Writing `n=t+6`,

`P(t+6)=2t^6+142t^5+3147t^4+33233t^3+187651t^2+551661t+666396`,

which is strictly positive for every `t>=0`. Hence every disjoint marked pair in every `K_n`, `n>=6`, has positive gap. Since

`J_dis=J_adj+H_k`

and `H_k>0`, the adjacent gap is larger. The small cases are exact:

- `K_2`: no distinct pair;
- `K_3`: `(Z,E,J_adj)=(7,3,1)`, gap `2`;
- `K_4`: disjoint gap `14^2-38*5=6`;
- `K_5`: disjoint gap `93^2-291*29=210`.

Thus Conjecture 1.1 holds for every complete graph `K_n`.

### Step B. Published fixed-graph upgrade

The final Semple--Welsh paper defines `M` to be independence correlated precisely when

`Delta_I(M;y)>=0`

for every pair and every positive real edge weighting `y`. Its final Note records Cocks's theorem:

> If Conjecture 1.1 holds for a graph `G`, then `M(G)` is independence correlated.

Apply this theorem to each `K_n`. Step A therefore upgrades the unit result to

`Delta_{K_n}(e,f;y)>=0`

for every positive weighting `y` and every distinct pair.

This is the exact previously unpaid universal step.

### Step C. Minor closure

Semple--Welsh Proposition 3.5 proves independence-correlated matroids are minor-closed. For deletion of an edge `a`, assign `y_a=epsilon` and take `epsilon->0+`; for contraction, rescale by `epsilon^-2` and take `epsilon->infinity`. The corresponding Rayleigh difference limits are precisely those of `M\a` and `M/a`.

Thus every deletion minor of `M(K_n)` is independence correlated.

### Step D. Arbitrary finite simple graph

Let `G` have `n` vertices. Delete from `K_n` every edge not in `G`. The resulting graphic matroid is `M(G)`; isolated vertices do not affect the matroid or forest counts. Hence `M(G)` is independence correlated by Step C. Evaluate its positive weights at `y_a=1` for every surviving edge. This is exactly the uniform law over **all** acyclic edge subsets, with every size and disconnected forests included. Therefore for every distinct `e,f in E(G)`,

`Pr(e,f in F) <= Pr(e in F) Pr(f in F)`.

This includes all finite simple graphs and all degenerate cases.

## 4. Independent exact computation used only as an audit

The local B20 checker produced:

```
K3 adjacent=(7, 3, 3, 1, 2)
K4 adjacent=(38, 14, 14, 4, 44) disjoint=(38, 14, 14, 5, 6)
K5 adjacent=(291, 93, 93, 23, 1956) disjoint=(291, 93, 93, 29, 210)
K6 adjacent=(2932, 822, 822, 178, 153788) disjoint=(2932, 822, 822, 226, 13052)
B20_HERMITE_EXACT_REVIEW_PASS n=6..1000
```

The script uses exact integers/Fractions only. It is not used in place of the all-`n` proof.

## 5. Current-source / novelty caution

A bounded fresh literature check still found the Grimmett--Winkler pairwise uniform-forest conjecture publicly described as open in full generality. The March 2026 Tang--Zhang preprint treats fixed-component forest measures and related complete-graph families for sufficiently large `n`, not the all-size uniform forest law on arbitrary graphs. Therefore this campaign candidate appears to go beyond the readily found public partial results, but a search miss is **not** a priority certificate.

Before any external announcement, publication, or claim of resolution, the original Cocks article should be inspected directly (or the fixed-graph theorem confirmed by an expert/reference with the proof in hand), and the Hermite derivation should receive ordinary journal-level review. The final Semple--Welsh paper is nonetheless explicit enough that there is no remaining *logical* implication missing from the candidate when cited as a published theorem.

## 6. Honest classification

**`FULL_PROOF_CANDIDATE`.**

Reason: the lead's complete-graph argument has an all-`n` symbolic proof; the named other-account checker independently supports its exact formulas; this run independently reproduced the key Hermite chain through `n=1000`; and, most importantly, the previously disputed fixed-graph weighted upgrade plus minor closure are explicitly present in the final published Semple--Welsh source. The complete chain contains all quantifiers and boundary cases.

This is not a public solved-problem declaration and not a novelty claim. The decisive next action is publication-grade source/proof scrutiny, especially direct inspection of Cocks's 2008 proof, not reopening an already-closed local switching route merely to generate activity.
