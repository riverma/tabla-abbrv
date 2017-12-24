# tabla-abbrv
Converts [Tabla notation](https://en.wikipedia.org/wiki/Tabla#Basic_strokes) shorthand (abbreviations) into full long-hand notation.

i.e. ``dttkttkttkt`` -> ``DhaTheTeKeTeTaKeTheTeKeTe``

## Requirements

* A command-line terminal
* ``sed`` - GNU stream editor. Most *nix platforms have this already installed as a tool on the command-line. If you're 
using MacOSX, please not that you'll want to install the GNU version of ``sed`` and not use the pre-installed BSD version 
(because certain regex shortcuts are not supported by the BSD version). If you're using [Homebrew](https://brew.sh/) on MacOSX,
try installing the GNU version of ``sed`` via: ``$ brew install gnu-sed`` and use the binary via ``gsed...``

## Installation

Clone this directory onto your machine:

``git clone https://github.com/riverma/tabla-abbrv.git``

Change into the ``tabla-abbrv`` directory.

## Usage Examples

```
$ echo "dt dgtnkt" | sed -f ./tabla-abbrv.sed``
DhaTi DhaGeTuNaKaTa
```

```
$ echo "dtdgtnkt dtdttkttkttkt dtdttkttkttkt dtdgtnkt" | sed -f ./tabla-abbrv.sed
DhaTiDhaGeTuNaKaTa DhaTiDhaTheTeKeTeTaKeTheTeKeTe DhaTiDhaTheTeKeTeTaKeTheTeKeTe DhaTiDhaGeTuNaKaTa
```
