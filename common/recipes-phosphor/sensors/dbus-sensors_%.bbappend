FILESEXTRAPATHS:prepend := "${THISDIR}/${PN}:"

SRC_URI:append = " \
    file://0001-PSUSensor-add-ina233-support.patch \
    file://0002-PSUSensor-add-adm1281-support.patch \
    file://0003-psusensor-avoid-crash-by-activate-sensor-twice.patch \
    file://0004-PwmSensor-Fix-function-getValue-returns-wrong-data-t.patch \
    file://0005-PSUSensor-Fix-error-for-decimal-part-of-scalefactor.patch \
"
