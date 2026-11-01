import urllib.request, urllib.parse, pathlib, xml.etree.ElementTree as E, json
root=pathlib.Path(__file__).resolve().parent
q='(all:"disorder chaos" OR all:"noise sensitivity" OR all:superconcentration) AND (all:polymer OR all:"last passage")'
url='https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':q,'max_results':15})
try:
 data=urllib.request.urlopen(url,timeout=40).read()
 (root/'targeted_search.xml').write_bytes(data)
 ns={'a':'http://www.w3.org/2005/Atom'}
 print('\n\n'.join(e.find('a:id',ns).text+' '+e.find('a:title',ns).text+'\n'+e.find('a:summary',ns).text for e in E.fromstring(data).findall('a:entry',ns)))
 result={'url':url,'status':'success'}
except Exception as e:
 result={'url':url,'status':'error','error':str(e)}; print(result)
(root/'targeted_search_log.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
