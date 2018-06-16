# [tmdrv](https://gitlab.com/her0/tmdrv)

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
* Thrustmaster TMX

See the status of additional devices on the GitLab
[board](https://gitlab.com/her0/tmdrv/boards?=&label_name[]=new%20device).

## Requirements

* [Python 3](https://www.python.org)
* [python-libusb1](https://pypi.python.org/pypi/libusb1) (must work with your Python 3 install)
* jscal (from [Linux Console](https://sourceforge.net/projects/linuxconsole),
for calibration)


The USB device files must be readable and writeable. I recommend setting a udev
rule for this.

## Usage

After plugging in your device, run `./tmdrv.py -d $device_name` from the source
tree. A list of valid device names can be found with `./tmdrv.py -D`.

For more information, try `./tmdrv.py --help`.

## Contributing

By participating in tmdrv, you agree to the terms set forth by the
Contributor Covenant. See `CODE_OF_CONDUCT.md` for details.

Issues or pull requests can be filed on the GitLab
[issue tracker](https://gitlab.com/her0/tmdrv/issues).

### Adding support for new devices

Other wheels which use the same method for initialization can be added to tmdrv
relatively easily. If you have a device that you think will work, please file an
issue (or add to the existing issue for your device, if it
[already exists](https://gitlab.com/her0/tmdrv/issues?label_name%5B%5D=new+device)) with the
following information:

* The name of the device (e.g. Thrustmaster TX)
* The vendor and product USB IDs (e.g. 044f:b65d)
* A USB capture between the Windows driver and the device
(such as with [USBPcap](http://desowin.org/usbpcap) on Windows or a Virtual
Machine on Linux and [Wireshark](https://wiki.wireshark.org/CaptureSetup/USB))

If it is determined that your device can be added to tmdrv, it would be helpful
to test the support and provide a jscal preset (for eliminating deadzones).

In the case that you are having trouble providing all the requested information,
please feel free to open an issue with that which you do know, and I will do my
best to walk you through providing the rest.

#### Possible signs that your Thrustmaster wheel can be added to tmdrv

tmdrv uses a very simple and specific method of sending a message to the wheel
which switches it to various modes. These modes may be the same for each one,
so the following is my observations of the patterns, but it is possible that
some devices have different behaviors or that I am wrong:

* Supports a console and PC via USB connection
* Relatively recent (possibly only Playstation 4 and Xbox One supporting wheels)

##### Playstation 4 wheels when plugged in to a Linux machine

* USB product ID of `b65d`
* Device name of `Thrustmaster FFB Wheel`
* Appears as a working joystick, but the configuration is incorrect,
including buttons wrongly assigned and pedals acting as buttons

##### Xbox One wheels when plugged in to a Linux machine

* USB product ID is **not** `b65d` (probably)
* Does not show as an HID device of any sort, not found in
joystick-supporting software

With more data, these guidelines can almost definitely be made more accurate,
but I've only seen limited information on a few devices!

