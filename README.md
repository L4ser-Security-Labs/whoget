# WhoGet

```txt
 █████   ███   █████ █████                 █████████            █████
░░███   ░███  ░░███ ░░███                 ███░░░░░███          ░░███
 ░███   ░███   ░███  ░███████    ██████  ███     ░░░   ██████  ███████  
 ░███   ░███   ░███  ░███░░███  ███░░███░███          ███░░███░░░███░
 ░░███  █████  ███   ░███ ░███ ░███ ░███░███    █████░███████   ░███
  ░░░█████░█████░    ░███ ░███ ░███ ░███░░███  ░░███ ░███░░░    ░███ ███
    ░░███ ░░███      ████ █████░░██████  ░░█████████ ░░██████   ░░█████
     ░░░   ░░░      ░░░░ ░░░░░  ░░░░░░    ░░░░░░░░░   ░░░░░░     ░░░░░
                              OSINT tool for Nigerian phone numbers
                              By L4ser Security Labs
                              Beta - v1.0.1
```

- - -
OSINT tool for Nigerian phone numbers

WhoGet is an OSINT tool that helps you gather information about nigerian phone numbers.
With WhoGet you can get information about the mobile number such as the 
Carrier, Geocode, Timezone. You can also find more information by searching through
the internet on supported search engines and also on supported social media plataforms.
With WhoGet, you can easily get leads from a phone number to email, websites, images, videos, etc.

## Phone Number Information

Future versions will support listed search engines

* [x] Carrier
* [x] GeoCode
* [x] Timezone
* [ ] Contact name

## Supported Search Engines

Future versions will support listed search engines

* [x] Google
* [x] DuckDuckGo
* [ ] Yahoo
* [ ] Bing

## Supported Social Media Platforms

Future versions will support listed social media platforms

* Twitter
* Facebook

## Install on Linux, Mac OS, Windows

```bash
  git clone https://github.com/L4ser-Security-Labs/whoget.git
  cd whoget
  pip3 install -r requirements.txt
```

## Usage

```txt
usage: whoget.py [-h] [-p P] [-g {google,duckduckgo}]
                 [-s {twitter,instagram,facebook}] [-t]

OSINT tool for Nigerian phone numbers

optional arguments:
  -h, --help            Shows this message and exits
  -p P                  Phone number starting with +234
  -g {google,duckduckgo}
                        Search information using search engines.
  -s {twitter,facebook}
                        Find information on social media
  -t                    Use Tor for anonymity
```

## Examples

```bash
  # Get phone number information
  python3 whoget.py -p +2348123456789

  # Search Google for phone number information
  python3 whoget.py -p +2348123456789 -g google

  # Search DuckDuckGo for phone number information
  python3 whoget.py -p +2348123456789 -g duckduckgo
  
  # Find leads on Twitter
  python3 whoget.py -p +2348123456789 -s twitter
  
  # Find leads from Facebook
  python3 whoget.py -p +2348123456789 -s facebook
  
  # Anonymize Twitter lookup
  python3 whoget.py -p +2348123456789 -s twitter -t

  # Anonymize DuckDuckGo lookup
  python3 whoget.py -p +2348123456789 -g duckduckgo -t

```
