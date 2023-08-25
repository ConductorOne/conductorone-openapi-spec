## Release Notes

### Added:
#### Schemas:
- Add App Entitlement Owner Request: The request message for adding an app entitlement owner.
- Add App Entitlement Owner Response: The empty response message for adding an app entitlement owner.
- App User Expand Mask: The AppUserExpandMask message contains a list of paths to expand in the response.
- App User Service Update Request: The AppUserServiceUpdateRequest message contains the app user and the fields to be updated.
- App User Service Update Response: The AppUserServiceUpdateResponse message.
- List App Entitlement Owners Response: The response message for listing app entitlement owners.
- Remove App Entitlement Owner Request: The request message for removing an app entitlement owner.
- Remove App Entitlement Owner Response: The empty response message for removing an app entitlement owner.
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
- Task Grant Source: The TaskGrantSource message tracks which external URL was the source of the specificed grant ticket.
#### Endpoints:
- /api/v1/apps/{app_id}/entitlements/{entitlement_id}/owners [GET]: List owners for a given app entitlement.
- /api/v1/apps/{app_id}/entitlements/{entitlement_id}/owners [POST]: Add an owner to a given app entitlement.
- /api/v1/apps/{app_id}/entitlements/{entitlement_id}/owners/{user_id} [DELETE]: Remove an owner from a given app entitlement.
- /api/v1/apps/{app_user_app_id}/app_users/{app_user_id} [POST]: Update an app user by ID. Only the fields specified in the update mask are updated.
 Currently, only the appUserType, and identityUserId fields can be updated.
- /api/v1/attribute/{id} [DELETE]: Delete an attribute value by id.
- /api/v1/attributes [POST]: Create a new attribute value.
- /api/v1/attributes/{id} [GET]: Get an attribute value by id.
- /api/v1/attributes/types [GET]: List all attribute types.
- /api/v1/attributes/types/{attribute_type_id}/values [GET]: List all attribute values for a given attribute type.
- /api/v1/search/attributes [POST]: Search attributes based on filters specified in the request body.
### Deleted:
#### Schemas:
- App Group: The AppGroup message.
- List App Entitlement Groups Response: The ListAppEntitlementGroupsResponse message contains a list of results and a nextPageToken if applicable.
#### Endpoints:
- /api/v1/apps/{app_id}/entitlements/{app_entitlement_id}/groups [GET]: List app groups associated with an app entitlement.
### Changed:
#### Schemas:
- root['components']['schemas']['c1.api.policy.v1.Provision']['properties']['provisionTarget']
- root['components']['schemas']['c1.api.task.v1.TaskServiceCreateGrantRequest']['properties']['source']
- root['components']['schemas']['c1.api.task.v1.TaskTypeGrant']['properties']['source']
- root['components']['schemas']['c1.api.app.v1.AppResourceTypeServiceListResponse']['properties']['notificationToken']
- root['components']['schemas']['c1.api.app.v1.ListAppOwnersResponse']['properties']['notificationToken']
- root['components']['schemas']['c1.api.app.v1.ListAppResourceOwnersResponse']['properties']['notificationToken']
- root['components']['schemas']['c1.api.app.v1.ListAppsResponse']['properties']['notificationToken']
- root['components']['schemas']['c1.api.app.v1.SearchAppResourceTypesResponse']['properties']['notificationToken']
- root['components']['schemas']['c1.api.app.v1.SearchAppsResponse']['properties']['notificationToken']
- root['components']['schemas']['c1.api.iam.v1.ListRolesResponse']['properties']['notificationToken']
- root['components']['schemas']['c1.api.policy.v1.ListPolicyResponse']['properties']['notificationToken']
- root['components']['schemas']['c1.api.user.v1.SearchUsersResponse']['properties']['notificationToken']
- root['components']['schemas']['c1.api.user.v1.UserServiceListResponse']['properties']['notificationToken']
