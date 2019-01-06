# Simple python module installer

This script scans directory for python scripts and installs needed dependencies

## Getting Started

* Download a copy of [script](spmi.py) from this rep.
* *[Optional]* add to `PATH` for quicker access.

## Usage

* `python3 spmi.py ` - Installs modules for the directory it's running from.
* `python3 spmi.py -d ~/test ` - Installs modules for the `~/test` directory.
* `python3 spmi.py -c 'pip3 install'` - uses `pip3 install` instead of default `pip install`.

### Prerequisites

* pyhton 3.7 or higher.
* pip 10 or higher.

## Author
* **Ilia Nikishin** ([Gibitop](https://github.com/Gibitop)).

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments
* This script won't work if the name of package you `import` doesn't match the name of package you `pip install`.
