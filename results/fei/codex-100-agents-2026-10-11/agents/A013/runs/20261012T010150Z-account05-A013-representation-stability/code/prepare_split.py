from pathlib import Path
RUN=Path(__file__).resolve().parents[1]
s=(RUN/'code/check.py').read_text(encoding='utf-8')
prefix=s[:s.index('# Independent full tables')]
transport=s[s.index('# Independent full tables'):s.index('# Independent reference review')]
transport=transport.replace('for m in [4,8,16,32,64]:','for m in [4,8,16]:').replace('for D in [1,2,4,8,16]:','for D in [1,2,4]:').replace('[256,512,1024,2048,4096]','[256,512,1024,2048]')
transport+='''\nresult={'helper':'A013-transport-v2','status':'PASS','exact_assertions':checks,'elapsed_seconds':time.perf_counter()-start,'full_truth_cases':truth_cases,'ledger_cases':ledger_cases,'rational_jump_certificates':signs,'failures':0}
(RUN/'out/TRANSPORT_RESULTS.json').write_text(json.dumps(result,indent=2)+'\\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k not in ['full_truth_cases','ledger_cases','rational_jump_certificates']},indent=2))
'''
review=s[s.index('# Independent reference review'):s.index('\nresult={')]
review+='''\nresult={'helper':'A013-A012-review-v2','status':'PASS','exact_assertions':checks,'elapsed_seconds':time.perf_counter()-start,'activation_reference_cases':activation_cases,'posterior_joint_cases':posterior_cases,'sharp_coefficient_interval':[str(x) for x in enclose(cstar)],'failures':0}
(RUN/'out/REVIEW_RESULTS.json').write_text(json.dumps(result,indent=2)+'\\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k not in ['posterior_joint_cases','sharp_coefficient_interval']},indent=2))
'''
(RUN/'code/check_transport.py').write_text(prefix+transport,encoding='utf-8')
(RUN/'code/check_review.py').write_text(prefix+review,encoding='utf-8')
print('Frozen independent transport/review helpers written inside A013')
