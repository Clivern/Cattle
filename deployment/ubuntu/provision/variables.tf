# Copyright 2021 Clivern
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

variable do_token {
    type = string
    description = "Digitalocean API Token"
}

variable "ssh_key" {
    type = string
    default = "clivern"
    description = "Digitalocean Account SSH Key Name"
}

variable "region" {
    type    = string
    default = "nyc3"
    description = "Digitalocean Region"
}

variable "name" {
    type = string
    default = "cattle.sh"
    description = "Server Name"
}

variable "droplet_size" {
    type = string
    default = "s-1vcpu-2gb"
    description = "Server Size"
}

variable "image" {
    type = string
    default = "ubuntu-20-04-x64"
    description = "Server Image"
}
