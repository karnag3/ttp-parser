# ttp-parser
My attempt at having ttp cycle though all template files against a config and outputting results.

Assumes there is a config file in conf-files directory named conf.cfg.

Output will land in 'outputs/<template-name>-output.<file-format>'

e.g.:
outputs/clock-timezone-outputfile.yaml


  optional arguments:

  -h, --help            show this help message and exit
  
  -p, --do_print        Print output to screen
  
  -t TEMPLATE, --template TEMPLATE
                        Run against a singular template file
  
  -c CONFIG_FILE, --config_file CONFIG_FILE
                        Source configuration file
  
  -f FILE_FORMAT, --file_format FILE_FORMAT
                        Output file format (options json or yaml)
