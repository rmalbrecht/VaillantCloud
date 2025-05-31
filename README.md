# VaillantCloud for Home Assistant 

[![GitHub Release](https://img.shields.io/github/release/rmalbrecht/VaillantCloud.svg)](https://github.com/rmalbrecht/VaillantCloud/releases)
[![License](https://img.shields.io/github/license/rmalbrecht/VaillantCloud.svg)](https://github.com/rmalbrecht/VaillantCloud/blob/main/LICENSE)
![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/rmalbrecht/VaillantCloud/build.yml)

This Home Assistant component interfaces with the myVAILLANT API (and branded versions of it, such as the MiGo Link app
from Saunier Duval & Bulex).

![VaillantCloud](https://github.com/user-attachments/assets/665fd059-7516-42ed-afea-e95c43a70883)

> [!WARNING] 
> This integration is not affiliated with Vaillant, the developers take no responsibility for anything that happens to
> your devices because of this library.

> [!IMPORTANT] 
> This integration uses the API which is developed by Vaillant for it's myVaillant App. The API therefore supports only what the app needs.
> If an information is not present in the app, it will also not be present in the API.
> If a function is not supported by the app, it will also not be supported in the API.
> This API is not scoped for smart home control, ... 

> [!NOTE]
> There are many many different setups and products from Vaillant. Without manufacturer documentation or support it's impossible to test every single installation.
> If something is not working in your installation: happy to accept a pull request with the fix. Otherwise, not much can be done.


# Tested Setups

* Vaillant aroTHERM plus heatpump + sensoCOMFORT VRC 720 + sensoNET VR 921
* Vaillant ECOTEC PLUS boiler + VR940F + sensoCOMFORT
* Vaillant ECOTEC PLUS boiler + VRT380f + sensoNET
* Vaillant EcoCompact VSC206 4-5 boiler + Multimatic VRC700/6 + gateway VR920
* Saunier Duval DUOMAX F30 90 + MISET Radio + MiLink V3
* VR42 controllers are also supported
* [More are documented here](https://github.com/rmalbrecht/VaillantCloud/wiki#tested-setups)

# Features

* Supports climate & hot water controls, as well as sensor information
* Control operating modes, target temperature, and presets such as holiday more or quick veto
* Set the schedule for climate zones, water heaters, and circulation pumps
  with a custom service  
* Track sensor information of devices, such as temperature, humidity, operating mode, energy usage, or energy efficiency
* See diagnostic information, such as the current heating curve, flow temperature, firmware versions, or water pressure
* Custom services to set holiday mode or quick veto temperature overrides, and their duration

# Installation

1. [Install HACS](https://hacs.xyz/docs/setup/download)
2. Search for the myVAILLANT integration in HACS and install it
3. Restart Home Assistant
4. [Add VaillantCloud integration](https://my.home-assistant.io/redirect/config_flow_start/?domain=myVaillant)
5. Sign in with the email & password you used in the myVAILLANT app (or MiGo app for Saunier Duval)

# Options

## Seconds between scans

Wait interval between updating (most) sensors. **Don't set this too low, for example 10 leads to quota exceeded errors
and a temporary ban**.

The energy data and efficiency sensors have a fixed hourly interval.

## Delay before refreshing data after updates

How long to wait between making a request (i.e. setting target temperature) and refreshing data.
The Vaillant takes some time to return the updated values.

## Default duration in hours for quick veto

When setting the temperature with the climate controls, the integration uses the "quick veto" feature of the myVAILLANT
app.

With this option you can set for how long the temperature should stay set, before returning to the default value.

## Default duration in days for away mode

When the away mode preset is activated, this duration is used to for the end date (default is 365 days).

## Temperature controls overwrite time program instead of setting quick veto

When raising or lowering the desired temperature in the myVAILLANT app, it sets a quick veto mode for a limited time
with that new temperature, if the zone is in time controlled mode. If you want to permanently change the desired
temperature, you need to update the time schedule.

By default, this integration has the same behavior. But when enabling this option, the Home Assistant climate controls
instead overwrite the temperatures set in the time schedule with the new value (unless quick veto is already active).

## Country

The country you registered your myVAILLANT account in. The list of options is limited to known supported countries.

## Brand

Brand of your HVAC equipment and app, pick Saunier Duval if you use the MiGo Link app.

# Known Issues

## Lack of Test Data for Different Systems

Your HVAC system might differ from the ones in `Tested on` above.
If you don't see any entities, or get an error during setup, please check `Debugging` below and create an issue.
With debugging enabled, there's a chance to find the culprit in the data returned by the myVAILLANT API and fix it.

## Vaillant Load Limits

To protect their API Vaillant has employed load limits. While the exact limits are unknown, the more app-installtions you have and the more often Home Assistant polls the information, the faster you will hit the limit. Nothing can be done here. Vaillant might just decline the API calls, or might eben ban your whole account. You have been warned!

# Debugging

When debugging or reporting issues, turn on debug logging by adding this to your `configuration.yaml`
and restarting Home Assistant:

```yaml
logger:
  default: warning
  logs:
    custom_components.vaillantcloud: debug
    myVaillant: debug
```
# Screenshots

## Heating

![Bildschirmfoto 2025-05-31 um 21 25 17](https://github.com/user-attachments/assets/fef8fb96-d122-4244-9301-f7e56585c558)

<img src="github.com/user-attachments/assets/fef8fb96-d122-4244-9301-f7e56585c558" width="250">

## Water

![Bildschirmfoto 2025-05-31 um 21 26 07](https://github.com/user-attachments/assets/00d5a8bc-4b1c-4147-8041-f9fcc864d7b1)

![Bildschirmfoto 2025-05-31 um 21 27 37](https://github.com/user-attachments/assets/30d0c8bb-9920-44eb-a6ac-f9b859df9719)
