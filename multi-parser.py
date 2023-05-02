from ttp import ttp
import os

source_file = open('conf-files/conf-1.cfg', 'r')
data_to_parse = (source_file.read())
do_print = True
dir_as_str = 'arista-ttp-templates/templates'
directory = os.fsencode(dir_as_str)

for file in os.listdir(directory):
  next_file  = os.fsdecode(file) 
  if next_file.endswith('.ttp'):
    active_template = file.decode('utf-8')
    template_file = open('arista-ttp-templates/templates/' + active_template)
    ttp_template = (template_file.read())
    parser = ttp(data_to_parse, template=ttp_template)
    parser.parse()
    results = parser.result(format='yaml')[0]
    if do_print:
      print(results)
    output = open('outputs/' + active_template.replace('.ttp','') + '-outputfile.yml', 'w')
    output.write(results)
