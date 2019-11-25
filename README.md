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

Below is a list of supported abbreviations and their conversions.

NOTE: subsets of the below abbreviations are also supported! It is not an exhaustive list. Please play around, as various combinations of the below abbreviations can lead to more complicated long form Tabla sentences.

| Short Form | Long Form |
| --- | --- |
| dtdttkttkttkt | DhaTiDhaTheTeKeTeTaKeTheTeKeTe |
| dtdgtnkt | DhaTiDhaGeTuNaKaTa |
| ttkt | TheTeKeTe |
| dn | DhinNa |
| dd | DhaDha |
| dt | DhaTi |
| tt | TheTe |
| gn | GeNa |
| dg | DhaGe |
| tk | TaKe |
| tn | TuNa |
| kt | KaTa |
| t | Ti |
| d | Dha |
| k | Ka |
| s | S |


```
$ ./tabla-abbrv.sed "dt dgtnkt"
DhaTi DhaGeTuNaKaTa
```

```
$ ./tabla-abbrv.sh "dtdgtnkt dtdttkttkttkt dtdttkttkttkt dtdgtnkt"
DhaTiDhaGeTuNaKaTa DhaTiDhaTheTeKeTeTaKeTheTeKeTe DhaTiDhaTheTeKeTeTaKeTheTeKeTe DhaTiDhaGeTuNaKaTa
```
