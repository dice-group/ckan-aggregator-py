from ckanclient import CkanClient
import os

ckanApiUrl="http://catalog.data.gov/api"
ckanClient = CkanClient(base_location=ckanApiUrl)
cacheFolder=os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../../data/datagov"))