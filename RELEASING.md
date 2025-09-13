# Releasing the dataset

## Recreate the raw data from glottography-data

In case of upstream changes in glottography-data:
```shell
cldfbench download cldfbench_vuillermet2012grammar.py
```

## Recreate the CLDF data

```shell
cldfbench makecldf cldfbench_vuillermet2012grammar.py --glottolog-version v5.2
cldfbench cldfreadme cldfbench_vuillermet2012grammar.py
cldfbench zenodo --communities glottography cldfbench_vuillermet2012grammar.py
cldfbench readme cldfbench_vuillermet2012grammar.py
```

## Validation

```shell
cldf validate cldf
```

```shell
cldfbench geojson.validate cldf
```

```shell
cldfbench geojson.glottolog_distance cldf --format pipe
```

| ID | Distance | Contained | NPolys |
|:---------|-----------:|:------------|---------:|
| arao1248 | 0.00 | False | 2 |
| ayor1240 | 0.47 | False | 1 |
| baur1253 | 0.10 | False | 2 |
| cani1243 | 0.00 | True | 1 |
| cavi1250 | 0.00 | True | 1 |
| cayu1262 | 0.03 | False | 2 |
| chac1251 | 0.57 | False | 1 |
| east2555 | 0.00 | True | 1 |
| esee1248 | 0.60 | False | 2 |
| guar1292 | 0.54 | False | 1 |
| iton1250 | 0.27 | False | 1 |
| leco1242 | 0.73 | False | 2 |
| mach1268 | 0.73 | False | 1 |
| mose1249 | 0.50 | False | 1 |
| movi1243 | 0.14 | False | 1 |
| paca1246 | 1.36 | False | 1 |
| reye1240 | 0.61 | False | 2 |
| siri1273 | 0.62 | False | 1 |
| sout2991 | 0.00 | True | 14 |
| stan1288 | 87.30 | False | 1 |
| taca1256 | 0.20 | False | 1 |
| tapi1253 | 0.00 | False | 1 |
| uruu1244 | 1.07 | False | 1 |
| wich1262 | 0.17 | False | 1 |
| yami1256 | 2.32 | False | 1 |
| yuqu1240 | 0.00 | True | 2 |
| yura1255 | 0.27 | False | 1 |
