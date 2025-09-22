import os
# Using os.walk()
for dirpath, dirs, files in os.walk('src/CompanyDocuments/invoices'): 
  for filename in files:
    fname = os.path.join(dirpath,filename)
    if fname.endswith('.pdf'):
      print(fname)