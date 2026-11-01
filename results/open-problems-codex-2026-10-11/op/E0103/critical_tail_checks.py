from pathlib import Path
import math,json
rows=[]
b=.4
for alpha,A,m in [(1.,1.,2.),(.5,1.,1.5)]:
    for x in [100.,1000.,10000.]:
        s=.2 if alpha==1 else 1.
        t=s*x**alpha
        tiny=math.exp(-x)
        logH=x+math.log1p(-b*tiny)-math.log(t)
        beta=t*A/logH**alpha
        # Exact tail formula in the explicit models, computed without huge L.
        correlations=[]
        for frac in [.1,.01]:
            loga=x+math.log(frac-b*tiny)-math.log(t)
            I=t*A/loga**alpha
            correlations.append({'separation_over_L':frac,
                                 'conditional_common_hit_intensity':I-beta})
        delta=.2 if alpha==1 else .5
        near_log_bound=(delta-1)*x+m*t+b
        rows.append({'alpha':alpha,'log_L':x,'s':s,
                     'spanning_mean':beta,'limit_spanning_mean':A*s,
                     'macroscopic_conditional_correlations':correlations,
                     'log_of_short_pair_bound_up_to_constant':near_log_bound})
out={'explicit_tail_checks_in_log_coordinates':rows,
     'critical_example':{'mean_speed':2.,'rate':1.,'threshold':.5,
                         'mass_at_threshold':math.exp(-.5),
                         'limiting_normalized_mean':1-math.exp(-.5)},
     'note':'These verify closed-form asymptotic quantities, not full coverage samples or a proof.'}
Path('critical_tail_checks.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
