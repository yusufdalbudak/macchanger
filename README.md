# MAC Changer

This Python script allows you to change the MAC address of a specified network interface.

## Features
- Parses and validates command line arguments
- Changes the MAC address of a specified network interface
- Retrieves the current MAC address before and after the change to verify the update

## Requirements
- Python 3.x
- `argparse` module
- `re` module
- `subprocess` module
- `sys` module

## Usage
1. Clone the repository:
   ```sh
   git clone https://github.com/yusufdalbudak/macchanger.git
   cd macchanger
Run the script with the required arguments:

"python macchanger.py -i <interface> -m <new_mac_address>"

License
This project is licensed under the MIT License - see the LICENSE file for details.

Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
