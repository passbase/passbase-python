# Identity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID of the identity | [optional] 
**status** | **str** | Current state of the identity in Passbase&#x27;s systems | [optional] 
**owner** | [**IdentityOwner**](IdentityOwner.md) |  | [optional] 
**score** | **float** | Float between 0 and 1 representing our confidence that this identity is valid. 0 meaning we couldn&#x27;t verify any of the information provided with accuracy, and 1 absolute confidence. | [optional] 
**created** | **int** | Unix-timestamp of when the identity was created | [optional] 
**updated** | **int** | Unix-timestamp of when the identity was updated | [optional] 
**resources** | [**list[IdentityResource]**](IdentityResource.md) | resources attached to a verification | [optional] 
**watchlist** | [**WatchlistResponse**](WatchlistResponse.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

