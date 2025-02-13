# Copyright 2015-present Facebook. All Rights Reserved.

FILESEXTRAPATHS:prepend := "${THISDIR}/files:"
LOCAL_URI += " \
    file://setup-ipmbd.sh \
    file://run-ipmbd_1.sh \
    file://run-ipmbd_3.sh \
    file://run-ipmbd_5.sh \
    file://run-ipmbd_7.sh \
    file://run-ipmbd_13.sh \
    "
DEPENDS:append = " plat-utils "

CFLAGS:prepend = " -DCONFIG_FBY2 -DTIMEOUT_IPMB=3"

do_install:append() {
  install -d ${D}${sysconfdir}/init.d
  install -d ${D}${sysconfdir}/rcS.d
  install -d ${D}${sysconfdir}/sv
  install -d ${D}${sysconfdir}/sv/ipmbd_1
  install -d ${D}${sysconfdir}/sv/ipmbd_3
  install -d ${D}${sysconfdir}/sv/ipmbd_5
  install -d ${D}${sysconfdir}/sv/ipmbd_7
  install -d ${D}${sysconfdir}/sv/ipmbd_13
  install -d ${D}${sysconfdir}/ipmbd_1
  install -d ${D}${sysconfdir}/ipmbd_3
  install -d ${D}${sysconfdir}/ipmbd_5
  install -d ${D}${sysconfdir}/ipmbd_7
  install -d ${D}${sysconfdir}/ipmbd_13
  install -m 755 ${UNPACKDIR}/setup-ipmbd.sh ${D}${sysconfdir}/init.d/setup-ipmbd.sh
  install -m 755 ${UNPACKDIR}/run-ipmbd_1.sh ${D}${sysconfdir}/sv/ipmbd_1/run
  install -m 755 ${UNPACKDIR}/run-ipmbd_3.sh ${D}${sysconfdir}/sv/ipmbd_3/run
  install -m 755 ${UNPACKDIR}/run-ipmbd_5.sh ${D}${sysconfdir}/sv/ipmbd_5/run
  install -m 755 ${UNPACKDIR}/run-ipmbd_7.sh ${D}${sysconfdir}/sv/ipmbd_7/run
  install -m 755 ${UNPACKDIR}/run-ipmbd_13.sh ${D}${sysconfdir}/sv/ipmbd_13/run
  update-rc.d -r ${D} setup-ipmbd.sh start 65 5 .
}
