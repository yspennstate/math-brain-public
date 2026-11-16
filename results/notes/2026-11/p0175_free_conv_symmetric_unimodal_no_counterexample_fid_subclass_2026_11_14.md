---
name: p0175_free_conv_symmetric_unimodal_no_counterexample_fid_subclass_2026_11_14
description: "[PROVISIONAL] P0175 (Hasebe-Ueda 2018 Conj 3.5, symmetric unimodal mu boxplus nu unimodal?): still open; ~5,900 random atom+uniform pairs and an elasticity hill-climb found no counterexample; FID subclass with unimodal free Levy measures follows from Hasebe-Sakuma 2017"
metadata:
  type: project
  created: 2026-11-14
  created_at: 2026-11-14T16:29:27+02:00
  status: provisional
  evidence: ""
---

Status: provisional (numerics, not a proof). Settled subcases: a semicircle factor; symmetric freely ID laws with unimodal free Levy measures, since Hasebe-Sakuma (Ann. IHP 2017, arXiv 1508.01285) prove that a symmetric free Levy process is unimodal iff its free Levy measure is unimodal, and the free Levy measures add under boxplus (read from the abstract only: whether a semicircular part is allowed is not checked). Wintner's mixture-of-uniforms proof fails because boxplus is not affine (P0175-A001 moment check, m6 67 vs 70). Numerics on worker machine 1, 14 Nov: subordination solver for atom plus up to 3 uniforms (fc.py); about 5,900 random pairs with largest relative rise 6e-16 (noise); hill-climb on the elasticity -x f'/f ended at m between 1.6e-9 and 2.1e-7, positive, always by widening one uniform to the clip bound, so it found flat stretches and no bump. Grid resolution about R/2000, at most 3 components. Files: the private repository, 12_cognitive_architecture/math/trio_1011/op/P0175 (NOTE.md, STATUS.md, scripts, outputs). What would change it: a law outside the sampled family (heavy tails, many components) or a fine-scale bump below the grid. Next: read the Hasebe-Sakuma theorem in full; try the route where Im G is decreasing along horizontal lines.
