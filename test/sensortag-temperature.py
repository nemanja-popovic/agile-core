#!/usr/bin/env python3
#-------------------------------------------------------------------------------
# Copyright (C) 2017 Create-Net / FBK.
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Eclipse Public License v1.0
# which accompanies this distribution, and is available at
# http://www.eclipse.org/legal/epl-v10.html
# 
# Contributors:
#     Create-Net / FBK - initial API and implementation
#-------------------------------------------------------------------------------

# --- Imports -----------
import sys
import time
import dbus
# -----------------------

# DBus
PM_BUS_NAME = "iot.agile.ProtocolManager"
PM_OBJ_PATH = "/iot/agile/ProtocolManager"
DM_BUS_NAME = "iot.agile.DeviceManager"
DM_OBJ_PATH = "/iot/agile/DeviceManager"
D_BUS_NAME = "iot.agile.Device"
D_OBJ_PATH = "/iot/agile/Device"


# --- Main program ------
if __name__ == "__main__":

   global protocol_manager
   global device_manager

   # DBus
   session_bus = dbus.SessionBus()
   dbusdm = session_bus.get_object(DM_BUS_NAME, DM_OBJ_PATH)
   device_manager = dbus.Interface(dbusdm, dbus_interface=DM_BUS_NAME)

   for sensortag in device_manager.devices():
     print (sensortag["conn"])
     print (sensortag["path"])
     dbusd = session_bus.get_object(sensortag["conn"], sensortag["path"])
     device = dbus.Interface(dbusd, dbus_interface=sensortag["conn"])
     try:
       print(device.Read('Temperature'))
     except dbus.exceptions.DBusException as e:
       print(e)

