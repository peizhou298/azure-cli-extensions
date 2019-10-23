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
# create_or_update -- create
        self.cmd('peering asn create  --name "MyPeerAsn" --peer-asn "65000" --emails "abc@contoso.com,xyz@contoso.com" --phone "+1 (234) 567-8900" --peer-name "Contoso"', checks=[
        ])

        self.cmd('peering asn create  --name "MyPeerAsn"', checks=[
        ])

# create_or_update -- update
        self.cmd('peering asn update  --name "MyPeerAsn" --peer-asn "65000" --emails "abc@contoso.com,xyz@contoso.com" --phone "+1 (234) 567-8900" --peer-name "Contoso"', checks=[
        ])

        self.cmd('peering asn update  --name "MyPeerAsn"', checks=[
        ])

# delete -- delete
        self.cmd('peering asn delete  --name "MyPeerAsn"', checks=[
        ])

        self.cmd('peering asn delete  --name "MyPeerAsn"', checks=[
        ])

# list_by_subscription -- list
        self.cmd('peering asn list ', checks=[
        ])

        self.cmd('peering asn list ', checks=[
        ])

# get -- show
        self.cmd('peering asn show  --name "MyPeerAsn"', checks=[
        ])

        self.cmd('peering asn show  --name "MyPeerAsn"', checks=[
        ])

# list -- list
# create_or_update -- create
        self.cmd('peering create  --resource-group "MyResourceGroup" --name "MyPeering" --sku-name "Basic_Direct_Free" --kind "Direct" --direct-direct-peering-type "Edge" --peering-location "peeringLocation0" --location "eastus"', checks=[
        ])

        self.cmd('peering create  --resource-group "MyResourceGroup" --name "MyPeering" --sku-name "Basic_Exchange_Free" --kind "Exchange" --peering-location "peeringLocation0" --location "eastus"', checks=[
        ])

        self.cmd('peering create  --resource-group "MyResourceGroup" --name "MyPeering"', checks=[
        ])

        self.cmd('peering create  --resource-group "MyResourceGroup" --name "MyPeering"', checks=[
        ])

# create_or_update -- update
        self.cmd('peering update  --resource-group "MyResourceGroup" --name "MyPeering" --sku-name "Basic_Direct_Free" --kind "Direct" --direct-direct-peering-type "Edge" --peering-location "peeringLocation0" --location "eastus"', checks=[
        ])

        self.cmd('peering update  --resource-group "MyResourceGroup" --name "MyPeering" --sku-name "Basic_Exchange_Free" --kind "Exchange" --peering-location "peeringLocation0" --location "eastus"', checks=[
        ])

        self.cmd('peering update  --resource-group "MyResourceGroup" --name "MyPeering"', checks=[
        ])

        self.cmd('peering update  --resource-group "MyResourceGroup" --name "MyPeering"', checks=[
        ])

# delete -- delete
        self.cmd('peering delete  --resource-group "MyResourceGroup" --name "MyPeering"', checks=[
        ])

        self.cmd('peering delete  --resource-group "MyResourceGroup" --name "MyPeering"', checks=[
        ])

        self.cmd('peering delete  --resource-group "MyResourceGroup" --name "MyPeering"', checks=[
        ])

        self.cmd('peering delete  --resource-group "MyResourceGroup" --name "MyPeering"', checks=[
        ])

# list_by_resource_group -- list
        self.cmd('peering list  --resource-group "MyResourceGroup"', checks=[
        ])

        self.cmd('peering list  --resource-group "MyResourceGroup"', checks=[
        ])

        self.cmd('peering list  --resource-group "MyResourceGroup"', checks=[
        ])

        self.cmd('peering list  --resource-group "MyResourceGroup"', checks=[
        ])

# list_by_subscription -- list
        self.cmd('peering list  --resource-group "MyResourceGroup"', checks=[
        ])

        self.cmd('peering list  --resource-group "MyResourceGroup"', checks=[
        ])

        self.cmd('peering list  --resource-group "MyResourceGroup"', checks=[
        ])

        self.cmd('peering list  --resource-group "MyResourceGroup"', checks=[
        ])

# get -- show
        self.cmd('peering show  --resource-group "MyResourceGroup" --name "MyPeering"', checks=[
        ])

        self.cmd('peering show  --resource-group "MyResourceGroup" --name "MyPeering"', checks=[
        ])

        self.cmd('peering show  --resource-group "MyResourceGroup" --name "MyPeering"', checks=[
        ])

        self.cmd('peering show  --resource-group "MyResourceGroup" --name "MyPeering"', checks=[
        ])

# list -- list
# create_or_update -- create
        self.cmd('peering service prefix create  --resource-group "MyResourceGroup" --peering-service-name "MyPeeringService" --name "MyPeeringServicePrefix" --prefix "192.168.1.0/24"', checks=[
        ])

        self.cmd('peering service prefix create  --resource-group "MyResourceGroup" --peering-service-name "MyPeeringService" --name "MyPeeringServicePrefix"', checks=[
        ])

# create_or_update -- update
        self.cmd('peering service prefix update  --resource-group "MyResourceGroup" --peering-service-name "MyPeeringService" --name "MyPeeringServicePrefix" --prefix "192.168.1.0/24"', checks=[
        ])

        self.cmd('peering service prefix update  --resource-group "MyResourceGroup" --peering-service-name "MyPeeringService" --name "MyPeeringServicePrefix"', checks=[
        ])

# delete -- delete
        self.cmd('peering service prefix delete  --resource-group "MyResourceGroup" --peering-service-name "MyPeeringService" --name "MyPeeringServicePrefix"', checks=[
        ])

        self.cmd('peering service prefix delete  --resource-group "MyResourceGroup" --peering-service-name "MyPeeringService" --name "MyPeeringServicePrefix"', checks=[
        ])

# list_by_peering_service -- list
        self.cmd('peering service prefix list  --resource-group "MyResourceGroup" --peering-service-name "MyPeeringService"', checks=[
        ])

        self.cmd('peering service prefix list  --resource-group "MyResourceGroup" --peering-service-name "MyPeeringService"', checks=[
        ])

# get -- show
        self.cmd('peering service prefix show  --resource-group "MyResourceGroup" --peering-service-name "MyPeeringService" --name "MyPeeringServicePrefix"', checks=[
        ])

        self.cmd('peering service prefix show  --resource-group "MyResourceGroup" --peering-service-name "MyPeeringService" --name "MyPeeringServicePrefix"', checks=[
        ])

# list -- list
# create_or_update -- create
        self.cmd('peering service create  --resource-group "MyResourceGroup" --name "MyPeeringService" --peering-service-location "state1" --peering-service-provider "serviceProvider1" --location "eastus"', checks=[
        ])

        self.cmd('peering service create  --resource-group "MyResourceGroup" --name "MyPeeringService"', checks=[
        ])

        self.cmd('peering service create  --resource-group "MyResourceGroup" --name "MyPeeringService"', checks=[
        ])

# create_or_update -- update
        self.cmd('peering service update  --resource-group "MyResourceGroup" --name "MyPeeringService" --peering-service-location "state1" --peering-service-provider "serviceProvider1" --location "eastus"', checks=[
        ])

        self.cmd('peering service update  --resource-group "MyResourceGroup" --name "MyPeeringService"', checks=[
        ])

        self.cmd('peering service update  --resource-group "MyResourceGroup" --name "MyPeeringService"', checks=[
        ])

# delete -- delete
        self.cmd('peering service delete  --resource-group "MyResourceGroup" --name "MyPeeringService"', checks=[
        ])

        self.cmd('peering service delete  --resource-group "MyResourceGroup" --name "MyPeeringService"', checks=[
        ])

        self.cmd('peering service delete  --resource-group "MyResourceGroup" --name "MyPeeringService"', checks=[
        ])

# list_by_resource_group -- list
        self.cmd('peering service list  --resource-group "MyResourceGroup"', checks=[
        ])

        self.cmd('peering service list  --resource-group "MyResourceGroup"', checks=[
        ])

        self.cmd('peering service list  --resource-group "MyResourceGroup"', checks=[
        ])

# list_by_subscription -- list
        self.cmd('peering service list  --resource-group "MyResourceGroup"', checks=[
        ])

        self.cmd('peering service list  --resource-group "MyResourceGroup"', checks=[
        ])

        self.cmd('peering service list  --resource-group "MyResourceGroup"', checks=[
        ])

# get -- show
        self.cmd('peering service show  --resource-group "MyResourceGroup" --name "MyPeeringService"', checks=[
        ])

        self.cmd('peering service show  --resource-group "MyResourceGroup" --name "MyPeeringService"', checks=[
        ])

        self.cmd('peering service show  --resource-group "MyResourceGroup" --name "MyPeeringService"', checks=[
        ])
