
FILESEXTRAPATHS:prepend := "${THISDIR}/files:"

SRC_URI += "file://fby2.conf \
           "

do_install:append() {
    install -d ${D}${sysconfdir}/sensors.d
    install -m 644 ${UNPACKDIR}/fby2.conf ${D}${sysconfdir}/sensors.d/fby2.conf
}
