import os
import subprocess

def install_dependencies():
    print("Installing necessary packages...")
    subprocess.run(["sudo", "pacman", "-S", "tlp", "powertop", "--noconfirm"], check=True)

def enable_tlp():
    print("Enabling and starting TLP service...")
    subprocess.run(["sudo", "systemctl", "enable", "tlp"], check=True)
    subprocess.run(["sudo", "systemctl", "start", "tlp"], check=True)

def enable_cpu_power_saving():
    print("Setting CPU governor to powersave...")
    subprocess.run(["sudo", "cpupower", "frequency-set", "-g", "powersave"], check=True)

def enable_usb_autosuspend():
    print("Enabling USB autosuspend...")
    subprocess.run(["sudo", "sh", "-c", "echo 'options usbcore autosuspend=1' > /etc/modprobe.d/usb-autosuspend.conf"], check=True)

def optimize_powertop():
    print("Running Powertop auto-tune...")
    subprocess.run(["sudo", "powertop", "--auto-tune"], check=True)

def main():
    try:
        install_dependencies()
        enable_tlp()
        enable_cpu_power_saving()
        enable_usb_autosuspend()
        optimize_powertop()
        print("Power-saving optimizations applied successfully!")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
