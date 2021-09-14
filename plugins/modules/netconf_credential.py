#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: netconf_credential
short_description: Resource module for Netconf Credential
description:
- Manage operations create and update of the resource Netconf Credential.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  comments:
    description: Netconf Credential's comments.
    type: str
  credentialType:
    description: Netconf Credential's credentialType.
    type: str
  description:
    description: Netconf Credential's description.
    type: str
  id:
    description: Netconf Credential's id.
    type: str
  instanceTenantId:
    description: Netconf Credential's instanceTenantId.
    type: str
  instanceUuid:
    description: Netconf Credential's instanceUuid.
    type: str
  netconfPort:
    description: Netconf Credential's netconfPort.
    type: str
  payload:
    description: Netconf Credential's payload.
    suboptions:
      comments:
        description: Netconf Credential's comments.
        type: str
      credentialType:
        description: Netconf Credential's credentialType.
        type: str
      description:
        description: Netconf Credential's description.
        type: str
      id:
        description: Netconf Credential's id.
        type: str
      instanceTenantId:
        description: Netconf Credential's instanceTenantId.
        type: str
      instanceUuid:
        description: Netconf Credential's instanceUuid.
        type: str
      netconfPort:
        description: Netconf Credential's netconfPort.
        type: str
    type: list
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Netconf Credential reference
  description: Complete reference of the Netconf Credential object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Update all
  cisco.dnac.netconf_credential:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    comments: string
    credentialType: string
    description: string
    id: string
    instanceTenantId: string
    instanceUuid: string
    netconfPort: string

- name: Create
  cisco.dnac.netconf_credential:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    comments: string
    credentialType: string
    description: string
    id: string
    instanceTenantId: string
    instanceUuid: string
    netconfPort: string

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "taskId": "string",
        "url": "string"
      },
      "version": "string"
    }
"""
