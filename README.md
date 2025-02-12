# Frictionless Connectors Test

Publisher: Splunk \
Connector Version: 1.0.6 \
Product Vendor: Splunk \
Product Name: Frictionless Connectors Test \
Minimum Product Version: 6.3.0

To test changes to CI/CD. using cisco secure firewalls actions

### Configuration variables

This table lists the configuration variables required to operate Frictionless Connectors Test. These variables are specified when configuring a Frictionless Connectors Test asset in Splunk SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**api_key** | optional | password | Api key for cloud delivered FMC |
**region** | optional | string | Region your Cisco Security Cloud Control is deployed in |

### Supported Actions

[test connectivity](#action-test-connectivity) - Validate the asset configuration for connectivity using supplied configuration \
[list network objects](#action-list-network-objects) - List network object in FMC

## action: 'test connectivity'

Validate the asset configuration for connectivity using supplied configuration

Type: **test** \
Read only: **True**

#### Action Parameters

No parameters are required for this action

#### Action Output

No Output

## action: 'list network objects'

List network object in FMC

Type: **investigate** \
Read only: **True**

#### Action Parameters

PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**name** | optional | Network object name to filter results by | string | |
**type** | optional | Network object type to filter results by | string | |
**domain_name** | optional | Firepower Domain. If none is specified the default domain will be queried | string | |

#### Action Output

DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string | | success failed |
action_result.message | string | | |
summary.total_objects | numeric | | |
summary.total_objects_successful | numeric | | |
action_result.parameter.name | string | | |
action_result.parameter.type | string | | Network |
action_result.parameter.domain_name | string | | |
action_result.data.\*.id | string | | |
action_result.data.\*.name | string | | |
action_result.data.\*.type | string | | Network |
action_result.data.\*.links.self | string | | |
action_result.data.\*.links.parent | string | | |

______________________________________________________________________

Auto-generated Splunk SOAR Connector documentation.

Copyright 2025 Splunk Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
