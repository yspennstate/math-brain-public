import literature_search as s
import urllib.parse as u
queries={
 'arxiv_specific':'https://export.arxiv.org/api/query?search_query='+u.quote('all:condensation AND all:scaling')+'&max_results=50',
 'arxiv_dendron':'https://export.arxiv.org/api/query?search_query='+u.quote('all:dendron OR (au:Janson AND all:limits AND all:trees)')+'&max_results=30',
 'crossref_tree_limits':'https://api.crossref.org/works?query='+u.quote('Janson tree limits condensation dendrons')+'&rows=15',
 'openalex_retry':'https://api.openalex.org/works?search=condensation%20Galton%20Watson&per_page=20',
 'semantic_source':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:1112.0510?fields=title,citations.title,citations.year,citations.externalIds',
}
if __name__=='__main__':
 import concurrent.futures
 with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
  for result in pool.map(s.get,queries.items()): print(result,flush=True)
