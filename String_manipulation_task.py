
'''
smart_print prints keys and values of the target dictionary
with a specific number of dots and spaces in between.
dict: target dictionary
dot: number of dots
space: number of spaces
'''
def smart_print(dict, left, right):
   print("\n"+"PICNIC ITEMS".center(left+right+1, "-"))
   #check for existance of dict
   try:
     for key in dict.keys():
       value = dict[key]
       print(f"\n {key}"+"."*(left-len(key))+" "*(right-len(str(value)))+f"{value}")    
   except:
     print("Cross-check target dictionary")

#target dictionary
picnicitems = {'sandwiches':4,'apples':12,'cups':4,'cookies':8000}

#Get output
smart_print(picnicitems, left=12, right=5)
smart_print(picnicitems, left=20, right=6)