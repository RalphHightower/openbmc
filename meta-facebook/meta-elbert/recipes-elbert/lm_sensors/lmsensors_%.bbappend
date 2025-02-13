
FILESEXTRAPATHS:prepend := "${THISDIR}/files:"

SRC_URI += "file://elbert.conf \
            file://pim16q.conf \
            file://pim16q2.conf \
            file://pim8ddm.conf \
           "

do_install:append() {
    install -d ${D}${sysconfdir}/sensors.d
    install -m 644 ${UNPACKDIR}/elbert.conf ${D}${sysconfdir}/sensors.d/elbert.conf
    install -m 644 ${UNPACKDIR}/pim16q.conf ${D}${sysconfdir}/sensors.d/.pim16q.conf
    install -m 644 ${UNPACKDIR}/pim16q2.conf ${D}${sysconfdir}/sensors.d/.pim16q2.conf
    install -m 644 ${UNPACKDIR}/pim8ddm.conf ${D}${sysconfdir}/sensors.d/.pim8ddm.conf
}
