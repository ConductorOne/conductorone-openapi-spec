import yaml
from deepdiff import DeepDiff
import os

# --- Sort Changes ---
NODE_BLACKLIST = ['description']
def classify_change(change_path, change_type, buckets):
    node = change_path.split('[')[-1][1:-2]
    object_changed = ''
    if change_path.startswith("root['components']['schemas']"):
        object_changed = 'schemas'
    elif change_path.startswith("root['paths']"):
        object_changed = 'endpoints'
    else:
        raise ValueError("This case is not handled" + change_path)
    
    # Ignore changes in certain leaves
    if node in NODE_BLACKLIST:
        return

    # Check if the change occured on a schema [should only happens when a schema is added/deleted]
    if node.startswith('c1.api'):
        # Ensure there are no more [] after the matching pattern (i.e. its not an attribute of a schema being changed)
        if change_path.count('[') == 3 and change_type in ['added', 'deleted'] and object_changed == 'schemas':
            buckets[change_type][object_changed].append(node)
            return
        raise ValueError("This case is not handled" + change_path)
    
    # If the leaf starts with '/api/' it means an endpoint was added/deleted
    if node.startswith('/api/'):
        # Ensure there are no more [] after the matching pattern (i.e. its not an attribute of a schema being changed)
        if change_path.count('[') == 2 and change_type in ['added', 'deleted'] and object_changed == 'endpoints':
            buckets[change_type][object_changed].append(node)
            return
        raise ValueError("This case is not handled" + change_path)

def extract_changes(diff):
    buckets = {
        'added': {'schemas': [], 'endpoints': []},
        'deleted': {'schemas': [], 'endpoints': []},
        'changed': {'schemas': [], 'endpoints': []},
    }

    # Extract added items
    for item in diff.get('dictionary_item_added', []):
        classify_change(item, 'added', buckets)

    # Extract deleted items
    for item in diff.get('dictionary_item_removed', []):
        classify_change(item, 'deleted', buckets)

    # Extract changed items
    for item in diff.get('values_changed', []):
        classify_change(item, 'changed', buckets)

    return buckets

# --- Release notes generators ---
def _generate_schemas_notes(schemas, spec):
    notes = ""
    for schema in schemas:
        schema_details = spec['components']['schemas'].get(schema, {})
        title = schema_details.get('title', schema.split('.')[-1]) # Extract last part if title is missing
        description = schema_details.get('description', '')
        notes += f"- {title}: {description}\n" if description else f"- {title}\n"
    return notes

def generate_added_schemas_notes(added_schemas, current_spec):
    return "#### Schemas:\n" + _generate_schemas_notes(added_schemas, current_spec)

def generate_deleted_schemas_notes(deleted_schemas, previous_spec):
    return "#### Schemas:\n" + _generate_schemas_notes(deleted_schemas, previous_spec)

def generate_changed_schemas_notes(changed_schemas, current_spec, previous_spec):
    # ... implementation ...
    pass 

def _generate_endpoints_notes(endpoints, spec):
    notes = ""
    for endpoint in endpoints:
        http_methods = spec['paths'].get(endpoint, {})
        for method, details in http_methods.items():
            description = details.get('description', '')
            notes += f"- {endpoint} [{method.upper()}]: {description}\n"
    return notes

def generate_added_endpoints_notes(added_endpoints, current_spec):
    return "#### Endpoints:\n" + _generate_endpoints_notes(added_endpoints, current_spec)

def generate_deleted_endpoints_notes(deleted_endpoints, previous_spec):
    return "#### Endpoints:\n" + _generate_endpoints_notes(deleted_endpoints, previous_spec)

def generate_changed_endpoints_notes(changed_endpoints, current_spec, previous_spec):
    # ... implementation ...
    pass

def _get_specs_for_change_type(change_type, current_spec, previous_spec):
    if change_type == 'changed':
        return current_spec, previous_spec
    return (current_spec,) if change_type != 'deleted' else (previous_spec,)

# --- Release notes generation ---

NOTE_GENERATORS = {
    'added': {
        'schemas': generate_added_schemas_notes,
        'endpoints': generate_added_endpoints_notes
    },
    'deleted': {
        'schemas': generate_deleted_schemas_notes,
        'endpoints': generate_deleted_endpoints_notes
    },
    'changed': {
        'schemas': generate_changed_schemas_notes,
        'endpoints': generate_changed_endpoints_notes
    }
}

def generate_release_notes(buckets, current_spec, previous_spec):
    release_notes = "## Release Notes\n\n"
    for change_type, categories in buckets.items():
        section_content = ""
        for category, items in categories.items():
            if items:
                specs = _get_specs_for_change_type(change_type, current_spec, previous_spec)
                section_content += NOTE_GENERATORS[change_type][category](items, *specs)

        if section_content:
            release_notes += f"### {change_type.capitalize()}:\n{section_content}"

    return release_notes

# --- Main ---
OLD_OPENAPI_FILE_PATH = 'openapi_old.yaml'
OPENAPI_FILE_PATH = 'openapi.yaml'
def main():
    with open(OLD_OPENAPI_FILE_PATH, 'r') as file:
        previous_spec = yaml.safe_load(file)
    with open(OPENAPI_FILE_PATH, 'r') as file:
        current_spec = yaml.safe_load(file)

    if not previous_spec or not current_spec:
        raise ValueError("Unable to read openapi.yaml files.")
        
    diff = DeepDiff(previous_spec, current_spec)
    buckets = extract_changes(diff)
    release_notes = generate_release_notes(buckets, current_spec, previous_spec)

    with open('RELEASE_NOTES.md', 'w') as file:
        file.write(release_notes)

    # os.remove(OLD_OPENAPI_FILE_PATH)

    print("Release notes generated.")

if __name__ == "__main__":
    main()
