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
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import usb1
from time import sleep

def initialize():
	# Switch from initial state to transitory state
	try:
		_init_one()
	except Exception:
		pass
	
	sleep(1)
	
	# Switch from transitory state to full HID
	try:
		_init_two()
	except Exception:
		pass

def _init_one():
	context = usb1.USBContext()
	handle = context.openByVendorIDAndProductID(
			0x044f, 0xb664,
			skip_on_error=True,
	)
	if handle is None:
		print("Uninitialized Thrustmaster TX not found")
	handle.claimInterface(0)
	
	handle.controlWrite(0x41,
			83,
			0x0001,
			0x0000,
			b'',
	)

def _init_two():
	context = usb1.USBContext()
	handle = context.openByVendorIDAndProductID(
			0x044f, 0xb65d,
			skip_on_error=True,
	)
	if handle is None:
		print("Second stage device not found")
	handle.detachKernelDriver(0)
	handle.claimInterface(0)
	
	handle.controlWrite(0x41,
			83,
			0x0004,
			0x0000,
			b'',
	)

if __name__ == '__main__':
	initialize()
