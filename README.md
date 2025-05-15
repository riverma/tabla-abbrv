# tabla-abbrv
Converts [Tabla notation](https://en.wikipedia.org/wiki/Tabla#Basic_strokes) shorthand (abbreviations) into full long-hand notation.

i.e. ``dttkttkttkt`` -> ``DhaTheTeKeTeTaKeTheTeKeTe``

## Requirements

* A command-line terminal
* Python 3.x (Python 2.x may also work but is not officially supported)

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
$ python tabla-abbrv.py "dt dgtnkt"
DhaTi DhaGeTuNaKaTa
```

```
$ python tabla-abbrv.py "dtdgtnkt dtdttkttkttkt dtdttkttkttkt dtdgtnkt"
DhaTiDhaGeTuNaKaTa DhaTiDhaTheTeKeTeTaKeTheTeKeTe DhaTiDhaTheTeKeTeTaKeTheTeKeTe DhaTiDhaGeTuNaKaTa
```

For backwards compatibility, you can also use the old bash script:

```
$ ./tabla-abbrv.sh "dtdgtnkt dtdttkttkttkt dtdttkttkttkt dtdgtnkt"
DhaTiDhaGeTuNaKaTa DhaTiDhaTheTeKeTeTaKeTheTeKeTe DhaTiDhaTheTeKeTeTaKeTheTeKeTe DhaTiDhaGeTuNaKaTa
```
