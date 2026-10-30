# Threshold reduction analysis — fleet01/B16 — 20260924T130832Z-r11

Source pin: baseline commit `7c0d6e60946b19423e6400a12d34b473cf0591e2`, manuscript blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

## Result of this run

No complete theorem lowering 17 while preserving all hypotheses was proved. In particular I do **not** claim a 16-, 13-, 9-, or 3-eigenvalue replacement.

I did isolate exactly why the current proof cannot be lowered by retuning constants.

## The rank-count bottleneck is structural

At the bad volume ratio of order `r`, Lemma `lem:completion` gives

- `rank R <= 3r`,
- `rank R[L,L] <= r`,
- `D=0` on the `2r` seed coordinates.

If `s_m(A)>=1` and `||E||<=epsilon`, rank perturbation forces at least `m-3r` diagonal entries of `D` to have modulus at least `1-epsilon`. To contradict the restricted rank bound by diagonal dominance, the proof needs **r+1** such indices in `L`. Therefore

`m-3r >= r+1`, i.e. `m >= 4r+1`.

For the order-five density step the worst possible ratio is `r=4`, so this exact mechanism requires `m>=17`.

## Sharpness of the rank bookkeeping

The rank inequalities themselves can saturate. For `r=1`, take

```text
A = [ -2  -1  -6  -9
      -1   0   1   1
      -6   1  -8  -1
      -9   1  -1   2 ]
```

with seed `S={1}`, `T={2}` in one-based indexing. The manuscript construction gives

```text
P = [ -2 -1 -6 -9
       0  0  0  0
       2  1  6  9
       2  1  6  9 ],

D = diag(0,0,-14,-7),

E = [0 0  0   0
     0 0  0   0
     0 0  0 -10
     0 0 -7   0],

R = [ -2 -1 -6 -9
      -1  0  1  1
      -6  1  6  9
      -9  1  6  9].
```

Exact ranks are

`rank P=1`, `rank R=3=3r`, `rank R[L,L]=1=r`, and `rank(D+R)=4=4r`.

This is not a counterexample to the theorem (it is not normalized to the no-pivot numerical regime); it is a counterexample to any attempted improvement that uses only the displayed rank inequalities. Thus replacing 17 by 16 requires genuinely new information beyond the current rank count.

## The analytic endpoint at order four

The determinant theorem plus order-`k` crossing volume gives

`|phi_Q(t)| <= min(1,(u_k/|t|)^(k/4))`.

At `k=4` the exponent is exactly one. Absolute Fourier inversion then has the logarithmically divergent majorant `C/|t|`. Therefore the current no-pivot analytic step cannot turn the `s_13 -> V_4` structural conclusion into a uniform density bound.

A true reduction below 17 must supply at least one of:

1. an endpoint order-four density theorem that avoids absolute `L^1` Fourier inversion;
2. a stronger decoupling/BL determinant exponent in the rough product-law setting;
3. a new structural dichotomy that turns the saturated `r=4` interpolation case into a pivot or another already bounded branch;
4. a different product-preserving nonlinear integration argument.

Changing `eta`, `kappa`, or numerical constants alone cannot cross either the `m=4r+1` rank threshold or the `k/4=1` Fourier endpoint.

## Status

- Baseline 17 theorem: independently audited PASS by this worker.
- Lower threshold proved this run: **none**.
- 16-eigenvalue theorem: **OPEN / UNCHECKED**, not refuted.
- 13-eigenvalue theorem: **OPEN / UNCHECKED**, current order-four absolute-Fourier route insufficient.
- Full three-eigenvalue theorem: **OPEN / UNCHECKED**.
