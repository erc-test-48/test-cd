
import re
import sys
import json
import os

def generate_files(checklist_status, modified_files, pr_url):
    for file in modified_files:
        match = re.match(r'(.*/)(\w+)\.(\w+)\.json$', file)
        if match:
            file_path, file_id, file_type = match.groups()
            for title, status in checklist_status.items():
                if file_type.lower() in title.lower():
                    review_content = {
                        "pull_request": pr_url,
                    }
                    review_filename = os.path.join(file_path, f"{file_id}.json")
                    with open(review_filename, 'w', encoding='utf-8') as review_file:
                        json.dump(review_content, review_file, indent=4)
                    print(f"Generated: {review_filename}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python generate_files.py '<checklist_status_json>' '<modified_files>' '<pr_url>'")
    else:
        checklist_status = json.loads(sys.argv[1])
        generate_files(checklist_status, sys.argv[2].split(), sys.argv[3])
