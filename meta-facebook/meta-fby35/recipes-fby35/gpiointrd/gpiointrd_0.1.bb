# Copyright 2015-present Facebook. All Rights Reserved.
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

SUMMARY = "GPIO Monitoring Daemon"
DESCRIPTION = "Daemon for monitoring the gpio signals"
SECTION = "base"
PR = "r1"
LICENSE = "GPL-2.0-or-later"
LIC_FILES_CHKSUM = "file://gpiointrd.c;beginline=4;endline=16;md5=b395943ba8a0717a83e62ca123a8d238"

S="${WORKDIR}/sources"
UNPACKDIR="${S}"

LOCAL_URI = " \
    file://meson.build \
    file://gpiointrd.c \
    file://setup-gpiointrd.sh \
    file://run-gpiointrd.sh \
    file://server-init.sh \
    "

inherit meson pkgconfig
inherit legacy-packages

pkgdir = "gpiointrd"

DEPENDS += "\
    libbic \
    libfby35-common \
    libfby35-gpio \
    libgpio-ctrl \
    libipmi \
    libkv \
    libobmc-i2c \
    libpal \
    libras \
    update-rc.d-native \
"
RDEPENDS:${PN} += "bash"
CFLAGS += " -DCONFIG_FBY3 "


do_install:append() {
  install -d ${D}${sysconfdir}/sv
  install -d ${D}${sysconfdir}/sv/gpiointrd
  install -d ${D}${sysconfdir}/init.d
  install -d ${D}${sysconfdir}/rcS.d
  install -m 755 ${UNPACKDIR}/server-init.sh ${D}${sysconfdir}/init.d/server-init.sh
  install -m 755 ${UNPACKDIR}/setup-gpiointrd.sh ${D}${sysconfdir}/init.d/setup-gpiointrd.sh
  install -m 755 ${UNPACKDIR}/run-gpiointrd.sh ${D}${sysconfdir}/sv/gpiointrd/run
  update-rc.d -r ${D} setup-gpiointrd.sh start 91 5 .
}

