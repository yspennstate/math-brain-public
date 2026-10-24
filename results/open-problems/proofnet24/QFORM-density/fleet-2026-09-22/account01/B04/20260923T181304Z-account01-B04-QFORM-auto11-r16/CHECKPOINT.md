SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B04, 2026-09-23T18:13:04Z.
attacking: close the quantitative compound-hub branch left by the Gibbs third-volume dichotomy using the arbitrary-rank grouped-crossing theorem and exact Gram-volume identities.

# Early substantive checkpoint

Status: calculation in progress; full QFORM remains open.

Let `M=A[I,J]` be an original-coordinate cross block and `H subset I`, `L=I\H`. For each independent `K subset H`, `r=|K|<=3`, put

`Delta_K = det(M_K M_K^T)`, `P_K = projection onto rowspan(M_K)`, `C_K=M_L(I-P_K)`,

and

`Gamma_K = Delta_K E_{3-r}(C_K)` (with `E_0=1`).

The Gram Schur-complement identity gives exactly

`Gamma_K = sum_{S subset L, |S|=3-r} det(M_{K union S} M_{K union S}^T)`.

Therefore

`E_3(M)=E_3(M_L)+sum_{nonempty K subset H, |K|<=3} Gamma_K`.

The planned analytic closure is:

* `r=3`: exact-rank crossing on the three original hub coordinates gives `||p_Q||_infty <= 3 sqrt(2) Gamma_K^(-1/6)`.
* `r=2`: if the canonical `E_1(C_K)` row marginals are all <=1/2, the checked grouped-crossing theorem (`k=2, ell=1`) gives `3*2^(5/6) Gamma_K^(-1/6)`. If one marginal exceeds 1/2, promote that physical light row to the hub; the new 3-row Gram volume is `>Gamma_K/2`, and the previous line pays it.
* `r=1`: if the canonical `E_2(C_K)` row marginals are all <=1/2, grouped crossing (`k=1, ell=2`) gives `C12 Gamma_K^(-1/6)` with `C12=3*2^(7/6)*exp(1/3)=9.3991318878...`. If a row marginal exceeds 1/2, promote that row. The promoted two-hub currency is `>Gamma_K/2`; the `r=2` branch then costs at most `6 Gamma_K^(-1/6)<C12 Gamma_K^(-1/6)`.

Hence every nonzero `Gamma_K` should be payable by `C12 Gamma_K^(-1/6)`, with arbitrary within-bank curvature retained by original-coordinate conditioning and the complex-measure grouped-crossing theorem.

If `|H|<=4` and `E_3(M_L)<=E_3(M)/2`, there are at most `4+6+4=14` nonempty K terms, so some `Gamma_K>=E_3(M)/28`; this would yield

`||p_Q||_infty <= C12*28^(1/6) E_3(M)^(-1/6)=16.3787498048... E_3(M)^(-1/6)`.

Combined with the earlier Gibbs soft-hub theorem at `h=3/5` and threshold `g=E_3(M)/2`, this appears to remove *all* marginal/entropy gates for a fixed cross block with `E_3(M)>0`. The high-currency branch has coefficient `5 e sqrt(5/6) 2^(1/6)=13.9266136991...`, so the preliminary universal fixed-cross-block coefficient is `16.3787498048...`.

The remaining full-target problem, if this proof checks, is then purely deterministic routing from the three-large-eigenvalue hypothesis to either a target-scale `E_3` cross block or one of the already-paid diagonal/low-cross-rank/hub mechanisms.