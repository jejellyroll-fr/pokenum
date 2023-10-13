import os
import subprocess
import json
import traceback

class Pokenum:
    """
    A class representing a Pokenum object.

    This class provides functionality to run the 'pokenum' program and retrieve the output in JSON format.

    Attributes:
        progdir (str): The directory where the 'pokenum' program is located.
        program (str): The name of the 'pokenum' program.
        progpath (str): The full path to the 'pokenum' program.

    Methods:
        __init__(): Initializes the Pokenum object.
        run(*args) -> str: Runs the 'pokenum' program with the specified arguments and returns the output in JSON format.

    Raises:
        RuntimeError: If the 'pokenum' program does not exist.
        RuntimeError: If an error occurs while executing the 'pokenum' program or parsing the output.
    """

    def __init__(self):
        thisdir = os.path.dirname(os.path.abspath(__file__))
        self.progdir = os.path.join(thisdir, '.libs')
        self.program = 'pokenum'
        self.progpath = os.path.join(self.progdir, self.program)

    def run(self, *args):
        """
        Executes the 'run' method of the Pokenum class.

        This method runs the 'pokenum' program with the specified arguments and returns the output in JSON format.

        Args:
            self: An instance of the Pokenum class.

        Returns:
            str: The output of the 'pokenum' program in JSON format.

        Raises:
            RuntimeError: If the 'pokenum' program does not exist.
            RuntimeError: If an error occurs while executing the 'pokenum' program or parsing the output.
        """

        if not os.path.isfile(self.progpath):
            raise RuntimeError(f"`{self.progpath}` does not exist")
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

            return json.dumps(payload, indent=None)
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Cannot exec {self.program} {args}") from e
        except json.JSONDecodeError as e:
            traceback.print_exc()
            raise RuntimeError(f"JSONDecodeError: {e}") from e

#pokenum = Pokenum()
#output = pokenum.run('-h', 'Ac', '7c', '-', '5s', '4s', '-', 'Ks', 'Kd','--', '2s', '3d', 'As', "-mc", "10000")
#print(output)
