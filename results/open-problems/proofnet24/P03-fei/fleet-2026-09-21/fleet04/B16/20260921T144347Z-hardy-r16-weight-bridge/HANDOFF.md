# B16 FEI handoff — exact Hardy/R16 parity weight bridge

**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full FEI:** **OPEN / NOT PROVED**.

New exact theorem: if
\[
a_{v,q}=\sum_{A:v\in R_A,\ q_A=q}c_A,\qquad
u_{v,q}=\frac{q-1}{q}a_{v,q},
\]
and
\[
\Gamma_j=\sum_v\sum_{q+r=j}\nu_{v,q}\nu_{v,r},
\]
then the actual **low-half contribution** of the radial Hardy bank is
\[
\boxed{
\mathcal L_-=\frac12\sum_vV_{-,v}
=\sum_{\substack{j\ge6\\j\ {\rm even}}}
\frac{\Gamma_j}{(j-1)2^{j-1}}.
}
\]
These are exactly the scalar weights of the inherited R16 high-resolvent collision bank.

The parity information is useful, not cosmetic. Every frustrated `q_A` is odd; the Hardy multiplier kills `q=1`; hence the low radial demand touches only even collision orders `j>=6`. It uses neither R16 `j=2,4` nor any odd-order refund.

The reachable positive-even R16 envelope is therefore only
\[
\sum_{\substack{j\ge6\\j\ {\rm even}}}
\frac{j}{(j-1)2^{j-1}}
=
\boxed{\frac{\ln3-1}{2}}
=0.0493061443340548\ldots.
\]
The newest fleet01 high-resolvent result independently leaves an aggregate R16 bank floor
\[
[\kappa_2-2\ln(3/2)-\varepsilon_d]J.
\]
Thus if the remaining authentic signed moment bridge
\[
\sum_{j\ge6,\ even}w_j\Gamma_j
\le
\sum_{j\ge6,\ even}w_jD_{d,j}
\]
is proved, the entire low radial half costs at most `((ln3-1)/2) J` and fits strictly inside that already-proved bank floor, leaving the terminal machinery to the high radial half plus bridge scalar.

Do **not** try to prove `Gamma_j>=0`: it is false. A one-site example has
\[
\Gamma_6=16/9,\quad \Gamma_8=-32/15,\quad \Gamma_{10}=16/25.
\]
The genuine q=3 `+1/8,-1/8` Boolean/Borel diagnostic retains a negative radial refund `-1/180`, whose low-half contribution is exactly `-1/5760`.

Next attack: prove or refute the single weighted signed domination above directly from the authentic Borel coefficients and the even symmetric-difference identity
\[
|R_A\cap R_B|=(q_A+q_B-q_{A\triangle B})/2,
\]
without taking absolute values.
