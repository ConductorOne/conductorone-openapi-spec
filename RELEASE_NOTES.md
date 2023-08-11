## Release Notes

### Added:
#### Schemas:
- Attribute Type: AttributeType defines the type of an attribute.
- Attribute Value: AttributeValue is the value of an attribute of a defined type.
- Create Attribute Value Request: The CreateAttributeValueRequest message.
- Create Attribute Value Response: CreateAttributeValueResponse is the response for creating an attribute value.
- Delete Attribute Value Request: The DeleteAttributeValueRequest message.
- Delete Attribute Value Response: DeleteAttributeValueResponse is the empty response for deleting an attribute value.
- Get Attribute Value Response: GetAttributeValueResponse is the response for getting an attribute value by id.
- List Attribute Types Response: ListAttributeTypesResponse is the response for listing attribute types.
- List Attribute Values Response: ListAttributeValuesResponse is the response for listing attribute values for a given AttributeType.
- Search Attribute Values Request: Search Attributes by a few properties.
- Search Attribute Values Response: SearchAttributeValuesResponse is the response for searching AttributeValues.
- Provision Target: ProvisionTarget indicates the specific app, app entitlement, and if known, the app user and grant duration of this provision step
#### Endpoints:
- /api/v1/attribute/{id} [DELETE]: Delete an attribute value by id.
- /api/v1/attributes [POST]: Create a new attribute value.
- /api/v1/attributes/{id} [GET]: Get an attribute value by id.
- /api/v1/attributes/types [GET]: List all attribute types.
- /api/v1/attributes/types/{attribute_type_id}/values [GET]: List all attribute values for a given attribute type.
- /api/v1/search/attributes [POST]: Search attributes based on filters specified in the request body.
### Changed:
#### Schemas:
- root['components']['schemas']['c1.api.policy.v1.Provision']['properties']['provisionTarget']
