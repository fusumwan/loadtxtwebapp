import json
import re
from datetime import datetime
from json import JSONDecodeError
import json
import uuid

class JsonUtil:
    @staticmethod
    def to_json(arg0):
        # Check if arg0 has a toJson method
        if hasattr(arg0, 'to_json') and callable(getattr(arg0, 'to_json')):
            # Call the to_json method and return its result
            return arg0.to_json()
        elif isinstance(arg0, list):  # Check if arg0 is a list
            # Process each item in the list recursively and collect JSON strings
            list_json_str = [JsonUtil.to_json(item) for item in arg0]
            # Combine individual JSON strings into a single array JSON string
            return '[' + ', '.join(list_json_str) + ']'
        else:
            # Handle serialization for other types of objects
            try:
                # Custom handler for objects that json.dumps can't serialize directly
                def default_handler(o):
                    if isinstance(o, datetime):
                        return o.isoformat()
                    elif isinstance(o, uuid.UUID):
                        return str(o)
                    raise TypeError(f"Object of type {o.__class__.__name__} is not JSON serializable")
                
                return json.dumps(arg0, default=default_handler)
            except (TypeError, OverflowError) as e:
                print(e)
                return None


    @staticmethod
    def ToJSONObject(json_str):
        try:
            # Direct conversion of JSON string to Python dictionary
            return json.loads(json_str)
        except JSONDecodeError as e:
            print(e)
            return None

    @staticmethod
    def extractJson(input_str):
        pattern = r"\{.*?\}"  # Regex to match JSON objects
        match = re.search(pattern, input_str, re.DOTALL)
        if match:
            return match.group(0)
        return "No JSON found"

    @staticmethod
    def IsValidDataType(json_object, key, data_type):
        try:
            value = json_object[key]
            if data_type == "String" and isinstance(value, str):
                return True
            elif data_type == "Integer" and isinstance(value, int):
                return True
            elif data_type == "Boolean" and isinstance(value, bool):
                return True
            elif data_type == "Double" and isinstance(value, float):
                return True
            elif data_type == "Long" and isinstance(value, int):  # Python does not distinguish between Long/Int
                return True
            elif data_type == "JSONArray" and isinstance(value, list):
                return True
            elif data_type == "JSONObject" and isinstance(value, dict):
                return True
            elif data_type == "Null" and value is None:
                return True
        except KeyError:
            pass
        return False
    
    @staticmethod
    def adjustJsonValue(value):
        """
        Adjusts the given value to ensure it is properly formatted for JSON serialization.
        This method handles different types of values and ensures special characters
        are correctly represented.
        """
        if isinstance(value, str):
            # Replace or escape special characters as needed, for example:
            # return value.replace('"', '\\"').replace('\n', '\\n')
            # For simplicity, just return the value in this example
            return value
        elif value is None:
            return ''
        # Add more conditions as necessary for different types
        else:
            return str(value)
        
    @staticmethod
    def set_properties(json_dict, property_name, value):
        """
        Add or update a property and its value in a JSON dictionary.

        Parameters:
        - json_dict (dict): The JSON dictionary to modify.
        - property_name (str): The name of the property to add or update.
        - value: The value to set for the given property.

        Returns:
        - dict: The updated JSON dictionary with the new or updated property.
        """
        # Update the dictionary with the new property and value
        json_dict[property_name] = value

        # Return the updated dictionary
        return json_dict

