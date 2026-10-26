ViT-Base singular value spectra, measured 2026-09-16
checkpoint: timm vit_base_patch16_224.augreg2_in21k_ft_in1k (model.safetensors, 346,284,714 bytes)
method: numpy.linalg.svd on the float64 weight matrix, no normalisation
MP edge: sigma * sqrt(max_dim) * (1 +- sqrt(gamma)), gamma = min_dim/max_dim, sigma = the matrix's own entry std

CONTROL, iid Gaussian matrices of the same shapes: 0 of 768 above the predicted edge in all three,
and the smallest singular value lands on the lower edge to three decimals. The formula is not flattering.

layer                          shape          gamma   edge hi    max sv above edge
blocks.0.mlp.fc1.weight        3072x768       0.250     1.685     6.778     67 /768
blocks.6.mlp.fc1.weight        3072x768       0.250     1.790     3.439     78 /768
blocks.11.mlp.fc1.weight       3072x768       0.250     2.250     5.080     36 /768
blocks.6.attn.qkv.weight       2304x768       0.333     1.726     3.090     78 /768
blocks.11.attn.proj.weight     768x768        1.000     1.525     3.932      2 /768
