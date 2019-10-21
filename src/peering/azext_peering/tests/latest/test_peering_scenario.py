# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import unittest

from azure_devtools.scenario_tests import AllowLargeResponse
from azure.cli.testsdk import (ScenarioTest, ResourceGroupPreparer)


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


class ApimgmtScenarioTest(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='cli_test_apimgmt')
    def test_apimgmt(self, resource_group):

        self.kwargs.update({
            'name': 'test1'
        })

# list -- list
# list -- list
# create_or_update -- create
        self.cmd('peering asn create  --name "peerAsnName" --peer-asn "65000" --emails "abc@contoso.com,xyz@contoso.com" --phone "+1 (234) 567-8900" --peer-name "Contoso"', checks=[
        ])

        self.cmd('peering asn create  --name "peerAsnName"', checks=[
        ])

# create_or_update -- update
        self.cmd('peering asn update  --name "peerAsnName" --peer-asn "65000" --emails "abc@contoso.com,xyz@contoso.com" --phone "+1 (234) 567-8900" --peer-name "Contoso"', checks=[
        ])

        self.cmd('peering asn update  --name "peerAsnName"', checks=[
        ])

# delete -- delete
        self.cmd('peering asn delete  --name "peerAsnName"', checks=[
        ])

        self.cmd('peering asn delete  --name "peerAsnName"', checks=[
        ])

# list_by_subscription -- list
        self.cmd('peering asn list ', checks=[
        ])

        self.cmd('peering asn list ', checks=[
        ])

# get -- show
        self.cmd('peering asn show  --name "peerAsnName"', checks=[
        ])

        self.cmd('peering asn show  --name "peerAsnName"', checks=[
        ])

# list -- list
# create_or_update -- create
        self.cmd('peering create  --resource-group "rgName" --name "peeringName" --sku-name "Basic_Direct_Free" --kind "Direct" --direct-direct-peering-type "Edge" --peering-location "peeringLocation0" --location "eastus"', checks=[
        ])

        self.cmd('peering create  --resource-group "rgName" --name "peeringName" --sku-name "Basic_Exchange_Free" --kind "Exchange" --peering-location "peeringLocation0" --location "eastus"', checks=[
        ])

        self.cmd('peering create  --resource-group "rgName" --name "peeringName"', checks=[
        ])

        self.cmd('peering create  --resource-group "rgName" --name "peeringName"', checks=[
        ])

# create_or_update -- update
        self.cmd('peering update  --resource-group "rgName" --name "peeringName" --sku-name "Basic_Direct_Free" --kind "Direct" --direct-direct-peering-type "Edge" --peering-location "peeringLocation0" --location "eastus"', checks=[
        ])

        self.cmd('peering update  --resource-group "rgName" --name "peeringName" --sku-name "Basic_Exchange_Free" --kind "Exchange" --peering-location "peeringLocation0" --location "eastus"', checks=[
        ])

        self.cmd('peering update  --resource-group "rgName" --name "peeringName"', checks=[
        ])

        self.cmd('peering update  --resource-group "rgName" --name "peeringName"', checks=[
        ])

# delete -- delete
        self.cmd('peering delete  --resource-group "rgName" --name "peeringName"', checks=[
        ])

        self.cmd('peering delete  --resource-group "rgName" --name "peeringName"', checks=[
        ])

        self.cmd('peering delete  --resource-group "rgName" --name "peeringName"', checks=[
        ])

        self.cmd('peering delete  --resource-group "rgName" --name "peeringName"', checks=[
        ])

# list_by_resource_group -- list
        self.cmd('peering list  --resource-group "rgName"', checks=[
        ])

        self.cmd('peering list  --resource-group "rgName"', checks=[
        ])

        self.cmd('peering list  --resource-group "rgName"', checks=[
        ])

        self.cmd('peering list  --resource-group "rgName"', checks=[
        ])

# list_by_subscription -- list
        self.cmd('peering list  --resource-group "rgName"', checks=[
        ])

        self.cmd('peering list  --resource-group "rgName"', checks=[
        ])

        self.cmd('peering list  --resource-group "rgName"', checks=[
        ])

        self.cmd('peering list  --resource-group "rgName"', checks=[
        ])

# get -- show
        self.cmd('peering show  --resource-group "rgName" --name "peeringName"', checks=[
        ])

        self.cmd('peering show  --resource-group "rgName" --name "peeringName"', checks=[
        ])

        self.cmd('peering show  --resource-group "rgName" --name "peeringName"', checks=[
        ])

        self.cmd('peering show  --resource-group "rgName" --name "peeringName"', checks=[
        ])

# list -- list
# create_or_update -- create
        self.cmd('peering service prefix create  --resource-group "rgName" --peering-service-name "peeringServiceName" --name "peeringServicePrefixName" --prefix "192.168.1.0/24"', checks=[
        ])

        self.cmd('peering service prefix create  --resource-group "rgName" --peering-service-name "peeringServiceName" --name "peeringServicePrefixName"', checks=[
        ])

# create_or_update -- update
        self.cmd('peering service prefix update  --resource-group "rgName" --peering-service-name "peeringServiceName" --name "peeringServicePrefixName" --prefix "192.168.1.0/24"', checks=[
        ])

        self.cmd('peering service prefix update  --resource-group "rgName" --peering-service-name "peeringServiceName" --name "peeringServicePrefixName"', checks=[
        ])

# delete -- delete
        self.cmd('peering service prefix delete  --resource-group "rgName" --peering-service-name "peeringServiceName" --name "peeringServicePrefixName"', checks=[
        ])

        self.cmd('peering service prefix delete  --resource-group "rgName" --peering-service-name "peeringServiceName" --name "peeringServicePrefixName"', checks=[
        ])

# list_by_peering_service -- list
        self.cmd('peering service prefix list  --resource-group "rgName" --peering-service-name "peeringServiceName"', checks=[
        ])

        self.cmd('peering service prefix list  --resource-group "rgName" --peering-service-name "peeringServiceName"', checks=[
        ])

# get -- show
        self.cmd('peering service prefix show  --resource-group "rgName" --peering-service-name "peeringServiceName" --name "peeringServicePrefixName"', checks=[
        ])

        self.cmd('peering service prefix show  --resource-group "rgName" --peering-service-name "peeringServiceName" --name "peeringServicePrefixName"', checks=[
        ])

# list -- list
# create_or_update -- create
        self.cmd('peering service create  --resource-group "rgName" --name "peeringServiceName" --peering-service-location "state1" --peering-service-provider "serviceProvider1" --location "eastus"', checks=[
        ])

        self.cmd('peering service create  --resource-group "rgName" --name "peeringServiceName"', checks=[
        ])

        self.cmd('peering service create  --resource-group "rgName" --name "peeringServiceName"', checks=[
        ])

# create_or_update -- update
        self.cmd('peering service update  --resource-group "rgName" --name "peeringServiceName" --peering-service-location "state1" --peering-service-provider "serviceProvider1" --location "eastus"', checks=[
        ])

        self.cmd('peering service update  --resource-group "rgName" --name "peeringServiceName"', checks=[
        ])

        self.cmd('peering service update  --resource-group "rgName" --name "peeringServiceName"', checks=[
        ])

# delete -- delete
        self.cmd('peering service delete  --resource-group "rgName" --name "peeringServiceName"', checks=[
        ])

        self.cmd('peering service delete  --resource-group "rgName" --name "peeringServiceName"', checks=[
        ])

        self.cmd('peering service delete  --resource-group "rgName" --name "peeringServiceName"', checks=[
        ])

# list_by_resource_group -- list
        self.cmd('peering service list  --resource-group "rgName"', checks=[
        ])

        self.cmd('peering service list  --resource-group "rgName"', checks=[
        ])

        self.cmd('peering service list  --resource-group "rgName"', checks=[
        ])

# list_by_subscription -- list
        self.cmd('peering service list  --resource-group "rgName"', checks=[
        ])

        self.cmd('peering service list  --resource-group "rgName"', checks=[
        ])

        self.cmd('peering service list  --resource-group "rgName"', checks=[
        ])

# get -- show
        self.cmd('peering service show  --resource-group "rgName" --name "peeringServiceName"', checks=[
        ])

        self.cmd('peering service show  --resource-group "rgName" --name "peeringServiceName"', checks=[
        ])

        self.cmd('peering service show  --resource-group "rgName" --name "peeringServiceName"', checks=[
        ])
