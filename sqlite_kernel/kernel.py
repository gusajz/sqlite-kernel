from ipykernel.kernelbase import Kernel

import sqlite3
from contextlib import closing

from . import __version__

class SqliteKernel(Kernel):
    implementation = 'Sqlite'
    implementation_version = __version__
    language = 'sqlite'
    language_version = '3'
    language_info = {
        'name': 'sqlite',
        'codemirror_mode': 'sql',
        'mimetype': 'text/x-sql',
        'file_extension': '.sql'}

    banner = "Sqlite kernel - Just type sql"

    def __init__(self, **kwargs):
        Kernel.__init__(self, **kwargs)
        self._conn = None 

    def _execute_sql(self, code):
        with closing(self._conn.cursor()) as cursor:
            try:
                cursor.execute(code)
                return str(cursor.fetchone())
            except Exception as e:
                return str(e)

    def _execute_meta_cmd(self, code):
        parts = code.split(' ')
        cmd = parts[0]
        args = parts[1:]

        if cmd == 'open':
            self._conn = sqlite3.connect(args[0])
            return 'Success'
        else:
            return 'Unknown command'



    def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=False):

        code = code.strip()
        if not code:
            return {'status': 'ok', 'execution_count': self.execution_count,
                    'payload': [], 'user_expressions': {}}

        if not silent:
            if code[0] == '%':
                result = self._execute_meta_cmd(code[1:])
            else:
                if self._conn:
                    result = self._execute_sql(code)
                else:
                    result = "Please open the database with %open"

            stream_content = {'name': 'stdout', 'text': result}
            self.send_response(self.iopub_socket, 'stream', stream_content)

        return {'status': 'ok',
                # The base class increments the execution count
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {},
               }


if __name__ == '__main__':
    from ipykernel.kernelapp import IPKernelApp
    IPKernelApp.launch_instance(kernel_class=SqliteKernel)