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

        self.cmd('az peering service create --resource-group "MyResourceGroup" --name "MyPeeringService"', checks=[
        ])

        self.cmd('az peering service prefix create --resource-group "MyResourceGroup" --peering-service-name "MyPeeringService" --name "MyPeeringServicePrefix"', checks=[
        ])

        self.cmd('az peering service prefix delete --resource-group "MyResourceGroup" --peering-service-name "MyPeeringService" --name "MyPeeringServicePrefix"', checks=[
        ])

        self.cmd('az peering service delete --resource-group "MyResourceGroup" --name "MyPeeringService"', checks=[
        ])
