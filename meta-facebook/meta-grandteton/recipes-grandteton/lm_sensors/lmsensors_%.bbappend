#

FILESEXTRAPATHS:prepend := "${THISDIR}/files:"

SRC_URI += "file://common.conf \
            file://cover.conf \
            file://evt.conf \
            file://evt2.conf \
            file://hpdb-adm1272-1.conf \
            file://hpdb-adm1272-2.conf \
            file://vpdb-adm1272-1.conf \
            file://vpdb-adm1272-2.conf \
            file://gt-medusa.conf \
            file://gt-hnext-medusa.conf \
           "

FILES:${PN}-libsensors += "${sysconfdir}/sensors_cfg"


do_install:append() {
    install -d ${D}${sysconfdir}/sensors_cfg
    install -d ${D}${sysconfdir}/sensors.d
    install -m 644 ${UNPACKDIR}/common.conf ${D}${sysconfdir}/sensors.d/common.conf
    install -m 644 ${UNPACKDIR}/cover.conf ${D}${sysconfdir}/sensors.d/cover.conf
    install -m 644 ${UNPACKDIR}/evt.conf   ${D}${sysconfdir}/sensors_cfg/evt.conf
    install -m 644 ${UNPACKDIR}/evt2.conf ${D}${sysconfdir}/sensors_cfg/evt2.conf
    install -m 644 ${UNPACKDIR}/hpdb-adm1272-1.conf ${D}${sysconfdir}/sensors_cfg/hpdb-adm1272-1.conf
    install -m 644 ${UNPACKDIR}/hpdb-adm1272-2.conf ${D}${sysconfdir}/sensors_cfg/hpdb-adm1272-2.conf
    install -m 644 ${UNPACKDIR}/vpdb-adm1272-1.conf ${D}${sysconfdir}/sensors_cfg/vpdb-adm1272-1.conf
    install -m 644 ${UNPACKDIR}/vpdb-adm1272-2.conf ${D}${sysconfdir}/sensors_cfg/vpdb-adm1272-2.conf
    install -m 644 ${UNPACKDIR}/gt-medusa.conf ${D}${sysconfdir}/sensors_cfg/gt-medusa.conf
    install -m 644 ${UNPACKDIR}/gt-hnext-medusa.conf ${D}${sysconfdir}/sensors_cfg/gt-hnext-medusa.conf
}
