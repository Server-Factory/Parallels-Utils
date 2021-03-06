#!/usr/bin/python
import os
import sys
import time
import xml.etree.ElementTree


def main():
    if len(sys.argv) > 1:
        image = sys.argv[1]
        file_path = image + "/config.pvs"
        if os.path.exists(file_path):
            with open(file_path, 'r') as fp:
                print(file_path + ": Configuration file")
                """
                    <ParallelsVirtualMachine dyn_lists="VirtualAppliance 0" schemaVersion="1.0">
                       
                       <Identification dyn_lists="">
                       
                          <VmName>VM_NAME</VmName>
                       </Identification>
                    </ParallelsVirtualMachine
                """
                ext = "IDFR"
                et = xml.etree.ElementTree.parse(file_path)
                for child in et.getroot().findall('.//Identification'):
                    for vm_name in child.findall('.//VmName'):
                        millis = int(round(time.time() * 1000))
                        addition = " " + ext + str(millis)
                        current_name = vm_name.text
                        if ext in current_name:

                            parts = current_name.split(ext)
                            new_name = parts[0].strip() + addition
                        else:
                            new_name = current_name + addition
                        vm_name.text = new_name
                        et.write(file_path)
                        print("Machine name set to: " + new_name)

        else:
            print("ERROR: Configuration file was not found")
            sys.exit(1)

    else:
        print("No image path provided")
        sys.exit(1)


if __name__ == "__main__":
    main()
