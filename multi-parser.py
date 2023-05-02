from ttp import ttp
import os
import argparse


def cmdline_args():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-p",
        "--do_print",
        action="store_true",
        help="Print output to screen",
    )
    parser.add_argument("-t", "--template", type=str , help="Run against a singular template file")
    parser.add_argument("-c", "--config_file", type=str, help="Source configuration file")
    
    return parser.parse_args()

def get_config_file(config_file):
  if config_file:
    source_file = open(config_file, 'r')
  else:
    source_file = open('conf-files/conf-1.cfg', 'r')  
  data_to_parse = (source_file.read())
  return data_to_parse

TEMPLATE_DIR = 'arista-ttp-templates/templates'
DIRECTORY = os.fsencode(TEMPLATE_DIR)


def run_parser(data_to_parse,do_print):
  for file in os.listdir(DIRECTORY):
    next_file  = os.fsdecode(file) 
    if next_file.endswith('.ttp'):
      active_template = file.decode('utf-8')
      template_file = open('arista-ttp-templates/templates/' + active_template)
      ttp_template = (template_file.read())
      parser = ttp(data_to_parse, template=ttp_template)
      parser.parse()
      results = parser.result(format='yaml')[0]
      output = open('outputs/' + active_template.replace('.ttp','') + '-outputfile.yml', 'w')
      output.write(results)
      if do_print:
        print(results)

def main():
   args = cmdline_args()
   data_to_parse = get_config_file(args.config_file)
   run_parser(data_to_parse,args.do_print)

if __name__ == "__main__":
    main()