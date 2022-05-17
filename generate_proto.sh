#!/bin/bash
# Copyright 2021 dfuse Platform Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

curl -L -O https://github.com/streamingfast/substreams-playground/releases/download/v0.5.0/pcs-v0.5.0.spkg
PKG=./pcs-v0.5.0.spkg

CMD="python3 -m grpc_tools.protoc --descriptor_set_in=$PKG --python_out=. --grpc_python_out=."

$CMD sf/substreams/v1/substreams.proto
$CMD sf/substreams/v1/package.proto
$CMD sf/substreams/v1/modules.proto
$CMD sf/substreams/v1/clock.proto
$CMD pcs/v1/pcs.proto
$CMD codec_eth.proto
