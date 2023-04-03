# CorpTools

[![CI](https://github.com/pvyParts/allianceauth-corp-tools/actions/workflows/main.yml/badge.svg?branch=master)](https://github.com/pvyParts/allianceauth-corp-tools/actions/workflows/main.yml) [![PyPI version](https://badge.fury.io/py/allianceauth-corptools.svg)](https://badge.fury.io/py/allianceauth-corptools) ![Discord](https://img.shields.io/discord/399006117012832262?label=Support%20Server)

### Lightweight Toolbox of Bits and bobs for todays Eve Group on the go!

This module is the core of the CorpTools Ecosystem, this includes;

- [Invoices](https://github.com/Solar-Helix-Independent-Transport/allianceauth-invoice-manager): Automatic tracking of payments made to a holding wallet.
- [Moons](https://github.com/pvyParts/allianceauth-corp-tools-moons): Moon Mining tracking and Tax system.
- [Indy Dash](https://github.com/pvyParts/allianceauth-corp-tools-indy-dash): What Industrial structures have what rigs and where are they.
- [Pinger](https://github.com/Solar-Helix-Independent-Transport/allianceauth-corp-tools-pinger): High performance pings from the notification endpoint, using the data avaialbe from character audit.

Included `Bits and Bobs`:

- Character Audit

  - Assets
  - Roles
  - Contacts
  - Notifications
  - Standings
  - Markets
  - Skills
    - List
    - Queue
    - Audit/Export
  - Wallet
    - Activity Analysis
  - History
  - Clones
    - Implants

- Corp Audit

  - Wallets
  - Structures
  - Assets

- [Sec Group](https://github.com/Solar-Helix-Independent-Transport/allianceauth-secure-groups) Filters
  - Audit Fully Loaded
  - Assets
    - Location
    - Type
    - Group
  - Skill List
  - Corporate Roles
  - Corporate Title
  - Main time in corp

Active Devs:

- [AaronKable](https://github.com/pvyParts)

## Installation

1.  Install the Repo from git `pip install -U git+https://github.com/pvyParts/allianceauth-corp-tools.git`
2.  Add `'corptools',` to your `INSTALLED_APPS` in your projects `local.py`
3.  run migrations, collectstatic and restart auth
4.  run the corp tools setup managemnt command `python manage.py ct_setup`
5.  setup your perms as documented below
6.  add characters and corp tokens as required.

## Set Corp Tools Name

Add the below lines to your `local.py` settings file, Changing the contexts to yours.

You can optionally se the name of the app in the ui by setting this setting

```python
## name for Corp Tools
CORPTOOLS_APP_NAME = "Character Audit"
```

## Usage

### Seting up automatic updates

This will show how to do daily updates.

Currently this is:

- 2 times an hour ( minute 15, and 45) 1/48th of the total character updates, for at worst 1 update per character per day
- Corp update run on all corps hourly at minute 30

1. Got Audit Admin
2. Click `Create or Update Periodic Tasks`
3. you can edit the schedules to work more inline with your group as required.

## Permissions

There are some basic access perms

All permissions are filtered by main character, if a person has neutral alts loaded they will also be visible to someone who can see their main.

| Perm                | Admin Site | Perm                                                                         | Description                                            |
| ------------------- | ---------- | ---------------------------------------------------------------------------- | ------------------------------------------------------ |
| view_characteraudit | nill       | Can view character audit.                                                    | Generic Access perm to show the Member Audit Menu item |
| global_hr           | nill       | Can access other character's data for characters in any corp/alliance/state. | Superuser level access                                 |
| alliance_hr         | nill       | Can access other character's data for own alliance.                          | Alliance only level access                             |
| corp_hr             | nill       | Can access other character's data for own corp.                              | Corp restricted level access                           |

## Settings

### Modules

Each section of the character audit can be enabled and disabled via settings in your `local.py`

- `True` Enables the module
- `False` Disables the Module

You can also exclude section of hte updates from the "Active" metric, this is handy should you wish to add a module and not have everyone be marked as "Inactive" in the audit module. or if CCP is having issues with part of the ESI. _Looks at Assets_

- `True` Masks the section in the active calculation
- `False` Enforces the section in the active calculation

To assist with auth related tasks we request `publicData` on top of the configured set.

| Module                    | Enable Setting (Default)                 | Active Setting (Default)                               | Description                                     | Scopes Requested                                                                                                           | Note                                  |
| ------------------------- | ---------------------------------------- | ------------------------------------------------------ | ----------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| Assets                    | `CT_CHAR_ASSETS_MODULE` (`True`)         | `CT_CHAR_ACTIVE_IGNORE_ASSETS_MODULE` (`False`)        | Character Assets                                | 'esi-assets.read_assets.v1'                                                                                                | Fully enabled with a Sec Group Filter |
| Standings                 | `CT_CHAR_STANDINGS_MODULE` (`True`)      | `CT_CHAR_ACTIVE_IGNORE_STANDINGS_MODULE` (`False`)     | Character NPC Standings                         | 'esi-characters.read_standings.v1'                                                                                         | Fully enabled                         |
| Killmails                 | `CT_CHAR_KILLMAILS_MODULE` (`True`)      | `CT_CHAR_ACTIVE_IGNORE_KILLMAILS_MODULE` (`False`)     | Character Killmails                             | 'esi-killmails.read_killmails.v1'                                                                                          | Future Version                        |
| Fittings                  | `CT_CHAR_FITTINGS_MODULE` (`True`)       | `CT_CHAR_ACTIVE_IGNORE_FITTINGS_MODULE` (`False`)      | Character Fittings                              | 'esi-fittings.read_fittings.v1'                                                                                            | Future Version                        |
| Calendar                  | `CT_CHAR_CALENDAR_MODULE` (`True`)       | `CT_CHAR_ACTIVE_IGNORE_CALENDAR_MODULE` (`False`)      | Character Killmails                             | 'esi-calendar.read_calendar_events.v1'                                                                                     | Future Version                        |
| Contacts                  | `CT_CHAR_CONTACTS_MODULE` (`True`)       | `CT_CHAR_ACTIVE_IGNORE_CONTACTS_MODULE` (`False`)      | Character Contacts                              | 'esi-characters.read_contacts.v1'                                                                                          | Fully enabled                         |
| Notifications             | `CT_CHAR_NOTIFICATIONS_MODULE` (`True`)  | `CT_CHAR_ACTIVE_IGNORE_NOTIFICATIONS_MODULE` (`False`) | Character Notifications                         | 'esi-characters.read_notifications.v1'                                                                                     | Fully enabled                         |
| Roles                     | `CT_CHAR_ROLES_MODULE` (`True`)          | `CT_CHAR_ACTIVE_IGNORE_ROLES_MODULE` (`False`)         | Character Roles and Titles                      | 'esi-characters.read_titles.v1', 'esi-characters.read_corporation_roles.v1'                                                | Fully enabled with a Sec Group Filter |
| Industry                  | `CT_CHAR_INDUSTRY_MODULE` (`True`)       | `CT_CHAR_ACTIVE_IGNORE_INDUSTRY_MODULE` (`False`)      | Character Indy Jobs                             | 'esi-industry.read_character_jobs.v1'                                                                                      | Fully enabled                         |
| Mining                    | `CT_CHAR_MINING_MODULE` (`True`)         | `CT_CHAR_ACTIVE_IGNORE_MINING_MODULE` (`False`)        | Character Mining Ledgers                        | 'esi-industry.read_character_mining.v1'                                                                                    | Future Version                        |
| Wallets/Markets/Contracts | `CT_CHAR_WALLET_MODULE` (`True`)         | `CT_CHAR_ACTIVE_IGNORE_WALLET_MODULE` (`False`)        | Character Wallets, Contracts and Trading/Orders | 'esi-markets.read_character_orders.v1', 'esi-wallet.read_character_wallet.v1', 'esi-contracts.read_character_contracts.v1' | Fully Enabled                         |
| Skills                    | `CT_CHAR_SKILLS_MODULE` (`True`)         | `CT_CHAR_ACTIVE_IGNORE_SKILLS_MODULE` (`False`)        | Character Skills/Queues and Doctrine Tools      | 'esi-skills.read_skillqueue.v1','esi-skills.read_skills.v1'                                                                | Fully Enabled with Sec Group Filters  |
| Clones                    | `CT_CHAR_CLONES_MODULE` (`True`)         | `CT_CHAR_ACTIVE_IGNORE_CLONES_MODULE` (`False`)        | Character Medical and Jump Clone Module         | 'esi-clones.read_implants.v1', 'esi-clones.read_clones.v1'                                                                 | Fully Enabled with a Sec Group Filter |
| Fleet                     | `CT_CHAR_FLEET_MODULE` (`True`)          | nill                                                   | Character Fleet Tools                           | 'esi-fleets.read_fleet.v1', 'esi-fleets.write_fleet.v1`                                                                    | Future Version                        |
| Mail                      | `CT_CHAR_MAIL_MODULE` (`False`)          | `CT_CHAR_ACTIVE_IGNORE_MAIL_MODULE` (`False`)          | Character Mail Views                            | 'esi-mail.read_mail.v1`                                                                                                    | Fully Enabled                         |
| Helpers                   | `CT_CHAR_HELPER_MODULE` (`False`)        | `CT_CHAR_ACTIVE_IGNORE_HELPER_MODULE` (`False`)        | Character Helpers                               | 'esi-ui.open_window.v1','esi-ui.write_waypoint.v1'                                                                         | Future Versions                       |
| Opportunities             | `CT_CHAR_OPPORTUNITIES` (`False`)        | nill                                                   | Character Opportunities                         | 'esi-characters.read_opportunities.v1'                                                                                     | Future Versions                       |
| Loyalty Points            | `CT_CHAR_LOYALTYPOINTS_MODULE` (`False`) | `CT_CHAR_ACTIVE_IGNORE_LOYALTYPOINTS_MODULE` (`True`)  | Character LP                                    | 'esi-characters.read_loyalty.v1'                                                                                           | Fully Enabled                         |

### Extra Scopes

If `Assets`, `Clones`, `Wallets` or `Minning` are enabled these extra spoces are requested:

- 'esi-universe.read_structures.v1'
- 'esi-search.search_structures.v1'

## Contributing

Make sure you have signed the [License Agreement](https://developers.eveonline.com/resource/license-agreement) by logging in at https://developers.eveonline.com before submitting any pull requests. All bug fixes or features must not include extra superfluous formatting changes.
