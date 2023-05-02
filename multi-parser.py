#!/usr/bin/env python3
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
    parser.add_argument(
        "-t", "--template", type=str, help="Run against a singular template file"
    )
    parser.add_argument(
        "-c",
        "--config_file",
        type=str,
        help="Source configuration file",
        default="conf-files/conf.cfg",
    )
    parser.add_argument(
        "-f",
        "--file_format",
        type=str,
        help="Output file format (options json or yaml)",
        default="yaml",
    )
    parser.add_argument(
        "-d",
        "--template_directory",
        type=str,
        help="Specify different template directory (default is arista-ttp-templates/templates/",
        default="arista-ttp-templates/templates/",
    )

    return parser.parse_args()


def get_config_file(config_file):
    source_file = open(config_file, "r")
    data_to_parse = source_file.read()
    return data_to_parse


def run_parser(data_to_parse, ttp_template, file_format):
    parser = ttp(data_to_parse, template=ttp_template)
    parser.parse()
    results = parser.result(format=file_format)[0]
    return results


def do_output(output_name, results, do_print):
    output = open(output_name, "w")
    output.write(results)
    print("Output file saved as: " + output_name)
    if do_print:
        print(results)


def parse_files(data_to_parse, do_print, template, file_format, template_dir):
    if template:
        template_file = open(template)
        ttp_template = template_file.read()
        results = run_parser(data_to_parse, ttp_template, file_format)
        output_name = (
            "outputs/" + template.rsplit("/", 1)[1] + "-outputfile." + file_format
        )
        do_output(output_name, results, do_print)
    else:
        directory = os.fsencode(template_dir)
        for file in os.listdir(directory):
            next_file = os.fsdecode(file)
            if next_file.endswith(".ttp"):
                active_template = file.decode("utf-8")
                template_file = open(template_dir + active_template)
                ttp_template = template_file.read()
                results = run_parser(data_to_parse, ttp_template, file_format)
                output_name = (
                    "outputs/"
                    + active_template.replace(".ttp", "")
                    + "-outputfile."
                    + file_format
                )
                do_output(output_name, results, do_print)


def main():
    args = cmdline_args()
    data_to_parse = get_config_file(args.config_file)
    parse_files(
        data_to_parse,
        args.do_print,
        args.template,
        args.file_format,
        args.template_directory,
    )


if __name__ == "__main__":
    main()
