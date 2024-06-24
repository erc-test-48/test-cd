import re
import sys
import json

def parse_markdown(content):
    # checklists = re.findall(r'(^#+\s.*$|^- \[.\].*$)', content, re.MULTILINE)
    checklists = re.findall(r'(^#+\s.*$|^\s*- \[.\].*$)', content, re.MULTILINE)
    
    result = {}
    current_title = None
    current_checklist = []
    
    for line in checklists:
        if line.startswith('#'):
            if current_title and current_checklist:
                result[current_title] = all('x' in item for item in current_checklist)
            current_title = line.strip('# ').strip()
            current_checklist = []
        else:
            current_checklist.append(line)
    
    if current_title:
        result[current_title] = all('x' in item for item in current_checklist)

    print(json.dumps(result))
    
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python parse_checklist.py '<markdown_content>'")
    else:
        parse_markdown(sys.argv[1])