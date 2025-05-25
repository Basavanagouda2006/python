print('NAME:Basavanagouda.y' ,'USN:1AY24AI017') 
#table printer.py 
def print_table(table_data): 
    #find the maximum width of each column 
    col_widths=[max(len(str(item)) 
for item in col) for col in zip(*table_data)] 
    #print each row in aligned columns 
    for row in table_data: 
        for i,item in enumerate(row): 
           print(str(item).rjust(col_widths[i]), end='  ') 
        print() 
table=[ 
     ["name",  "age", "city"], 
     ["alice",  30,   "new york"], 
     ["bob",    25,    "los angels"], 
     ["charlie", 35,  "chicago"] 
] 
print_table(table) 