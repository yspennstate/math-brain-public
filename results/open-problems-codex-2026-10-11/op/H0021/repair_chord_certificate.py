import pathlib,json
r=json.loads(pathlib.Path('second_experiment_results.json').read_text(encoding='utf8'));pairs=r['lean_certificate']['packed_pairs']
lit=',\n  '.join('{'+', '.join(f'({u}, {v})' for u,v in pp)+'}' for pp in pairs)
s='import Mathlib.Data.Finset.Card\n\n'
s+='def chordPacking : Finset (Finset (ℕ × ℕ)) := {\n  '+lit+'}\n\n'
s+='def chordPackingList : List (Finset (ℕ × ℕ)) := [\n  '+lit+']\n\n'
s+=f'theorem chordPacking_size : chordPacking.card = {len(pairs)} := by decide +kernel\n'
s+='theorem chordPacking_disjoint : chordPackingList.Pairwise (fun A B => Disjoint A B) := by decide +kernel\n'
s+='theorem chordPacking_list_finset : chordPackingList.toFinset = chordPacking := by decide +kernel\n'
s+='#print axioms chordPacking_size\n#print axioms chordPacking_disjoint\n#print axioms chordPacking_list_finset\n'
pathlib.Path('ChordCertificate.lean').write_text(s,encoding='utf8')
