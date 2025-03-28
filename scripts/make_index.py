#! /usr/bin/env python3

import os
import json
import yaml


def main():
    agents_data = []
    data_dir = "index-data"

    # Check if the directory exists
    if not os.path.isdir(data_dir):
        print(f"Error: Directory '{data_dir}' not found")
        return

    # Iterate through all files in the directory
    for filename in os.listdir(data_dir):
        if filename.endswith(".yml") or filename.endswith(".yaml"):
            file_path = os.path.join(data_dir, filename)
            try:
                with open(file_path, "r") as file:
                    # Load YAML content
                    agent_data = yaml.safe_load(file)
                    agents_data.append(agent_data)
            except Exception as e:
                print(f"Error processing {filename}: {str(e)}")

    # Print the array as JSON to stdout
    print(json.dumps(agents_data))


if __name__ == "__main__":
    main()
