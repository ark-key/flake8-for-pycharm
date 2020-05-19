"""Module containing all of the JSON reporters for Flake8."""
from __future__ import print_function, unicode_literals

import json

from flake8.formatting import base


class DefaultJSON(base.BaseFormatter):
    """The non-pretty-printing JSON formatter."""

    def __init__(self, options):

        self.newline = ''
        self.first_error: bool = True
        super(DefaultJSON, self).__init__(options)

    def _write(self, output):
        if self.output_fd is not None:
            self.output_fd.write(output + self.newline)
        if self.output_fd is None or self.options.tee:
            print(output, end=self.newline)

    def write_line(self, line):
        """Override write for convenience."""
        self.write(line, None)

    def stop(self):
        self.write_line(']')

    def start(self):
        self.first_error = True
        self.write_line('[')

    def dictionary_from(self, violation):
        """Convert a Violation to a dictionary."""
        return {
            key: getattr(violation, key)
            for key in [
                'code',
                'filename',
                'line_number',
                'column_number',
                'text',
                'physical_line',
            ]
        }

    def format(self, violation):
        """Format a violation."""
        formatted = {
            "type": "warning",
            "module": "",
            "obj": "",
            "line": violation.line_number,
            "column": violation.column_number,
            "path": violation.filename,
            "symbol": violation.code,
            "message": violation.text,
            "message-id": violation.code
        }
        # Pycharm doesn't like when error's column number exceed line's length
        max_line_length = len(violation.physical_line)
        if violation.column_number >= max_line_length:
            formatted["column"] = max_line_length - 1
        # Convert to json and return
        formatted = json.dumps(formatted)
        if self.first_error:
            self.write_line(formatted)
            self.first_error = False
        else:
            self.write_line(", {}".format(formatted))
