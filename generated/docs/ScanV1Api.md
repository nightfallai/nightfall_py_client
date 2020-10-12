# openapi_client.ScanV1Api

All URIs are relative to *https://api.nightfall.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**scan_payload_v1**](ScanV1Api.md#scan_payload_v1) | **POST** /v1/scan | Scan for sensitive information in your data


# **scan_payload_v1**
> list[list] scan_payload_v1(scan_req_v1)

Scan for sensitive information in your data

Provide a list of arbitrary string data, and scan each item with the provided detectors to uncover sensitive information. Returns a list equal in size to the number of provided string payloads. The item at each list index will be a list of all matches for the provided detectors, or an empty list if no occurrences are found.

### Example

* Api Key Authentication (apiKeyAuth):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.nightfall.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.nightfall.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuth
configuration = openapi_client.Configuration(
    host = "https://api.nightfall.ai",
    api_key = {
        'x-api-key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ScanV1Api(api_client)
    scan_req_v1 = openapi_client.ScanRequest() # ScanRequest | 

    try:
        # Scan for sensitive information in your data
        api_response = api_instance.scan_payload_v1(scan_req_v1)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ScanV1Api->scan_payload_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scan_req_v1** | [**ScanRequest**](ScanRequest.md)|  | 

### Return type

**list[list]**

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  * Content-Type - the content type of the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

