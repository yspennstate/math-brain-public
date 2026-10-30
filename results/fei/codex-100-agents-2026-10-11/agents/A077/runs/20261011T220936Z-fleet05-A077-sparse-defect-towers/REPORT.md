# A077 / B16: a multiscale surcharge failure with exact KL cancellation

## exact target, quantifiers, hypotheses and units

Entropy and relative entropy are in bits; all physical inputs are independent fair bits and outputs are signs. This stage tests the specific candidate that every complete one-coordinate restriction tree can pay its cumulative **blind** minority-mismatch surcharge

\[
R_{\mathcal T}=\sum_v w_v M_v\log_2(1/M_v)\le K I(f)
\]

with one absolute finite K. Here parent Fourier masses in a residual fiber are u_T^2,v_T^2; q_T=u_T^2+v_T^2, m_T=min(u_T^2,v_T^2), M=sum m_T, and nu_T=m_T/M. These are the exact minority masses of the pinned isospectral-splicing interface, not ordinary disagreement unless explicitly calculated. Zero-M contributions vanish.

For every n>=1 and every ordered partition n=r_1+...+r_L into positive integers, take mutually disjoint fresh physical blocks z^(j), A_j=1{z^(j)=0}, F_0=-1, F_j=1+A_j(F_(j-1)-1). Then

\[
F_L=1-2\prod_j A_j=f_n=1-2\mathbf1_{\{x=0\}}.
\]

The probability of the defect after scale j is 2^(-r_1-...-r_j). No controls are reused. The nested changes overlap completely on the final defect, so entropy additivity across activation scales would be unjustified; the product-indicator expansion below computes this interference exactly.

Result: for any complete physical one-coordinate restriction tree on this function, skipping irrelevant queries,

\[
R_{\mathcal T}=2^{-n}n(n-1),\qquad I(f_n)=2n2^{-n},\qquad R_{\mathcal T}/I=(n-1)/2.
\]

Thus no finite K pays this candidate, even by optimizing the queried coordinate order. In contrast the exact corrected charge

\[
Q_{\mathcal T}=\sum_v w_v M_v[\log_2(1/M_v)-D_2(\nu_v\Vert q_v)]
\]

satisfies Q<=2I, Q/I->1, and H(f_n)<=4I with H/I->4. This is an intermediate overcharge counterfamily, not a counterexample to FEI or to the retained-KL stopping-tree target. Independent review is pending; no novelty or formal certification is claimed.

## sources actually read, revisions and theorem locators

The execution protocol was read in full: fei-execution-protocol/2, revision 2026-10-11-execution-v2. README, CURRENT_STATUS, the claim/obstruction/packet registries, STREAM_NEXT_ACTIONS and the campaign TeX plan were read for the target and ownership rules; A077's acceptance contract explicitly requires cross-scale interference and the distinction between local surcharge and H/I. BOARD.md was read at stage start (snapshot 2026-10-11 22:05 UTC). B16/STREAM_NOTES.md is absent at the supplied path, so no lead direction was available. There were no existing rolling files in this agent folder.

Earlier local B05, B09 and B19 run reports were read, in particular B05 Sections 3-7 and B19 Sections 2 and 4: the accepted bent local-refund no-go does not settle global nonreuse. No unreviewed B09 conclusion is used.

The supplement's CAMPAIGN, CLAIMS, COUNTEREXAMPLES, SEED_LEMMAS and NATIVE_MAPPING were read. SEED_LEMMAS Section 3 already supplies the point-defect spectrum and Shannon asymptotic; those are calibration, not claimed discoveries. The new calculation is the complete physical path's raw versus retained-KL multiscale ledger and its coordinate-order robustness. Relevant source notes read: LOG_ALLOCATION_CURATED Sections 2-6; ERASURE_REDUCTION Sections 1-6; BLOCK_RESTRICTION_IDENTITY Sections 1-5; ISOSPECTRAL_SPLICING_CURATED Theorems 3.2-3.3 and Corollary 3.4. The latter's original commit is fe94de760ee2b47545419a7447b492816bd16045, blob 3421c0cbfd22031554befb962ec92cd0c8bb45b9. Remaining curated source notes were inspected for tower and logarithmic-payment overlap. The child-defect logarithm Lambda from LOG_ALLOCATION Section 5 is **not** refuted here: one child is constant, so its kappa_min is zero.

The four supplied paper text files were decoded as cp1252 after UTF-8 decoding failed. Relevant passages inspected: threshold_paper_38pp Section 8.4, Proposition 8.9 and Corollary 8.10 (text lines 2583-2644), Section 8.1 selector separation; earlier threshold version for composition and normalization; both percolation versions' introduction, entropy normalization and stated geometric scope. Percolation's geometry does not enter the proof. Text SHA256 hashes and all local source paths are saved in out/SOURCE_RECEIPTS.json. No web lookup or Brain query was needed for the self-contained calculation.

## complete derivation or exact first unsupported line

Write p=2^-n. Every indicator coefficient is p, since the selected point is zero in binary Walsh coordinates. Consequently fhat(empty)=1-2p and fhat(S)=-2p for every nonempty S. In particular all cross-scale signs and coefficients are retained. Parseval is (1-2p)^2+(2^n-1)4p^2=1. Each coordinate influence is 2p, by counting the single disagreeing undirected edge or summing its 2^(n-1) spectral masses. Thus I=2np. The exact entropy is

\[
H=(1-2p)^2\log_2\frac1{(1-2p)^2}+8p(1-p)(n-1).
\]

Let v=4p(1-p). The empty term is -(1-v)log2(1-v)<=v/ln2, by -ln(1-v)<=v/(1-v), with endpoint continuity. Hence

\[
H/I\le (1-p)[4(n-1)/n+2/(n\ln2)]\le4.
\]

The n=1 case has H=0 and I=1. As n grows the empty term divided by I vanishes and the tail ratio tends to 4.

Now reveal any physical coordinate. A restriction missing the defect is constant +1; the sole surviving branch is f_(n-1). For any adaptive choice of subsequent coordinate there remains exactly one nonconstant node at each residual dimension m, with history probability w_m=2^(-(n-m)). The labels of the queried coordinates may change but the residual point-defect spectrum does not. All complete coordinate trees therefore have the same ledger. At m=1 the function is a character, so M=0, B=JS=0, while the queried ordinary influence is one.

For m>=2 write d=2^(-(m-1)) and p_m=d/2. The parent residual fiber with T empty has

\[
u_0=1-d,\quad v_0=-d,\quad q_0=(1-d)^2+d^2=1-2d+2d^2;
\]

each of the 1/d-1 other fibers has u_T=v_T=-d and q_T=2d^2. Since d<=1/2, every minority mass is d^2, including the tie at m=2. Hence M=d and nu is uniform with mass d on each residual fiber. This is also the ordinary queried influence at m>=2. The raw weighted charge of this one level is

\[
w_m M\log_2(1/M)=2^{1-n}(m-1).
\]

Summing m=2,...,n yields R=2^-n n(n-1). The same final rarity is used repeatedly in the **surprisal multiplier**: its weighted minority mass is 2^(1-n) at every surviving level. The ordinary influence allocation itself is legitimate and nonreusing, sum_(m=1)^n w_m Inf=2n2^-n; it is the blind surcharge that repeatedly prices the unresolved rarity.

For the rebate, directly compute

\[
D_2(\nu\Vert q)=(1-d)\log_2\frac1{2d}+d\log_2\frac d{q_0},
\]

\[
a_m:=\log_2(1/d)-D_2(\nu\Vert q)
=1-d+2d(m-1)+d\log_2 q_0.
\]

Equivalently M a_m=sum_T m_T log2(q_T/m_T). Each q_T>=2m_T, so a_m>=1. Since q_0<=1 and l/2^l<=1/2 for every integer l>=1 (by induction), a_m<=1+2d(m-1)<=2. Therefore

\[
Q=2^{1-n}\sum_{m=2}^n a_m\le2I,
\quad
1-1/n\le Q/I\le1+3/n.
\]

The last upper bound follows by dropping negative terms in a_m and using sum_(l>=1) l/2^l=2: sum a_m<=n-1+4=n+3. Thus Q/I->1. For n=1 Q=0. The corrected tree charge has a finite price without borrowing a separate ancestor influence reserve. The discarded total KL credit is exactly R-Q, so its leading term is the entire quadratic raw overcharge.

The exact erasure at residual m is

\[
B_m=2d(1-d)+q_0h_2(d^2/q_0).
\]

The residual marginal q consists of q_0 and 1/d-1 copies of 2d^2. Therefore JS_m=H(q)-H(f_(m-1))/2 and Delta_m=H(f_m)-H(f_(m-1))/2=B_m+JS_m. Weighted by w_m, these telescope to H(f_n); terminal entropy is zero. This exact telescope is verified independently of the raw surcharge identities in the checker.

For disjoint tensor factors product_j f_(n_j), spectra are independent, so H and I add. A sequential tree that completes one factor before the next has additive R and Q: a remaining independent tensor factor multiplies q and m by its spectral masses, preserving M and cancelling from nu/q and hence from KL. Both signs at completed leaves merely translate or preserve spectra. Thus

\[
R=\sum_j2^{-n_j}n_j(n_j-1),\quad I=\sum_j2n_j2^{-n_j},\quad Q\le2I,\quad H\le4I.
\]

No such additivity is asserted for overlapping defect flips. Nested activations here were collapsed by their actual Boolean identity, not treated as disjoint spectral pieces.

The first unsupported line toward full FEI would be: every Boolean function admits a proper physical stopping tree whose retained-KL Q and terminal entropy are O(I). This calculation proves that statement only for the explicit point-defect towers and their disjoint tensor products. It neither proves it universally nor exhibits failure of the retained-KL charge on any other family.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json was saved before the pilot. The final helper's pilot covered dimensions 1..6, 63 ordered partitions and five tensor controls: 216 exact assertions passed, 0.0262 seconds of measured Python runtime. Full validation covered compressed dimensions 1..32, full integer Walsh spectra in dimensions 1..12, every ordered block partition for n=1..8 (255 cases), and five declared tensor tuples: **2,520 assertions passed**, measured Python runtime 0.7991 seconds. No randomness, automatic dimension increase, GPU, background worker or heavy job was used. Expected memory is under 60 MB, below the memok threshold; no observed peak-memory measurement is claimed.

Commands from the agent folder:

```
python -X utf8 runs\20261011T220936Z-fleet05-A077-sparse-defect-towers\code\check.py pilot
python -X utf8 runs\20261011T220936Z-fleet05-A077-sparse-defect-towers\code\check.py full
```

All spectral and influence identities use integers and Fraction arithmetic. Logarithms use the positive atanh series after dyadic reduction to [1,2], 32 terms, with remainder 2z^65/[65(1-z^2)]; endpoints are divided by the positive enclosure of ln2 and rounded outward to denominator 2^120. Entropy intervals preserve signs by multiplication with nonnegative masses. Output values are exact rational intervals, not floating certificates. Runtime is the only floating field. The initial full validation passed its mathematical checks but could not serialize the unrestricted rational denominators under Python's 4,300-digit guard; this was repaired using exact outward dyadic rounding and rerun successfully. A prior code inspection also moved truth-table allocation inside the n<=12 guard before the full run. Neither issue altered the theorem or family.

The full output out/validation.json has SHA256 4babc7cac516bd8ef73504559619fec649851068d4ac31578f1975740084e347. The code is an author self-check; it does not count as independent agent review.

## proof dependencies and changed downstream conclusions

The new all-n proof is self-contained; no unreviewed campaign claim is a premise. The definitions and intended stopping-tree use are source-pinned to ISOSPECTRAL_SPLICING Theorem 3.2 and Corollary 3.4; point-defect spectrum and tensor entropy laws were already baseline. Changed downstream conclusion: a candidate dropping the exact KL rebate cannot be repaired merely by optimizing a complete one-coordinate order on these towers. The retained-KL candidate survives this test and pays the entire multiscale contribution with an explicit constant. The child-kappa logarithm is a distinct candidate and is not refuted. JSON uses the explicit compatibility key packet_ids; the protocol field list's parenthetical description is treated as annotation, as required by its compatibility paragraph and this assignment.

## one next mathematical action and independent reviewer

Next: replace the constant terminal seed with a bent seed plus one point surgery, retain all signs and the exact parent minority masses, and determine whether cumulative Q/I grows with the number of fresh activation levels after subtracting the paid terminal spectrum. This tests whether the cancellation mechanism depends on the point defect's flat minority distribution. Intended independent reviewers: A092 and A088; next consumers A022, A023, A064, A075, A080 and B20. No message was sent and no files in their folders were modified.

## actual persistence receipts or precise save blocker

The report, complete proof TeX, CLAIMS.json, PROGRESS.json, identical PACKET_DELTA.json, frozen spec, reproducible checker, rational outputs and MULTISCALE_COST_LEDGER.json are saved in this assigned run folder. STATUS.md, WORKLOG.md and LEARNED.md are saved in the agent root. out/ARTIFACT_MANIFEST.json records local SHA256 and byte counts. Independent acceptance, supervisor copy, Brain ingestion and GitHub mirror verification have not occurred in this stage and are not claimed.

## Universal bridge

This stage moves C019 stopping-tree payment by separating the exact retained-KL charge from a rigorously refuted blind multiscale replacement: on every depth of the declared point-defect tower, raw R/I=(n-1)/2 diverges while corrected Q<=2I and Q/I->1, with zero terminal entropy and all physical influence included. The universal existence of a paid stopping tree remains open. The next bent-surgery tower test directly challenges the same retained-KL payment under nonflat minority masses, rather than repeating the already closed point-defect FEI class; it is the shortest available step here toward deciding which transport can support the universal bridge.
