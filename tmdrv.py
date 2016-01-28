#!/usr/bin/env python

# tmdrv is a tool to initialize Thrustmaster racing wheels
# Copyright 2016 Andrew Conrad
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.	See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import usb1
import tmdrv_devices
from time import sleep

def initialize(device=tmdrv_devices.thrustmaster_tx):
	# Send all control packets for initialization
	for m in device.control:
		try:
			_control_init(
				device.idVendor, device.idProduct[m['step'] - 1],
				m['request_type'],
				m['request'],
				m['value'],
				m['index'],
				m['data'],
			)
		except usb1.USBErrorPipe:
			# This is caught when device switches modes
			pass
		# If there are remaining steps, give device time to switch
		if m['step'] < len(m): sleep(1)

def _control_init(idVendor, idProduct, request_type, request, value, index, data):
	context = usb1.USBContext()
	handle = context.openByVendorIDAndProductID(
		idVendor, idProduct,
		skip_on_error=True,
	)
	if handle is None:
		print('Device ' + idVendor + ', ' + idProduct + ' not found or wrong permissions')
		return
	handle.seAutoDetachKernelDriver(true)
	handle.claimInterface(0)
	
	# Send control packet that will switch modes
	handle.controlWrite(
		0x41,
		83,
		0x0001,
		0x0000,
		b'',
	)

if __name__ == '__main__':
	initialize()
