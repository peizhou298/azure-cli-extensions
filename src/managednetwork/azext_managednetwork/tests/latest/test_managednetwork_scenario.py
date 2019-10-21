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

# create_or_update -- create
        self.cmd('managednetwork create  --resource-group "myResourceGroup" --name "myManagedNetwork" --location "eastus"', checks=[
        ])

        self.cmd('managednetwork create  --resource-group "myResourceGroup" --name "myManagedNetwork"', checks=[
        ])

        self.cmd('managednetwork create  --resource-group "myResourceGroup" --name "myManagedNetwork"', checks=[
        ])

# create_or_update -- update
        self.cmd('managednetwork update  --resource-group "myResourceGroup" --name "myManagedNetwork" --location "eastus"', checks=[
        ])

        self.cmd('managednetwork update  --resource-group "myResourceGroup" --name "myManagedNetwork"', checks=[
        ])

        self.cmd('managednetwork update  --resource-group "myResourceGroup" --name "myManagedNetwork"', checks=[
        ])

# delete -- delete
        self.cmd('managednetwork delete  --resource-group "myResourceGroup" --name "myManagedNetwork"', checks=[
        ])

        self.cmd('managednetwork delete  --resource-group "myResourceGroup" --name "myManagedNetwork"', checks=[
        ])

        self.cmd('managednetwork delete  --resource-group "myResourceGroup" --name "myManagedNetwork"', checks=[
        ])

# list_by_resource_group -- list
        self.cmd('managednetwork list  --resource-group "myResourceGroup"', checks=[
        ])

        self.cmd('managednetwork list  --resource-group "myResourceGroup"', checks=[
        ])

        self.cmd('managednetwork list  --resource-group "myResourceGroup"', checks=[
        ])

# list_by_subscription -- list
        self.cmd('managednetwork list  --resource-group "myResourceGroup"', checks=[
        ])

        self.cmd('managednetwork list  --resource-group "myResourceGroup"', checks=[
        ])

        self.cmd('managednetwork list  --resource-group "myResourceGroup"', checks=[
        ])

# get -- show
        self.cmd('managednetwork show  --resource-group "myResourceGroup" --name "myManagedNetwork"', checks=[
        ])

        self.cmd('managednetwork show  --resource-group "myResourceGroup" --name "myManagedNetwork"', checks=[
        ])

        self.cmd('managednetwork show  --resource-group "myResourceGroup" --name "myManagedNetwork"', checks=[
        ])

# create_or_update -- create
        self.cmd('managednetwork scope-assignment create  --scope "/subscriptions/{{ subscription_id }}" --name "subscriptionCAssignment"', checks=[
        ])

        self.cmd('managednetwork scope-assignment create  --scope "/subscriptions/{{ subscription_id }}" --name "subscriptionCAssignment"', checks=[
        ])

# create_or_update -- update
        self.cmd('managednetwork scope-assignment update  --scope "/subscriptions/{{ subscription_id }}" --name "subscriptionCAssignment"', checks=[
        ])

        self.cmd('managednetwork scope-assignment update  --scope "/subscriptions/{{ subscription_id }}" --name "subscriptionCAssignment"', checks=[
        ])

# delete -- delete
        self.cmd('managednetwork scope-assignment delete  --scope "/subscriptions/{{ subscription_id }}" --name "subscriptionCAssignment"', checks=[
        ])

        self.cmd('managednetwork scope-assignment delete  --scope "/subscriptions/{{ subscription_id }}" --name "subscriptionCAssignment"', checks=[
        ])

# list -- list
        self.cmd('managednetwork scope-assignment list  --scope "/subscriptions/{{ subscription_id }}"', checks=[
        ])

        self.cmd('managednetwork scope-assignment list  --scope "/subscriptions/{{ subscription_id }}"', checks=[
        ])

# get -- show
        self.cmd('managednetwork scope-assignment show  --scope "/subscriptions/{{ subscription_id }}" --name "subscriptionCAssignment"', checks=[
        ])

        self.cmd('managednetwork scope-assignment show  --scope "/subscriptions/{{ subscription_id }}" --name "subscriptionCAssignment"', checks=[
        ])

# create_or_update -- create
        self.cmd('managednetwork managed-network-group create  --resource-group "myResourceGroup" --managed-network-name "myManagedNetwork" --name "myManagedNetworkGroup1"', checks=[
        ])

        self.cmd('managednetwork managed-network-group create  --resource-group "myResourceGroup" --managed-network-name "myManagedNetwork" --name "myManagedNetworkGroup1"', checks=[
        ])

# create_or_update -- update
        self.cmd('managednetwork managed-network-group update  --resource-group "myResourceGroup" --managed-network-name "myManagedNetwork" --name "myManagedNetworkGroup1"', checks=[
        ])

        self.cmd('managednetwork managed-network-group update  --resource-group "myResourceGroup" --managed-network-name "myManagedNetwork" --name "myManagedNetworkGroup1"', checks=[
        ])

# delete -- delete
        self.cmd('managednetwork managed-network-group delete  --resource-group "myResourceGroup" --managed-network-name "myManagedNetwork" --name "myManagedNetworkGroup1"', checks=[
        ])

        self.cmd('managednetwork managed-network-group delete  --resource-group "myResourceGroup" --managed-network-name "myManagedNetwork" --name "myManagedNetworkGroup1"', checks=[
        ])

# list_by_managed_network -- list
        self.cmd('managednetwork managed-network-group list  --resource-group "myResourceGroup" --managed-network-name "myManagedNetwork"', checks=[
        ])

        self.cmd('managednetwork managed-network-group list  --resource-group "myResourceGroup" --managed-network-name "myManagedNetwork"', checks=[
        ])

# get -- show
        self.cmd('managednetwork managed-network-group show  --resource-group "myResourceGroup" --managed-network-name "myManagedNetwork" --name "myManagedNetworkGroup1"', checks=[
        ])

        self.cmd('managednetwork managed-network-group show  --resource-group "myResourceGroup" --managed-network-name "myManagedNetwork" --name "myManagedNetworkGroup1"', checks=[
        ])

# create_or_update -- create
        self.cmd('managednetwork managed-network-peering-policy create  --resource-group "myResourceGroup" --managed-network-name "myManagedNetwork" --name "myHubAndSpoke"', checks=[
        ])

        self.cmd('managednetwork managed-network-peering-policy create  --resource-group "myResourceGroup" --managed-network-name "myManagedNetwork" --name "myHubAndSpoke"', checks=[
        ])

# create_or_update -- update
        self.cmd('managednetwork managed-network-peering-policy update  --resource-group "myResourceGroup" --managed-network-name "myManagedNetwork" --name "myHubAndSpoke"', checks=[
        ])

        self.cmd('managednetwork managed-network-peering-policy update  --resource-group "myResourceGroup" --managed-network-name "myManagedNetwork" --name "myHubAndSpoke"', checks=[
        ])

# delete -- delete
        self.cmd('managednetwork managed-network-peering-policy delete  --resource-group "myResourceGroup" --managed-network-name "myManagedNetwork" --name "myHubAndSpoke"', checks=[
        ])

        self.cmd('managednetwork managed-network-peering-policy delete  --resource-group "myResourceGroup" --managed-network-name "myManagedNetwork" --name "myHubAndSpoke"', checks=[
        ])

# list_by_managed_network -- list
        self.cmd('managednetwork managed-network-peering-policy list  --resource-group "myResourceGroup" --managed-network-name "myManagedNetwork"', checks=[
        ])

        self.cmd('managednetwork managed-network-peering-policy list  --resource-group "myResourceGroup" --managed-network-name "myManagedNetwork"', checks=[
        ])

# get -- show
        self.cmd('managednetwork managed-network-peering-policy show  --resource-group "myResourceGroup" --managed-network-name "myManagedNetwork" --name "myHubAndSpoke"', checks=[
        ])

        self.cmd('managednetwork managed-network-peering-policy show  --resource-group "myResourceGroup" --managed-network-name "myManagedNetwork" --name "myHubAndSpoke"', checks=[
        ])
