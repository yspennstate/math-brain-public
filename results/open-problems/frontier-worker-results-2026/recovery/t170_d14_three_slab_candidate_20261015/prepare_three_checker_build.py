from pathlib import Path
H=Path(__file__).resolve().parent
s=(H/'build_t067_independent_fusion.py').read_text(encoding='utf-8').replace('T067_INDEPENDENT_FUSION','T170_THREE_CONSTRUCTIVE_CHECK').replace('t067_independent_fusion','check_three_compressed')
p=H/'build_three_checker.py';assert not p.exists();p.write_text(s,encoding='utf-8')
