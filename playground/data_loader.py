#!/usr/bin/env python
import csv


class DataLoader(object):
    def _find_header_index(self, header_line, node_name):
        colnum = 0
        for col in header_line:
            if col == node_name:
                return colnum
            colnum += 1

    def _parse_header(self, csv_reader, config):
        # get header
        header = csv_reader.next()
        header = [el.strip() for el in header]

        # obtain and set response variable index
        response_var = config["response_variable"]
        response_index = self._find_header_index(header, response_var["name"])
        response_var["data_index"] = response_index

        # obtain and set input variable index
        for input_node in config["input_nodes"]:
            index = self._find_header_index(header, input_node["name"])
            input_node["data_index"] = index

    def _parse_data_row(self, row, config, variables):
        colnum = 0
        for col in row:
            for var in variables:
                if var["data_index"] == colnum:
                    config["data"][var["name"]].append(float(col))
            colnum += 1

    def _parse_data(self, csv_reader, config):
        # var list containig details what each column is
        variables = []
        variables.append(config["response_variable"])
        variables.extend(config["input_nodes"])

        # create data and variables (i.e. a data table in list form)
        config["data"] = {}
        for var in variables:
            config["data"][str(var["name"])] = []

        rownum = 0
        for row in csv_reader:
            self._parse_data_row(row, config, variables)
            rownum += 1

    def load_data(self, config):
        # open data and csv reader
        data_file = open(config["data_file"], "rb")
        csv_reader = csv.reader(data_file)

        self._parse_header(csv_reader, config)
        self._parse_data(csv_reader, config)

        # clean up
        data_file.close()