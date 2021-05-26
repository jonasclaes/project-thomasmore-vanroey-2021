# Services
In order for everything to function after a reboot, use has been made of Systemd services. There are in total 2 services running on the Raspberry Pi. These are critical for functioning correctly.
* Controls
* Webserver

## Controls
The `controls.service` service is required for the reading and processing of inputs as well as reporting them to the webserver. When this service is not running, the interactive wall will not respond to any inputs, and the active webpage will not change.

[controls.service](https://raw.githubusercontent.com/jonasclaes/project-thomasmore-vanroey-2021/master/systemd/controls.service ':include :type=code ini')

## Webserver
The `webserver.service` service is a core component required for running the webapp, as well as a `Socket.IO` server. The socket server is required for the communication between the browser and the controls program. If this service is not running, there will be no connectivity between the browser and the physical buttons. The browser won't be able to display anything since it's server is not running.

[webserver.service](https://raw.githubusercontent.com/jonasclaes/project-thomasmore-vanroey-2021/master/systemd/webserver.service ':include :type=code ini')