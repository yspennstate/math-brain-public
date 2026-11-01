# HARD8-05 verification addendum — maximal exponent-two portal checkpoint

This is an append-only companion to:

`hard8_2026-09-16/HARD8-05/runs/2026-09-16/2026-09-16T08-36-00Z__report.md`

## 1. Publication receipts

### Mathematical report

Path:

`hard8_2026-09-16/HARD8-05/runs/2026-09-16/2026-09-16T08-36-00Z__report.md`

Creation commit:

`1337102227c9815d0d3dd8d8007995a1e6c851af`

The file was fetched back by exact raw URL at this commit and its contents were inspected. Status:

**VERIFIED BY READBACK.**

### Exact verifier artifact

Path:

`hard8_2026-09-16/HARD8-05/artifacts/2026-09-16T08-36-00Z__exponent2_portal_verifier.py`

Creation commit:

`f3b10501879abc163316ec9a2b6644d157fd39af`

The file was fetched back by exact raw URL at this commit and its contents were inspected. Status:

**VERIFIED BY READBACK.**

## 2. Actual execution record

The verifier was executed in the bounded run before publication, using the same source text that was archived. It completed successfully with the following exact output:

```text
abstract exponent-two group checks: OK
Xu hard-class count: 7185
Xu nine-portal union: 7150
Xu nine-portal misses: 35
extended hard-class count: 37716
portal counts: {(1, 1): 19162, (1, 2): 23032, (2, 1): 23390, (1, 3): 16637, (3, 1): 17314, (1, 6): 11552, (6, 1): 12715, (2, 3): 11307, (3, 2): 11458}
extended nine-portal union: 37594
extended nine-portal misses: 122
minimal-u distribution on misses: {4: 41, 5: 35, 7: 5, 8: 11, 9: 8, 10: 4, 11: 3, 12: 3, 13: 1, 14: 3, 17: 2, 18: 2, 20: 1, 37: 2, 91: 1}
maximal observed minimal-u certificate: (2369929, 91, 727)
ALL CHECKS PASSED
```

The verifier checks, using only exact integer arithmetic and the Python standard library:

1. the exponent-two unit-group sanity classification for multiples of four in a finite range;
2. exhaustive support-subgroup classifications modulo 8, 12, and 24;
3. direct divisor search versus the closed nine-portal criteria for every prime `n≡1 (mod24)` through `720001`;
4. reciprocal gcd and Bezout identities;
5. exact nine-portal finite coverage through `4,300,000`;
6. the complete fixed-`a=1` Type-II search for every one of the 122 nine-portal misses, using the proved finite `u` bound;
7. the stated minimal-`u` distribution and the exact `(n,u,s)=(2369929,91,727)` witness;
8. the branch-forcing consequences used in the report.

No floating point, randomized solver, timeout inference, or approximate equality is used.

## 3. Scope warning

These checks verify the finite computations and internal algebra supporting the checkpoint. They are **not** an independent proof of the Erdős–Straus conjecture, and they do not turn the finite coverage into an asymptotic statement. The full conjecture remains open.
