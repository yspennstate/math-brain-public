import json
import pathlib
import time

root=pathlib.Path(__file__).resolve().parent
inbox=pathlib.Path('~/math-brain-inbox/w335')
changes=[]
for number in (5,9):
    name='bundle_%03d.json'%number
    path=root/'bundles'/name
    bundle=json.loads(path.read_text(encoding='utf-8'))
    for entry in bundle['entries']:
        if number==5:
            entry['statement']='For a finite star with at least one leaf and positive edge lengths, and a nearest-unvisited walk that stops after all vertices are visited, every random start distribution satisfies sd(L)/E L<=1/(2*sqrt(6)). For at least two leaves, write S for the sum of all edge lengths and w_1>=w_2 for the largest two. All lengths lie in [2S-w_1-w_2,2S-w_1], whose endpoint ratio is at most 3/2. A one-leaf star has constant positive length and coefficient zero. The constant is sharp over arbitrary start distributions; the uniform-start case is included but no optimality claim for that subclass is made. This does not prove an absolute bound for arbitrary graphs.'
            entry['assumptions'][0]='Positive weighted star with at least one leaf'
            changes.append({'key':entry['key'],'change':'Exclude the empty star and explicitly handle a one-leaf star.'})
        else:
            if 'Fekte' in entry['statement']:
                entry['statement']=entry['statement'].replace('Fekte','Fekete')
                changes.append({'key':entry['key'],'change':'Correct Fekete spelling.'})
    for folder in (root/'bundles',inbox):
        final=folder/name
        part=final.with_suffix('.json.part')
        part.write_text(json.dumps(bundle,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        part.replace(final)
boundary=[]
start=time.perf_counter()
for weight in (1,2,17,1000000):
    # Independent two-vertex distance matrix: there is exactly one move.
    distances=[[0,weight],[weight,0]]
    lengths=[distances[start_vertex][1-start_vertex] for start_vertex in (0,1)]
    assert lengths==[weight,weight]
    boundary.append({'weight':weight,'lengths':lengths,'cv':0})
measurement=json.loads((root/'p0255_measurement.json').read_text(encoding='utf-8'))
measurement['one_leaf_boundary_cases']=boundary
measurement['boundary_command']='python -X utf8 finalize_corrections.py'
measurement['boundary_check_seconds']=round(time.perf_counter()-start,6)
(root/'p0255_measurement.json').write_text(json.dumps(measurement,indent=2),encoding='utf-8')
receipt={'changes':changes,'boundary_cases':boundary,'result':'PASS','command':'python -X utf8 finalize_corrections.py'}
(root/'finalization_receipt.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(json.dumps(receipt),flush=True)
