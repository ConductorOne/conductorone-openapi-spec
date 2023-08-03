import yaml
from deepdiff import DeepDiff

# Read the previous version of the OpenAPI file
with open('path/to/existing/openapi_old.yaml', 'r') as file:
    previous_spec = yaml.safe_load(file)

# Read the current version of the OpenAPI file
with open('openapi.yaml', 'r') as file:
    current_spec = yaml.safe_load(file)

# Compare the two specifications
diff = DeepDiff(previous_spec, current_spec)

# Create the release notes
release_notes = "## Release Notes\n\n"

if 'dictionary_item_added' in diff:
    release_notes += "### New Endpoints/Schemas:\n"
    for item in diff['dictionary_item_added']:
        release_notes += f"- {item}\n"

if 'dictionary_item_removed' in diff:
    release_notes += "### Removed Endpoints/Schemas:\n"
    for item in diff['dictionary_item_removed']:
        release_notes += f"- {item}\n"

if 'values_changed' in diff:
    release_notes += "### Changed Endpoints/Schemas:\n"
    for item in diff['values_changed']:
        release_notes += f"- {item}\n"

# Optional: Write the release notes to a file
with open('RELEASE_NOTES.md', 'w') as file:
    file.write(release_notes)

# Optional: Set the release notes as an environment variable
# You can use this variable in the GitHub Actions workflow
import os
os.environ['RELEASE_NOTES'] = release_notes

print("Release notes generated.")
