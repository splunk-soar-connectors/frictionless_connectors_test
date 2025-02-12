# File: frictionlessconnectors_consts.py
#
# Copyright (c) 2025 Splunk Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific language governing permissions
# and limitations under the License.

HEADERS = {"Accept": "application/json"}
STATE_FILE_CORRUPT_ERR = "Error occurred while loading the state file due to its unexpected format"
DEFAULT_REQUEST_TIMEOUT = 30  # in seconds
GET_HOSTS_ENDPOINT = "/api/fmc_config/v1/domain/{domain_id}/object/hosts"
NETWORK_OBJECTS_ENDPOINT = "/api/fmc_config/v1/domain/{domain_id}/object/{type}"
OBJECT_TYPES = ["Network", "Host", "Range"]
CLOUD_HOST = "edge.{region}.cdo.cisco.com/api/rest/v1/cdfmc"
