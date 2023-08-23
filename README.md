## Running demo
You will require postgres installed on your system. 
In psql you can run following command to load demo table
```bash
\i <Path to this directory>/demo.sql
```
or manually run sql commands in demo.sql to build example table. 
Then you need to run the following run command.

## How to run
```bash
python main.py demo.yaml
```

## Configuration
`profile.yaml` specifies the data source configs and
`demo.yaml` specifies the yaml file for your pipeline. 