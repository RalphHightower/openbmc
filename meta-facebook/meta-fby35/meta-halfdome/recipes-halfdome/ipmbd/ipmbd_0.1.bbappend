# Copyright 2015-present Facebook. All Rights Reserved.

FILESEXTRAPATHS:prepend := "${THISDIR}/files:"
LOCAL_URI += " \
    file://setup-ipmbd.sh \
    file://run-ipmbd_0.sh \
    file://run-ipmbd_1.sh \
    file://run-ipmbd_2.sh \
    file://run-ipmbd_3.sh \
    "

do_install:append() {
  install -d ${D}${sysconfdir}/init.d
  install -d ${D}${sysconfdir}/rcS.d
  install -d ${D}${sysconfdir}/sv
  install -d ${D}${sysconfdir}/sv/ipmbd_0
  install -d ${D}${sysconfdir}/sv/ipmbd_1
  install -d ${D}${sysconfdir}/sv/ipmbd_2
  install -d ${D}${sysconfdir}/sv/ipmbd_3
  install -m 755 ${UNPACKDIR}/setup-ipmbd.sh ${D}${sysconfdir}/init.d/setup-ipmbd.sh
  install -m 755 ${UNPACKDIR}/run-ipmbd_0.sh ${D}${sysconfdir}/sv/ipmbd_0/run
  install -m 755 ${UNPACKDIR}/run-ipmbd_1.sh ${D}${sysconfdir}/sv/ipmbd_1/run
  install -m 755 ${UNPACKDIR}/run-ipmbd_2.sh ${D}${sysconfdir}/sv/ipmbd_2/run
  install -m 755 ${UNPACKDIR}/run-ipmbd_3.sh ${D}${sysconfdir}/sv/ipmbd_3/run
  update-rc.d -r ${D} setup-ipmbd.sh start 65 5 .
}

