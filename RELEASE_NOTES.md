## Release Notes

### Added:
#### Schemas:
- Set App Owners Request: The request message for setting the app owners.
- Set App Owners Response: The empty response message for setting the app owners.
- Marker: The Marker message.
- Validate Policy Cel Request: The ValidatePolicyCELRequest message.
- Validate Policy Cel Response: The ValidatePolicyCELResponse message.
- Task Actions Service Restart Request: The TaskActionsServiceRestartRequest object lets you restart a task.
- Task Actions Service Restart Response: The TaskActionsServiceRestartResponse message.
#### Endpoints:
- /api/v1/policies/validate/cel [POST]: Validate policies
- /api/v1/tasks/{task_id}/action/restart [POST]: Invokes the c1.api.task.v1.TaskActionsService.Restart method.
### Changed:
#### Schemas:
- root['components']['schemas']['c1.api.app.v1.App']['properties']['isDirectory']
- root['components']['schemas']['c1.api.app.v1.AppEntitlement']['properties']['userEditedMask']
- root['components']['schemas']['c1.api.app.v1.AppResource']['properties']['parentAppResourceId']
- root['components']['schemas']['c1.api.app.v1.AppResource']['properties']['parentAppResourceTypeId']
- root['components']['schemas']['c1.api.app.v1.AppResourceView']['properties']['parentResourcePath']
- root['components']['schemas']['c1.api.app.v1.AppResourceView']['properties']['parentResourceTypePath']
- root['components']['schemas']['c1.api.app.v1.AppUser']['properties']['emails']
- root['components']['schemas']['c1.api.app.v1.AppUser']['properties']['username']
- root['components']['schemas']['c1.api.app.v1.AppUser']['properties']['usernames']
- root['components']['schemas']['c1.api.app.v1.SearchAppsRequest']['properties']['onlyDirectories']
- root['components']['schemas']['c1.api.policy.v1.DelegatedProvision']['properties']['implicit']
- root['components']['schemas']['c1.api.task.v1.Task']['properties']['insightIds']
- root['components']['schemas']['c1.api.task.v1.Task']['properties']['recommendation']
- root['components']['schemas']['c1.api.task.v1.TaskView']['properties']['insightsPath']
- root['components']['schemas']['c1.api.user.v1.User']['properties']['emails']
- root['components']['schemas']['c1.api.user.v1.User']['properties']['username']
- root['components']['schemas']['c1.api.user.v1.User']['properties']['usernames']
- root['components']['schemas']['c1.api.policy.v1.AppGroupApproval']['properties']['allowSelfApproval']['readOnly']
- root['components']['schemas']['c1.api.policy.v1.AppGroupApproval']['properties']['appGroupId']['readOnly']
- root['components']['schemas']['c1.api.policy.v1.AppGroupApproval']['properties']['appId']['readOnly']
- root['components']['schemas']['c1.api.policy.v1.AppGroupApproval']['properties']['fallback']['readOnly']
- root['components']['schemas']['c1.api.policy.v1.AppGroupApproval']['properties']['fallbackUserIds']['readOnly']
- root['components']['schemas']['c1.api.policy.v1.AppOwnerApproval']['properties']['allowSelfApproval']['readOnly']
- root['components']['schemas']['c1.api.policy.v1.Approval']['properties']['allowReassignment']['readOnly']
- root['components']['schemas']['c1.api.policy.v1.Approval']['properties']['assigned']['readOnly']
- root['components']['schemas']['c1.api.policy.v1.Approval']['properties']['requireApprovalReason']['readOnly']
- root['components']['schemas']['c1.api.policy.v1.Approval']['properties']['requireReassignmentReason']['readOnly']
- root['components']['schemas']['c1.api.policy.v1.EntitlementOwnerApproval']['properties']['allowSelfApproval']['readOnly']
- root['components']['schemas']['c1.api.policy.v1.EntitlementOwnerApproval']['properties']['fallback']['readOnly']
- root['components']['schemas']['c1.api.policy.v1.EntitlementOwnerApproval']['properties']['fallbackUserIds']['readOnly']
- root['components']['schemas']['c1.api.policy.v1.ExpressionApproval']['properties']['allowSelfApproval']['readOnly']
- root['components']['schemas']['c1.api.policy.v1.ExpressionApproval']['properties']['assignedUserIds']['readOnly']
- root['components']['schemas']['c1.api.policy.v1.ExpressionApproval']['properties']['expressions']['readOnly']
- root['components']['schemas']['c1.api.policy.v1.ExpressionApproval']['properties']['fallback']['readOnly']
- root['components']['schemas']['c1.api.policy.v1.ExpressionApproval']['properties']['fallbackUserIds']['readOnly']
- root['components']['schemas']['c1.api.policy.v1.ManagerApproval']['properties']['allowSelfApproval']['readOnly']
- root['components']['schemas']['c1.api.policy.v1.ManagerApproval']['properties']['assignedUserIds']['readOnly']
- root['components']['schemas']['c1.api.policy.v1.ManagerApproval']['properties']['fallback']['readOnly']
- root['components']['schemas']['c1.api.policy.v1.ManagerApproval']['properties']['fallbackUserIds']['readOnly']
- root['components']['schemas']['c1.api.policy.v1.SelfApproval']['properties']['assignedUserIds']['readOnly']
- root['components']['schemas']['c1.api.policy.v1.SelfApproval']['properties']['fallback']['readOnly']
- root['components']['schemas']['c1.api.policy.v1.SelfApproval']['properties']['fallbackUserIds']['readOnly']
- root['components']['schemas']['c1.api.policy.v1.UserApproval']['properties']['allowSelfApproval']['readOnly']
- root['components']['schemas']['c1.api.policy.v1.UserApproval']['properties']['userIds']['readOnly']
#### Endpoints:
- root['paths']['/api/v1/apps/{app_id}/owners']['put']
