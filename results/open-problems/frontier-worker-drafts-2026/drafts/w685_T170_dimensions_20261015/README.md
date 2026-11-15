# T170 d18/d19 encoded renewal certificates

This research snapshot contains parameter-specific exact/outward certificates for two finite encoded renewal operators. It asserts no independently checked FPP lower bound, no novelty and no additional certified non-ball dimension.

C017-v1 records the binary64 screen. C018-v1 records exact scalar coefficients through400, 2564 rational common-norm inequalities and 330 outward contraction rows per dimension. Rational contraction ceilings are 999936480509838187/10^18 for d19 and 999907618879537695/10^18 for d18. Exact downward floors of sqrt(d)log(z)/s are .077855718601 and .080099928228. Their FPP interpretation remains dependent on the unaudited geometry/automaton and all-length argument.

Run `python -X utf8 scripts/run_renewal_extension.py 19 18` from this directory to rebuild the scalar, norm and interval certificates plus the ratio floors. Python, NumPy and SciPy are required. The Windows scripts use one core, below-normal priority for producers, at least2GB free and an estimated peak below400MB. Every producer exit and required result marker is checked before the next producer starts; checkpoints and per-dimension manifests are saved.

The exact parameter point and arbitrary positive binary64 witness are data, never assumptions about a floating eigenvalue. Every used coefficient is compared with its exact rational value; multiplication/addition use upward nextafter with normal-finite checks. The length>400 scalar remainder uses r<91/100 and an exact geometric tail. Source diffs and their date are saved. The fixed d21 proof and original certificates, preserved unchanged, are in earlier main commit647cf9d076c0eca6151903bf8958a98dbcb218fd at 06_math_research/frontier/worker_drafts/w685_T170_20261015/.

See DIMENSION_EXTENSION_DELIVERY.md and proofs/renewal_dimension_extension.md for exact scope and the unresolved FPP proof review. Repository backup does not confer mathematical approval.
