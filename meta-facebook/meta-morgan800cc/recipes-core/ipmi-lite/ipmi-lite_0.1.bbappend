RDEPENDS:${PN} += "libipmi libkv"

FILESEXTRAPATHS:prepend := "${THISDIR}/files:"
LOCAL_URI += "\ 
    file://config.json \
    "

do_install:append() {
    install -m 644 ${UNPACKDIR}/config.json ${dst}/config.json
}

