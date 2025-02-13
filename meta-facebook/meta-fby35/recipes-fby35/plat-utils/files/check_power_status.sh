#! /bin/bash
#
# Copyright 2023-present Facebook. All Rights Reserved.
#
# This program file is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; version 2 of the License.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
# for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program in a file named COPYING; if not, write to the
# Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA
#
echo "check power status"

. /usr/local/fbpackages/utils/ast-functions

for i in $(seq 1 4)
do
  if [ "$(is_server_prsnt $i)" = "1" ] && [ "$(is_slot_12v_on $i)" == "0" ]; then
    echo "detect slot$i is 12V-off, turn it to 12V-on"
    power-util slot$i 12V-on
  fi
done
