import pandas as pd
from lodstorage.sparql import SPARQL
from lodstorage.csv import CSV
import ssl
from urllib.request import urlopen
import json

ssl._create_default_https_context = ssl._create_unverified_context

sparqlQuery = """PREFIX purl: <http://purl.org/dc/terms/>
PREFIX cidoc: <http://www.cidoc-crm.org/cidoc-crm/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

SELECT DISTINCT ?priref ?beeld ?label
WHERE {
   SELECT ?versie ?priref ?beeld ?label FROM <http://stad.gent/ldes/industriemuseum>
   WHERE { 

     ?versie purl:isVersionOf ?priref.
     ?versie cidoc:P129i_is_subject_of ?beeld.
     ?versie cidoc:P41i_was_classified_by ?identifier.
     ?identifier cidoc:P42_assigned ?objectnaam.
     ?objectnaam skos:prefLabel ?label
     FILTER (regex(?label, "^porseleinkaart$", "i"))

   } 
}"""

sparql = SPARQL("https://stad.gent/sparql")
qlod = sparql.queryAsListOfDicts(sparqlQuery)
csv = CSV.toCSV(qlod)
df_porseleinkaarten = pd.DataFrame([x.split(',') for x in csv.split('\n')])
df_porseleinkaarten[1] = df_porseleinkaarten[1].str.replace(r'"', '')

iiifmanifesten = df_porseleinkaarten[1].tolist()
iiifmanifesten.remove('beeld')

for manifest in iiifmanifesten:
    response = urlopen(manifest)
    data_json = json.loads(response.read())
    iiif_manifest = data_json["sequences"][0]['canvases'][0]["images"][0]["resource"]["@id"]
    print(iiif_manifest)