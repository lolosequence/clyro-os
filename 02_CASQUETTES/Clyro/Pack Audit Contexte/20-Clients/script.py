import os
base = "output/Clyro-Audit-Contexte-Vault"
for root, dirs, files in os.walk(base):
    for f in files:
        print(os.path.join(root, f))
