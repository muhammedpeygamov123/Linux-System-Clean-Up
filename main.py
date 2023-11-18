import subprocess

def password():
    while True:
        password_input = input('Enter password: ')

        if password_input == 'Cr4ck3r':
            usr_ask = input('Wanna clean your machine? (yes/no): ')

            if usr_ask.lower() in ['yes', 'y']:
                try:
                    subprocess.run(['sudo', 'apt', 'clean'])
                    subprocess.run(['sudo', 'apt-get', 'autoremove', '-y'])
                    subprocess.run(['sudo', 'find', '/var/log/', '-type', 'f', '-name', '*.log*', '-exec', 'rm', '-f', '{}', '+'])
                    subprocess.run(['rm', '-rf', '~/.cache/thumbnails'])
                    subprocess.run(['sudo', 'rm', '-rf', '/tmp/*'])

                    print("System cleanup complete!")
                except subprocess.CalledProcessError as e:
                    print(f"Error during cleanup: {e}")
                break  
            else:
                print("Cleanup aborted.")
                break  
        else:
            print('Please Try Again!')

if __name__ == "__main__":
    password()
