# Azure CLI Module Creation Report

## peering

### peering list

list a peering.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
## peering asn

### peering asn create

create a peering asn.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--name**|str|The peer ASN name.|peer_asn_name|peerAsnName|
|--peer-asn|number|The Autonomous System Number (ASN) of the peer.|/peer_asn|/properties/peerAsn|
|--emails|list|The list of email addresses.|/peer_contact_info/emails|/properties/peerContactInfo/emails|
|--phone|list|The list of contact numbers.|/peer_contact_info/phone|/properties/peerContactInfo/phone|
|--peer-name|str|The name of the peer.|/peer_name|/properties/peerName|
|--validation-state|str|The validation state of the ASN associated with the peer.|/validation_state|/properties/validationState|

**Example: Create a peer ASN**

```
peering asn create --name peerAsnName
        --peer-asn 65000
        --emails abc@contoso.com,xyz@contoso.com
        --phone "+1 (234) 567-8900"
        --peer-name Contoso
```
### peering asn update

update a peering asn.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--name**|str|The peer ASN name.|peer_asn_name|peerAsnName|
|--peer-asn|number|The Autonomous System Number (ASN) of the peer.|/peer_asn|/properties/peerAsn|
|--emails|list|The list of email addresses.|/peer_contact_info/emails|/properties/peerContactInfo/emails|
|--phone|list|The list of contact numbers.|/peer_contact_info/phone|/properties/peerContactInfo/phone|
|--peer-name|str|The name of the peer.|/peer_name|/properties/peerName|
|--validation-state|str|The validation state of the ASN associated with the peer.|/validation_state|/properties/validationState|
### peering asn delete

delete a peering asn.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--name**|str|The peer ASN name.|peer_asn_name|peerAsnName|

**Example: Delete a peer ASN**

```
peering asn delete --name peerAsnName
```
### peering asn list

list a peering asn.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
### peering asn show

show a peering asn.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--name**|str|The peer ASN name.|peer_asn_name|peerAsnName|
## peering service

### peering service create

create a peering service.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--name**|str|The name of the peering service.|peering_service_name|peeringServiceName|
|**--location**|str|The location of the resource.|/location|/location|
|--peering-service-location|str|The PeeringServiceLocation of the Customer.|/peering_service_location|/properties/peeringServiceLocation|
|--peering-service-provider|str|The MAPS Provider Name.|/peering_service_provider|/properties/peeringServiceProvider|
|--tags|dictionary|The resource tags.|/tags|/tags|

**Example: Create a  peering service**

```
peering service create --resource-group rgName
        --name peeringServiceName
        --peering-service-location state1
        --peering-service-provider serviceProvider1
        --location eastus
```
### peering service update

update a peering service.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--name**|str|The name of the peering service.|peering_service_name|peeringServiceName|
|**--location**|str|The location of the resource.|/location|/location|
|--peering-service-location|str|The PeeringServiceLocation of the Customer.|/peering_service_location|/properties/peeringServiceLocation|
|--peering-service-provider|str|The MAPS Provider Name.|/peering_service_provider|/properties/peeringServiceProvider|
|--tags|dictionary|The resource tags.|/tags|/tags|

**Example: Update peering service tags**

```
peering service update --resource-group rgName
        --name peeringServiceName
```
### peering service delete

delete a peering service.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--name**|str|The name of the peering service.|peering_service_name|peeringServiceName|

**Example: Delete a peering service**

```
peering service delete --resource-group rgName
        --name peeringServiceName
```
### peering service list

list a peering service.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
### peering service show

show a peering service.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--name**|str|The name of the peering service.|peering_service_name|peeringServiceName|
## peering service prefix

### peering service prefix create

create a peering service prefix.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--peering-service-name**|str|The name of the peering service.|peering_service_name|peeringServiceName|
|**--name**|str|The name of the prefix.|prefix_name|prefixName|
|--prefix|str|The prefix from which your traffic originates.|/prefix|/properties/prefix|

**Example: Create or update a prefix for the peering service**

```
peering service prefix create --resource-group rgName
        --peering-service-name peeringServiceName
        --name peeringServicePrefixName
        --prefix 192.168.1.0/24
```
### peering service prefix update

update a peering service prefix.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--peering-service-name**|str|The name of the peering service.|peering_service_name|peeringServiceName|
|**--name**|str|The name of the prefix.|prefix_name|prefixName|
|--prefix|str|The prefix from which your traffic originates.|/prefix|/properties/prefix|
### peering service prefix delete

delete a peering service prefix.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--peering-service-name**|str|The name of the peering service.|peering_service_name|peeringServiceName|
|**--name**|str|The name of the prefix.|prefix_name|prefixName|

**Example: Delete a prefix associated with the peering service**

```
peering service prefix delete --resource-group rgName
        --peering-service-name peeringServiceName
        --name peeringServicePrefixName
```
### peering service prefix list

list a peering service prefix.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--peering-service-name**|str|The name of the peering service.|peering_service_name|peeringServiceName|
### peering service prefix show

show a peering service prefix.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--peering-service-name**|str|The name of the peering service.|peering_service_name|peeringServiceName|
|**--name**|str|The name of the prefix.|prefix_name|prefixName|