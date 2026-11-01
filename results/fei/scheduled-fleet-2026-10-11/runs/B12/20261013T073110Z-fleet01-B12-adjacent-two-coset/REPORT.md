# B12 / A057 — adjacent two-coset collision payment

Run: `20261013T073110Z-fleet01-B12-adjacent-two-coset`  
Primary packet: A057 (Coherent restriction remainder)  
Stable gap: `B12-A057-COHERENT-HIERARCHY-v13`  
Status: contributor-PROVED proper-class theorem; independent A090/A091 review pending; full FEI OPEN.

## Exact delta

The preceding theorem covered two disjoint affine defect cosets only when their physical Hamming distance was at least two, with constant `16 ln 2`. The distance condition removed the negative derivative cross term between the pieces.

This run removes that condition completely and improves the constant by two:

> Let `E1,E2` be arbitrary nonempty disjoint affine cosets in a physical Boolean cube, with indicators `s1,s2` and `s=s1+s2`. Put
> `d(x,z)=1_{x=-1}s(z)`, take branches `g_-=x`, `g_+=x+2d`, and hence `a=x+d`, `b=d`, `h=-x`, `F=a+d`. Then the signed associator
> 
> `Omega = E_raw(F)-E_raw(a)-E_raw(d)`
> 
> obeys
> 
> `Omega <= 8 ln(2) I(d)`.

There is no lower bound on the distance, no orthogonality hypothesis on the translated annihilator spectra, and no dependence on dimension, codimension, number of joining coordinate directions, or spectral-overlap ratio. The point-defect family from the overlap-only falsifier shows `8 ln 2` remains asymptotically sharp.

For an adaptive nonreusing hierarchy of reached local sources of this form, all restrictions of one physical source `b`, the exact derivative ledger gives

`sum_v w_v Omega_v <= 8 ln(2) I(b)`.

## Why adjacency is paid

Write the cosets as `A=a+V`, `B=b+W`, let `L=V+W`, and let `t=b-a+L` in the quotient `G/L`. Disjointness is exactly `t != 0`. Put

- `x=|A|/|G|=2^{-k1}` and `y=|B|/|G|=2^{-k2}`;
- `ell=codim(L)` and `r=2^ell`;
- `m_j` for the number of physical coordinates active on the `j`th coset;
- `J={i:e_i+L=t}`, `q=|J|`.

The `q` directions are precisely the coordinate directions joining the two pieces. Their exact influence cancellation is

`I(s)=x m1/2 + y m2/2 - q x y r`.                         (1)

The physical coordinate columns in `G/V` span a `k1`-dimensional quotient. The `q` joining columns all have the same nonzero image in the further `ell`-dimensional quotient `G/L`; hence they span at most `min(q,k1-ell+1)` dimensions. Consequently

`m_j >= max(k_j,q+ell-1)`.                                (2)

Set `alpha=k1-ell`, `beta=k2-ell`, and assume `alpha<=beta`. The elementary integer inequality

`2q <= 2^beta(1+(q-1-alpha)_+) + 2^alpha(1+(q-1-beta)_+)`  (3)

follows in the three ranges `q<=alpha+1`, `alpha+1<q<=beta+1`, and `q>beta+1`, using `2^u>=u+1`. Equations (2)-(3) give the exact collision payment

`2q x y r <= x(m1-k1)+y(m2-k2)+x+y`.                      (4)

Thus the joining-edge cancellation is paid by unused rank plus one terminal density unit; it is not charged as an additional source influence.

## Spectral collision refund

On the common annihilator `L^perp`, the relative phase is the nontrivial character induced by `t`, so exactly half the coefficients have magnitudes `x+y` and half `|x-y|`. The scalar Hadamard inequality

`[Phi((x+y)^2)+Phi((x-y)^2)]/2 <= Phi(x^2)+Phi(y^2)`       (5)

holds for `Phi(u)=u ln(1/u)`: after the normalized Hadamard rotation, binary entropy can increase by at most `ln 2`, exactly canceled by the scale factor. Therefore spectral overlap never increases raw entropy and

`E_raw(s) <= E_raw(s1)+E_raw(s2)`
`          = 2 ln(2)(x k1+y k2)`.                          (6)

Combining (1), (4), and (6), with `p=x+y`, yields

`E_raw(s) <= 2 ln(2)(2I(s)+p)`.

The exact selector-pair identity from the preceding run is

`Omega=E_raw(s)+C(p)`, with `C(p)<=0`, and
`I(d)=I(s)/2+p/4`.

Hence

`Omega <= 4 ln(2)I(s)+2p ln(2) = 8 ln(2)I(d)`.

## Verification

`check_all_two_cosets.py` reconstructs every disjoint affine-coset pair through four source variables using exact rational Walsh coefficients, including all adjacent and genuinely non-affine unions. It also audits (3) on 518,400 integer tuples (`0<=alpha<=beta<80`, `1<=q<=160`).

- 23,000 disjoint pair decompositions;
- 19,484 adjacent pairs;
- 22,148 genuinely non-affine pairs;
- 21,304 positive-associator pairs;
- zero violations of the `8 ln 2` theorem;
- largest non-affine finite ratio: `2.950791780762193` nats per influence;
- no random seed.

## Scope and remaining gap

This is a strict class extension and constant improvement, not full FEI. It pays arbitrary physical adjacency for exactly two affine pieces. The next unpaid step is a union of three or more affine pieces: pairwise joining-column quotients need not share one relative phase, so the rank slack and Hadamard refunds must be coupled across the whole collision graph without recharging one physical derivative. The complete changing coherent remainder for arbitrary Boolean sources is still OPEN.

Independent review: pending A090/A091. No native adoption or full-FEI acceptance is claimed.
