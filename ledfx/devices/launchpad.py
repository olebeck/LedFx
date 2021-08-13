import logging
import rtmidi

import numpy as np
import voluptuous as vol

from ledfx.devices import Device

_LOGGER = logging.getLogger(__name__)

try:
    class AvailableMidiPorts:
        ports = rtmidi.MidiOut().get_ports() # pylint: disable=no-member


    class LaunchpadDevice(Device):
        """launchpad midi matrix support"""
        pixel_count = 81

        CONFIG_SCHEMA = vol.Schema(
            {
                vol.Required(
                    "midi_port",
                    description="Midi port for the launchpad"
                ): vol.In(list(AvailableMidiPorts.ports))
            }
        )

        def activate(self):
            self.midi = rtmidi.MidiOut() # pylint: disable=no-member
            available_ports = self.midi.get_ports()
            port_idx = available_ports.index(self._config["midi_port"])
            self.midi.open_port(port_idx)
                    
            if not self.midi.is_port_open():
                _LOGGER.warning(
                    f"Cannot open midi device {self._config['midi_port']}, aborting"
                )
                return
            return super().activate()

        def flush(self, data):
            midiData = bytearray()
            byteData = data.astype(np.dtype("uint8")).reshape((9,9,3)) // 4
            
            for ix, iy in np.ndindex((9,9)):
                led = 11 + (10*iy) + ix
                if iy == 8: led += 13
                midiData += bytearray([0xF0, 0x00, 0x20, 0x29, 0x02, 0x18, 0xB, led, *byteData[iy,ix], 0xF7])
            self.midi.send_message(midiData)
except Exception as e:
    _LOGGER.warning(f"rtmidi not working: {e}, ignoring launchpad support")