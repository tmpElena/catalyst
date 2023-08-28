## Flowform
Flowform is a declarative configuration language for your data pipelines.

For example: you can specify that you want to load data from 
a PostgreSQL table, perform transformation and load the result
to a csv file using this config:
```yaml
extract:
  connector: postgres

transform:
  getBestSongs:
    getAllSongs: select * from artist
    getBest: where rating > 8

load:
  getBestSongs:
    format: csv
    fileName: result
```

## How does it work?

| block | explanation                                  |
|------|----------------------------------------------|
| connector: postgres | specifyies the data source                   |
| getBestSongs | task name, you can name it anything          |
| getAllSongs     | subquery name, you can name it anything      |
| load:getBestSongs | this loads the result from getBestSongs task |

NOTE: Subqueries get appended with the previous subquery.

### Configuration
`profiles/profiles.yaml` specifies the data source configs.

`demo/demo.yaml` specifies the yaml file for your pipeline. 

## Installation
```bash
pip install flowform
```

## How to run
```bash
ff run --file=<script>.yaml
```

## Running demo
You will require postgres installed on your system. 
In psql you can run following command to load demo table
```bash
\i <Path to this directory>/demo/demo.sql
```
or manually run sql commands in demo.sql to build example table. 

Then you need to run the command:
```bash
 ff run --file=./demo/demo.yaml 
```

## Support Status
Currently, supports extracting from PostgresSQL and exporting
to a file.