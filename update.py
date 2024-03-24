import os
import json

def update_json():
    files = os.listdir("sounds")
    data={str(i+1): "sounds/"+file for i, file in enumerate(files)}
    with open("audio.json",'w') as f:
        json.dump(data,f,indent=4)
        
update_json()
    