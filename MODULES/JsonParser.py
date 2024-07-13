import json

class Json_parser:
    def readJson(self, file_name, outer_key, inner_key, target_key):
        data = self.load_json(file_name)

        if data == None: return
        
        return data[outer_key][inner_key][target_key]
    
    def load_json(self, file_name):
        try:
            with open(file_name, 'r') as file:
                return json.load(file)
        except FileNotFoundError:    return None
        except json.JSONDecodeError: return None
        except Exception:            return None
    
    def save_json(self,file_name, data):
        try:
            with open(file_name, 'w') as file:
                json.dump(data, file, indent=4)
        except Exception as e: print(f"Failed to save json ERROR: {e}")
    
    def updateJson(self, file_name, outer_key, inner_key, target_key, value):
        data = self.load_json(file_name)

        if data == None: return
        
        if outer_key in data and inner_key in data[outer_key] and target_key in data[outer_key][inner_key]:
            data[outer_key][inner_key][target_key] = value
        else:
            print(f"Keys {outer_key} or {inner_key} or {target_key} not found in the JSON structure.")
            return
        
        self.save_json(file_name, data)
