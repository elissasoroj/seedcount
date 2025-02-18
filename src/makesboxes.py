"""Notes from Elissa ~
Generate the code for the checkboxes - it's the best fix I could come up with. 
Perhaps Deren or another student can help you organize this better or somehow get the 
program itself to generate and insert the code into streamlit.py app, but until then, 
	this at least gives you something to work with
	"""

import pandas as pd

#read in the dataframe
DATA = pd.read_csv("SEEDS.csv",
                   header=0,
                   index_col=False,
                   names=['seeds_per_lb', 'seeds_per_oz', 'species', 'nan', 'altname', 
                          'common_name', 'ecotypes', 'germ_protocol', 'forb', 'fall', 'germ_rate',
                          'a', 'm', 'j', 'j2', 'a2', 's', 'o'])

#save species as a list
splist_raw = DATA["species"].tolist()

#create empty list to store
SPLIST = [] 

#remove duplicate species names
for i in splist_raw: 
    if i not in SPLIST: 
        SPLIST.append(i) 

#run this code to create the checkboxes.txt file
if __name__ == "__main__" :
	boxes = open('checkboxes.txt', "w")
	for sp in SPLIST:
	    boxes.write(f"{''.join(sp.split()).lower().replace('-', '').replace('.', '')} = st.checkbox('{sp}')\n"
	                f"if {''.join(sp.split()).lower().replace('-', '').replace('.', '')}:\n"
	                f"\tusrchoices.append('{sp}')\n"
	                )
