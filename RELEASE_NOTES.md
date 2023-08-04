## Release Notes

### Added:
#### Schemas:
- Attribute Type: The AttributeType message.
- Attribute Value: The AttributeValue message.
- Create Attribute Value Request: The CreateAttributeValueRequest message.
- Create Attribute Value Response: The CreateAttributeValueResponse message.
- Delete Attribute Value Request: The DeleteAttributeValueRequest message.
- Delete Attribute Value Response: The DeleteAttributeValueResponse message.
- Get Attribute Value Response: The GetAttributeValueResponse message.
- List Attribute Types Response: The ListAttributeTypesResponse message.
- List Attribute Values Response: The ListAttributeValuesResponse message.
- Search Attribute Values Request: Search Attributes by a few properties.
- Search Attribute Values Response: The SearchAttributeValuesResponse message.
#### Endpoints:
- /api/v1/attribute/{id} [DELETE]: Invokes the c1.api.attribute.v1.Attributes.DeleteAttributeValue method.
- /api/v1/attributes [POST]: Invokes the c1.api.attribute.v1.Attributes.CreateAttributeValue method.
- /api/v1/attributes/{id} [GET]: Invokes the c1.api.attribute.v1.Attributes.GetAttributeValue method.
- /api/v1/attributes/types [GET]: Invokes the c1.api.attribute.v1.Attributes.ListAttributeTypes method.
- /api/v1/attributes/values [GET]: Invokes the c1.api.attribute.v1.Attributes.ListAttributeValues method.
- /api/v1/search/attributes [POST]: Search attributes based on filters specified in the request body.
### Changed:
#### Schemas:
- root['components']['schemas']['c1.api.task.v1.TaskView']['properties']['test']
