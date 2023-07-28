import os
import subprocess
import json
import traceback

class Pokenum:
    def __init__(self):
        thisdir = os.path.dirname(os.path.abspath(__file__))
        self.progdir = os.path.join(thisdir, '.libs')
        self.program = 'pokenum'
        self.progpath = os.path.join(self.progdir, self.program)

    def run(self, *args):
        if os.path.isfile(self.progpath):
            ld_library_path = os.environ.get('LD_LIBRARY_PATH', '')
            ld_library_path = f"/.libs:{ld_library_path}"
            ld_library_path = ld_library_path.rstrip(':')
            os.environ['LD_LIBRARY_PATH'] = ld_library_path

            try:
                output = subprocess.check_output([self.progpath] + list(args))
                output_str = output.decode()
                output_lines = output_str.strip().split('\n')
                headers = output_lines[0].split()
                print("header",headers)
                data = [line.split() for line in output_lines[1:]]
                payload = {
                    "legend": headers,
                    "headers": data[0],
                    "values": data[1:]
                }

                json_payload = json.dumps(payload, indent=None)
                #print(json_payload)
                return json_payload
            except subprocess.CalledProcessError:
                raise RuntimeError(f"Cannot exec {self.program} {args}")
            except json.JSONDecodeError as e:
                traceback.print_exc()
                raise RuntimeError(f"JSONDecodeError: {e}")
        else:
            raise RuntimeError(f"`{self.progpath}` does not exist")

#pokenum = Pokenum()
#output = pokenum.run('-h', 'Ac', '7c', '-', '5s', '4s', '-', 'Ks', 'Kd','--', '2s', '3d', 'As')
#print(output)
