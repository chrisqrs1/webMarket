# https://qrs1216-my.sharepoint.com/:u:/g/personal/christophe_edlinger_qrs1_fr/EWYJEm0lAMdIlmcyp5HjIssBvwvXxHzcHAGhk53gGwUNVw?e=LarS5g

import os
import requests

file_id = "EWYJEm0lAMdIlmcyp5HjIssBvwvXxHzcHAGhk53gGwUNVw"

ApplicationClientID = "032f9021-9dad-49df-8c4a-748426176605"
DirectoryTenantID   = "0752ba58-a585-45d6-8bee-878a5c749415"
ClientSecretID = "DaO8Q~U1qhJDuu9PjD.3gpNfWGzoX8G278dxfbT2"


from microsoftgraph.client import Client
client = Client('CLIENT_ID', 'CLIENT_SECRET', account_type='common') # by default common, thus account_type is optional parameter.


