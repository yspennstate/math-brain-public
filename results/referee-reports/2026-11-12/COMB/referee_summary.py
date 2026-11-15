"""Render the independent numerical outputs without fitting asymptotic laws."""
import json
import math

with open("numerical_checks.json") as f:
    d=json.load(f)
out=[]
out.append("Independent numerical summaries (natural logarithms).\n")
out.append("Long walks: six profiles, one independent pair per profile.\n")
out.append("regime t mean_all mean_backbone all_by_profile backbone_by_profile")
for r in d["long_run_summary"]:
    out.append(f'{r["regime"]} {r["time"]} {r["mean_all"]:.6f} {r["mean_backbone"]:.6f} {r["all_by_profile"]} {r["backbone_by_profile"]}')
out.append("\nMonte Carlo moments, pooled equally across six profiles:")
out.append("N mean second second/mean^2 (second/mean^2)/logN mean_quenched_ratio Ppositive")
for r in d["sampled_moment_summary"]:
    out.append(f'{r["N"]} {r["mean"]:.6f} {r["second"]:.6f} {r["pooled_ratio"]:.6f} {r["pooled_ratio_over_logN"]:.6f} {r["mean_quenched_ratio"]:.6f} {r["probability_positive"]:.6f}')
out.append("\nDeterministic kernel moments, pooled equally across six profiles:")
out.append("N mean second second/mean^2 (second/mean^2)/logN mean_quenched_ratio")
for N in (4,8,16):
    rows=[r for r in d["deterministic_moments"] if r["N"]==N]
    a=sum(r["mean"] for r in rows)/len(rows)
    b=sum(r["second"] for r in rows)/len(rows)
    q=sum(r["second_over_mean_squared"] for r in rows)/len(rows)
    out.append(f'{N} {a:.6f} {b:.6f} {b/a**2:.6f} {b/(a**2*math.log(N)):.6f} {q:.6f}')
out.append("\nPer-profile deterministic ratios second/mean^2:")
for p in range(6):
    out.append(f'{p}: '+" ".join(f'{r["N"]}:{r["second_over_mean_squared"]:.6f}' for r in d["deterministic_moments"] if r["profile"]==p))
out.append(f'\nDeterministic-kernel runtime: {d["elapsed_seconds"]:.6f} seconds.')
text="\n".join(out)+"\n"
with open("CHECK_OUTPUTS.txt","w") as f:
    f.write(text)
print(text)
