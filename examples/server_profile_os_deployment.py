# -*- coding: utf-8 -*-
###
# (C) Copyright [2019] Hewlett Packard Enterprise Development LP
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
###

"""
This module demonstrates a Server Profile creation with an associated i3s OS Deployment Plan.
"""

from pprint import pprint

from config_loader import try_load_from_file
from hpeOneView.oneview_client import OneViewClient

config = {
    "ip": "172.16.101.190",
    "api_version": 300,
    "credentials": {
        "userName": "administrator",
        "password": "",
    }
}

# Try load config from a file (if there is a config file)
config = try_load_from_file(config)

oneview_client = OneViewClient(config)

# To run this sample, you must define the values in the following dictionary:
example_settings = {
    "serverHardwareUri": "/rest/server-hardware/30303437-3034-4D32-3230-313131324752",
    "serverHardwareTypeUri": "/rest/server-hardware-types/1D1DB02A-2A57-4934-862B-B74E7832EBC2",
    "enclosureGroupUri": "/rest/enclosure-groups/184736fb-c64b-420f-b73f-ed62a9d9ea43",
    "networkUri": "/rest/ethernet-networks/062ff757-6ddd-47b4-b5c9-634498b85823",
    "osDeploymentPlanUri": "/rest/os-deployment-plans/81decf85-0dff-4a5e-8a95-52994eeb6493",
    "osDeploymentHostname": "examplehostname",
}

server_profile_creation_info = {
    "type": "ServerProfileV6",
    "serverHardwareUri": example_settings["serverHardwareUri"],
    "serverHardwareTypeUri": example_settings["serverHardwareTypeUri"],
    "enclosureGroupUri": example_settings["enclosureGroupUri"],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": "sp2",
    "description": "i3s deployment plan (for example)",
    "affinity": "Bay",
    "connections": [
        {
            "id": 1,
            "name": "Deployment Network A",
            "functionType": "Ethernet",
            "portId": "Mezz 3:1-a",
            "requestedMbps": "2500",
            "networkUri": example_settings["networkUri"],
            "boot": {
                "priority": "Primary",
                "initiatorNameSource": "ProfileInitiatorName",
                "firstBootTargetIp": None,
                "secondBootTargetIp": "",
                "secondBootTargetPort": "",
                "initiatorName": None,
                "initiatorIp": None,
                "bootTargetName": None,
                "bootTargetLun": None
            },
            "mac": None,
            "wwpn": "",
            "wwnn": "",
            "requestedVFs": "Auto"
        },
        {
            "id": 2,
            "name": "Deployment Network B",
            "functionType": "Ethernet",
            "portId": "Mezz 3:2-a",
            "requestedMbps": "2500",
            "networkUri": example_settings["networkUri"],
            "boot": {
                "priority": "Secondary",
                "initiatorNameSource": "ProfileInitiatorName",
                "firstBootTargetIp": None,
                "secondBootTargetIp": "",
                "secondBootTargetPort": "",
                "initiatorName": None,
                "initiatorIp": None,
                "bootTargetName": None,
                "bootTargetLun": None
            },
            "mac": None,
            "wwpn": "",
            "wwnn": "",
            "requestedVFs": "Auto"
        }
    ],
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk"
        ]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFIOptimized",
        "pxeBootPolicy": "Auto"
    },
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": "",
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": []
    },
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": {
        "osDeploymentPlanUri": example_settings["osDeploymentPlanUri"],
        "osCustomAttributes": [
            {
                "name": "hostname",
                "value": example_settings["osDeploymentHostname"]
            }
        ],
        "osVolumeUri": None
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": None
}

# Create a server profile
print("Create a Server Profile with associated OS Deployment")
basic_profile = oneview_client.server_profiles.create(server_profile_creation_info)
pprint(basic_profile)