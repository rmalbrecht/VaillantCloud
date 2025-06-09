# VaillantCloud for Home Assistant 

[![GitHub Release](https://img.shields.io/github/release/rmalbrecht/VaillantCloud.svg)](https://github.com/rmalbrecht/VaillantCloud/releases)
[![License](https://img.shields.io/github/license/rmalbrecht/VaillantCloud.svg)](https://github.com/rmalbrecht/VaillantCloud/blob/main/LICENSE)
![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/rmalbrecht/VaillantCloud/build.yml)

This Home Assistant component interfaces with the myVAILLANT API (and branded versions of it, such as the MiGo Link app
from Saunier Duval & Bulex).

<img src="https://github.com/user-attachments/assets/665fd059-7516-42ed-afea-e95c43a70883" width="250">

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
* More are documented in the wiki.

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

# Screenshots
## Heating
<img src="https://github.com/user-attachments/assets/fef8fb96-d122-4244-9301-f7e56585c558" width="250">
## Water
<img src="https://github.com/user-attachments/assets/00d5a8bc-4b1c-4147-8041-f9fcc864d7b1" width="250">
<img src="https://github.com/user-attachments/assets/30d0c8bb-9920-44eb-a6ac-f9b859df9719" width="250">

# Configuration
Please read the [Wiki](https://github.com/rmalbrecht/VaillantCloud/wiki) !

# Vaillant Load Limits
To protect their API Vaillant has employed load limits. While the exact limits are unknown, the more app-installtions you have and the more often Home Assistant polls the information, the faster you will hit the limit. Nothing can be done here. Vaillant might just decline the API calls, or might even ban your whole account. You have been warned!
