## Release Notes

### Added:
#### Schemas:
- Accept: This policy step indicates that a ticket should have an approved outcome. This is a terminal approval state and is used to explicitly define the end of approval steps.
- Accept Instance: This policy step indicates that a ticket should have an approved outcome. This is a terminal approval state and is used to explicitly define the end of approval steps.
 The instance is just a marker for it being copied into an active policy.
- Expression Approval: The ExpressionApproval message.
- Rule: The Rule message.
- Reject: This policy step indicates that a ticket should have a denied outcome. This is a terminal approval state and is used to explicitly define the end of approval steps.
- Reject Instance: This policy step indicates that a ticket should have a denied outcome. This is a terminal approval state and is used to explicitly define the end of approval steps.
 The instance is just a marker for it being copied into an active policy.
- Request Catalog Management Service List Response: The RequestCatalogManagementServiceListResponse message.
### Changed:
#### Schemas:
- root['components']['schemas']['c1.api.app.v1.AppEntitlementSearchServiceSearchRequest']['properties']['includeDeleted']
- root['components']['schemas']['c1.api.policy.v1.Approval']['properties']['expression']
- root['components']['schemas']['c1.api.policy.v1.Policy']['properties']['rules']
- root['components']['schemas']['c1.api.policy.v1.PolicyStep']['properties']['accept']
- root['components']['schemas']['c1.api.policy.v1.PolicyStep']['properties']['reject']
- root['components']['schemas']['c1.api.policy.v1.PolicyStepInstance']['properties']['accept']
- root['components']['schemas']['c1.api.policy.v1.PolicyStepInstance']['properties']['reject']
- root['components']['schemas']['c1.api.requestcatalog.v1.RequestCatalogSearchServiceSearchEntitlementsRequest']['properties']['includeDeleted']
#### Endpoints:
- root['paths']['/api/v1/catalogs']['get']
