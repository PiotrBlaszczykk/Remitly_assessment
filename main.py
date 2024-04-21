#Piotr Błaszczyk Remitly Internship 2024

import json


def verify(file_path):

    try:
        with open(file_path, 'r') as file:
            data = json.load(file)

        statements = data.get('PolicyDocument', {}).get('Statement', [])

        for statement in statements:

            resources = statement.get('Resource')
            if resources == '*' or (isinstance(resources, list) and '*' in resources):
                return False


    except json.JSONDecodeError:
        print("Error decoding JSON.")
        return True
    except FileNotFoundError:
        print("File not found.")
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return True

    """
       the task specifies: "Method should return logical false 
       if an input JSON Resource field contains a single asterisk 
       and true in any other case"
       
       So I will take that literally and exceptions will return True
       
    """

    return True


# usage:
path = 'tests/test1.json'
result = verify(path)
print("Policy validation result: ", result)
