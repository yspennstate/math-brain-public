# Fresh-source addendum: fourth-volume downshift sharpens the rank-four survivor

During the mandatory final source refresh, account01/B04 completed

`QFORM-FOURTHVOLUME-DOWNSHIFT-v1`,

canonical source

`yspennstate/math-open-problems@72d2768d509944880036a97581ff5115208bd8f4`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B04/20260923T124226Z-account01-B04-QFORM-auto11/REPORT.md`.

This is a later source than the initial run controls, so it is applied here to the rank-four subcase of `REPORT.md` Theorem 3.1.

## 1. Setup from the main report

We are in the low-fifth-tail branch

`T4=sum_(j>=5)s_j(M)^2 < q=P/4617`,

with

`a=s3(M)>16 sqrt(q)`.

Consider the subcase

`s4(M)>=a/16`.

Let `lambda_j=s_j(M)^2`, `F^2=||M||_F^2=sum lambda_j`. Then

`lambda_4>=a^2/256`.

Since `T4<q<a^2/256<=lambda_1/256`,

`F^2=lambda_1+lambda_2+lambda_3+lambda_4+T4
    <=4lambda_1+T4
    <(1025/256)lambda_1`.

Also

`E4(M)>=lambda_1 lambda_2 lambda_3 lambda_4
      >=lambda_1 a^6/256`.

Therefore the coarse fourth-volume downshift currency from account01/B04 obeys

`G>=4E4(M)/F^2 >4a^6/1025`.                                    (A.1)

## 2. A new paid range of fourth-volume marginals

Let `rho_*` be the largest canonical physical four-volume row marginal of the actual cross block `M`. If

`rho_*<=3/4`,

then the account01/B04 theorem uses

`q4=max(1,3rho_*/2)<=9/8`

and yields a continuous full-ambient density satisfying

`||p_Q||inf
 <= [3e/((3-2q4)sqrt(q4))] G^(-1/6)
 <= (8sqrt(2)e/3)(1025/4)^(1/6) a^(-1)`

`<25.836 a^(-1)
 <109.720 P^(-1/2)`.                                            (A.2)

The same applies after transposing `M`. Hence if either the row-side or column-side fourth-volume law has maximum marginal at most `3/4`, this rank-four branch is continuously paid.

If `rho_*=1` on either side, the same account01/B04 theorem forces `rank(M)=4` and its exact endpoint gives

`||p_Q||inf <=2e E4(M)^(-1/8)`.

Since `E4(M)>=a^8/256`,

`||p_Q||inf <=4e/a
             <(e sqrt(4617)/4) P^(-1/2)
             <46.176 P^(-1/2)`.                                (A.3)

Thus the only rank-four state not removed by this fresh theorem has, on BOTH physical sides,

`3/4 < rho_* < 1`.                                               (A.4)

This is stronger than the main report's generic statement that both rank-four core range projections merely have some leverage greater than `1/2`.

## 3. Heavy physical coordinates remain quantitative

The main report's volume-stability failure still supplies a top-four singular core whose left and right range projections each have a physical leverage greater than `1/2`. Therefore its original literal-row/column lower bounds remain valid:

`||M[u,*]||_2, ||M[*,v]||_2 > sqrt(P/9234)`.

The fresh fourth-volume downshift does not weaken those inequalities; it removes additional diffuse/intermediate-marginal states before the heavy-core receiver is invoked.

For reference, high actual four-volume marginal itself also has a direct row-norm implication. The fourth-volume marginal matrix has spectral weights

`p_j^(4)=lambda_j e3(lambda without j)/E4`,

so

`W4 <= (E3/E4) M M^T`.

Using `T3 E3<=4E4` and `T3>=lambda_4>=a^2/256`, any row with `rho_i>3/4` obeys

`||M[i,*]||_2^2 >= rho_i E4/E3 >3a^2/4096`.

This is a second, fully actual-block certificate independent of the truncated-core leverage estimate.

## 4. Revised remaining rank-four obligation

After this fresh-source application, the rank-four part of the remaining B07 debt is narrower:

`QFORM-STABLE-R4-TWOSIDED-34COLOOP-CONDITIONAL-H3-RECEIVER-v1`:

> consume a perturbatively stable rank-four physical cross core with `s3>16sqrt(P/4617)`, small fifth tail, row and column fourth-volume maxima both strictly between `3/4` and `1`, literal physical row/column norms `>sqrt(P/9234)`, and (in the edge-light branch) the relocated anchored-H3 packet from the main report, while retaining arbitrary same-bank curvature and all remaining spectrum.

The rank-three stable-core survivor and the separate r32 relative-rank-one/rank-two siblings remain distinct obligations.

Full QFORM remains OPEN. Full-target continuity remains OPEN. The new payments (A.2) and (A.3) have continuous densities because their source proofs use integrable Fourier envelopes.
