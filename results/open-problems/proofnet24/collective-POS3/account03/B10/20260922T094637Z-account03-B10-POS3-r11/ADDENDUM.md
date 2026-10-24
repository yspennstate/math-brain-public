# Addendum — sign-completeness and regression for the same-sign packet theorem

This addendum completes one sign case implicit in `REPORT.md` Theorem 5.1 and records an independent finite regression of the exact corridor identity. It does not change the parent status.

## 1. Why “same-sign” reduces to the positive-sign case

In the report, the pair is oriented by its actual strong majority `a prec_* b`, and Lemma 4.1 is proved when every relation distinguisher has the positive sign for `a<b`.

Suppose instead that an exact-two same-sign pair had both distinguishers negative for this orientation. Reverse the labels in Lemma 4.1: relative to the orientation `b<a`, those same distinguishers are all positive. The reversed safe-corridor identity would then read

`Pr(S_rev)=2 Pr(a<b)`.

But `a prec_* b` gives `Pr(a<b)>2/3`, hence the right side is `>4/3`, impossible for an event probability. Therefore an exact-two same-sign pair compatible with the actual strong-majority orientation cannot have the negative sign. The only surviving same-sign case is exactly the positive case proved in Sections 4-5 of the report.

Thus Theorem 5.1 as stated is sign-complete: absent an already accepted strict subspan exit, every exact-two same-sign pair carries actual minority probability `>1/6`.

## 2. Independent exact regression of Lemma 4.1

`verify_same_sign_corridor.py` independently enumerates every distinct naturally labelled transitive closure through six vertices, every incomparable pair whose full relation-distinguisher set is nonempty and all-positive for the displayed orientation, and every full linear extension. It checks the integer identity

`N(S)=2 N(b<a)`

with no floating-point arithmetic.

Recorded output:

```text
n=2 posets=2 all_positive_identity_cases=0
n=3 posets=7 all_positive_identity_cases=4
n=4 posets=40 all_positive_identity_cases=61
n=5 posets=357 all_positive_identity_cases=985
n=6 posets=4824 all_positive_identity_cases=20346
total_identity_cases=21396
POS3_SAME_SIGN_CORRIDOR_CHECK_PASS
```

The enumeration is regression evidence only. The arbitrary-size proof remains the involution in REPORT.md Lemma 4.1.
