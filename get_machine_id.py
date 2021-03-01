#!/usr/bin/python
import subprocess
import sys


def main():
    if len(sys.argv) > 1:
        machines = dict()
        image = sys.argv[1]
        row_home = "Home:"
        row_id_open = "{"
        row_id_close = "}"
        output = subprocess.check_output(['prlctl', 'list', '-a', '-i'])
        items = str(output).split("ID:")
        for item in items:
            if row_home in item:
                home = ""
                machine_id = ""
                rows = item.strip().split('\\n')
                for row in rows:
                    if row_id_open in row.strip() and row_id_close in row.strip():
                        machine_id = row.replace(row_id_open, "").replace(row_id_close, "").strip()
                    if row_home in row:
                        home = row.replace(row_home, "").strip()
                machines[home] = machine_id

        for machine_id in machines:
            if machine_id.startswith(image):
                machine = machines[machine_id]
                print(machine)
                sys.exit(0)

        print("Unknown_ID")
        sys.exit(1)
    else:
        print("No image path provided")
        sys.exit(1)


if __name__ == "__main__":
    main()
