""" load logging-server and emit logs from the library
"""
import logging
from logging_server import emit_logs


def main():
    emit_logs.emit_debug_logs()
    emit_logs.emit_info_logs()
    emit_logs.emit_warning_logs()
    emit_logs.emit_error_logs()

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    main()
