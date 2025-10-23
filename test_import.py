import sys
import traceback

print('sys.executable =', sys.executable)
print('sys.version =', sys.version)

try:
    import mysql.connector
    print('mysql.connector imported, version attribute:', getattr(mysql.connector, '__version__', 'n/a'))
except Exception:
    print('Import failed:')
    traceback.print_exc()
    # exit non-zero to reflect failure if run directly
    sys.exit(1)

print('Import succeeded')
