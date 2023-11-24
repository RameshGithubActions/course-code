import yaml
import json

# Read YAML file
with open('input.yaml', 'r') as yaml_file:
    yaml_data = yaml.safe_load(yaml_file)
    
# Convert YAML to JSON
json_data = json.dumps(yaml_data, indent = 2)

# Write JSON to output file
with open('output.json', 'w') as json_file:
    json_file.write(json_data)

