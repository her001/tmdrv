# [tmdrv](https://github.com/her001/tmdrv)

Copyright © 2016, 2017 Andrew "HER0" Conrad

**tmdrv** initializes some Thrustmaster racing wheels as a standard HID device.

This allows the wheels to be used in operating systems which are not officially
supported, though it likely only works on Linux. Note that tmdrv does not enable
force feedback. The eventual goal, and one I'll need help with, is to get these
devices supported in the Linux kernel, including force feedback support.

tmdrv is made available under the terms of the GNU GPL version 3. See `COPYING`
for details.

### Supported Devices

* Thrustmaster T500RS
* Thrustmaster TX


## Requirements

* [Python 3](https://www.python.org)
* [python-libusb1](https://pypi.python.org/pypi/libusb1)
* jscal (from [Linux Console](https://sourceforge.net/projects/linuxconsole),
for calibration)

The USB device files must be readable and writeable. I recommend setting a udev
rule for this.

## Usage

After plugging in your device, run `./tmdrv.py -d $device_name` from the source
tree. A list of valid device names can be found with `./tmdrv.py -D`.

For more information, try `./tmdrv.py --help`.

## Contributing

Issues or pull requests can be filed on the GitHub
[issue tracker](https://github.com/her001/tmdrv/issues).

### Adding support for new devices

Other wheels which use the same method for initialization can be added to tmdrv
relatively easily. If you have a device that you think will work, file an issue
with the following information:

* The name of the device (e.g. Thrustmaster TX)
* The vendor and product USB IDs (e.g. 044f:b65d)
* A USB capture between the Windows driver and the device
(such as with [USBPcap](http://desowin.org/usbpcap) on Windows or a Virtual
Machine on Linux and [Wireshark](https://wiki.wireshark.org/CaptureSetup/USB))

If it is determined that your device can be added to tmdrv, you will need to
test the support and provide a jscal preset (for eliminating deadzones).

