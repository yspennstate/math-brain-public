# account04/B14 handoff — kernel-leakage physical enlargement

Run: `20260923T011517Z-account04-B14-kernel-leakage-core-r6`  
Status: supporting target-level theorem proved; full QFORM remains open.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## Source pins

- Active request: math-research-brain blob `165c570ecb4dcc6299c38fc3298771e4a8339dac`.
- B14 assignment: blob `46b1d3db2ffb7759153a7209cd4cc34071e8c362`.
- Correction inbox: blob `c7000cf3822ae4935a2faf43b89ac92ea65ac0fe`.
- Claude source directory state: math-open-problems `370534c8763da810a1b81945e0e44344feab0b75`.
- New volume-stability continuation: math-open-problems `c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`.
- Completed partner account01/B14 r23: report blob `7908503d72472b58359c14e5011bcd65c0ba6a05`.

## New theorem

Let an actual three-coordinate principal block `B` have rank two, nonzero singular values `nu_1>=nu_2>0), and unit kernel vector `k`. Add one actual coordinate `j`, write `c=A[S,j]`, and let

`H=[[B,c],[c^T,A_jj]]`.

Then

`|det H|=nu_1 nu_2 |k^T c|^2`

and

`s_3(H)>=|k^Tc|sqrt(nu_1nu_2)/sqrt(s_1(H)s_2(H))`.

Combining this with the fixed four-dimensional affine theorem, account01/B14's rough-product transfer, and outside original-coordinate conditioning proves

`||p_(X^TAX)||inf
 <=1000(8+log4)sqrt(s_1(H)s_2(H))
   /(|k^Tc|sqrt(nu_1nu_2))`.

This absorbs genuine kernel leakage by pulling one leaking original coordinate into the physical core. It does not rotate random variables, bound supports, or discard the kernel term.

## Actual partner applications

1. account01/B14's smooth-to-rough interval transfer is used to pass the affine fixed-core inequality to arbitrary cap-one product laws with no localization loss.
2. Its outside-lifted top-two-cross theorem yields
   `||p_Q||inf<=e sqrt(pi)/sqrt(s_1(C)s_2(C))`
   whenever an actual zero-self bank and rank-two cross block exist, with arbitrary outside completion.

The current volume-stability theorem also supplies `||p_Q||inf<23/a` on its near-diffuse cross-block branch.

## Exact remaining gap

The global hypothesis `s_3(A)>=1` need not force any single leakage coordinate to make

`|k^Tc|sqrt(nu_1nu_2)/sqrt(s_1(H)s_2(H))`

uniformly positive. The remaining localization obligation is collective: aggregate many small kernel couplings into a product-preserving cross/volume certificate. The convex/two-sheet contribution also remains open outside protected full-core branches.

Canonical mathematics: math-open-problems commit `6442bbe9d4647a730b27b8e0786bc54b2546b7ec`, report blob `9fc59e23773dd6e3973923c0b4cea033be16ed25`.
