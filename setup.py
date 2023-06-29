import os
'''
Thanks ChatGPT
'''

def create_noon_command():
    # Get the directory path of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Create the path to the CLI app script
    cli_script_path = os.path.join(script_dir, 'app.py')

    # Create the contents of the "noon" script
    script_content = '''#!/bin/bash
python {0} "$@"
'''.format(cli_script_path)

    # Determine the destination directory for the "noon" script
    destination_dir = '/usr/local/bin'  # Change this if necessary

    # Create the "noon" script file
    script_file = os.path.join(destination_dir, 'noon')
    with open(script_file, 'w') as f:
        f.write(script_content)

    # Make the "noon" script executable
    os.chmod(script_file, 0o755)

    print('Custom command "noon" created successfully!')

create_noon_command()


