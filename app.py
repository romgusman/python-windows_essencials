import os
import requests
import subprocess
from tqdm import tqdm
from colorama import init, Fore, Back
import platform
import ctypes

init(autoreset=True)

def main():
    while True:
        print_menu()
        choice = input("Write App by number: ").strip()

        if choice == "1":
            install_anydesk()
        elif choice == "2":
            install_google_chrome()
        elif choice == "3":
            install_mozilla_firefox()
        elif choice == "4":
            install_zoom()
        elif choice == "5":
            install_vlc_media_player()
        elif choice == "6":
            install_microsoft_office()
        elif choice == "7":
            install_visual_studio_code()
        elif choice == "8":
            install_discord()
        elif choice == "9":
            install_winrar()
        elif choice == "10":
            install_notepad_plus_plus()
        elif choice == "11":
            install_dropbox()
        elif choice == "12":
            install_adobe_cc()
        elif choice == "13":
            print(Back.BLACK + Fore.GREEN + "Shutting down...")
            break
        else:
            print(Back.BLACK + Fore.RED + "Not valide.")

def print_menu():
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa o terminal
    print(Back.BLACK + Fore.GREEN + "========== Main Menu ==========")
    print(Back.BLACK + Fore.GREEN + "Choose a option:")
    print(Back.BLACK + Fore.YELLOW + "1. Install AnyDesk")
    print(Back.BLACK + Fore.YELLOW + "2. Install Google Chrome")
    print(Back.BLACK + Fore.YELLOW + "3. Install Mozilla Firefox")
    print(Back.BLACK + Fore.YELLOW + "4. Install Zoom")
    print(Back.BLACK + Fore.YELLOW + "5. Install VLC Media Player")
    print(Back.BLACK + Fore.YELLOW + "6. Install Microsoft Office (online)")
    print(Back.BLACK + Fore.YELLOW + "7. Install Visual Studio Code")
    print(Back.BLACK + Fore.YELLOW + "8. Install Discord")
    print(Back.BLACK + Fore.YELLOW + "9. Install WinRAR")
    print(Back.BLACK + Fore.YELLOW + "10. Install Notepad++")
    print(Back.BLACK + Fore.YELLOW + "11. Install Dropbox")
    print(Back.BLACK + Fore.YELLOW + "12. Install Adobe Creative Cloud (Trial Version)")
    print(Back.BLACK + Fore.GREEN + "13. Exit")
    print(Back.BLACK + Fore.GREEN + "====================================")

def install_anydesk():
    print(Back.BLACK + Fore.GREEN + "Starting download: AnyDesk...")
    anydesk_download_url = "https://download.anydesk.com/AnyDesk.exe"
    installer_filename = "AnyDesk.exe"
    try:
        download_with_progress(anydesk_download_url, installer_filename)
        run_installer(installer_filename, "AnyDesk")
        print(Back.BLACK + Fore.GREEN + "AnyDesk: installation successful")
    except Exception as e:
        print(Back.BLACK + Fore.RED + f"AnyDesk installation ERROR: {e}")
    finally:
        input("Press Enter to continue...")

def install_google_chrome():
    print(Back.BLACK + Fore.GREEN + "IStarting download: Google Chrome...")
    chrome_download_url = "https://www.google.com/intl/pt-BR/chrome/"
    installer_filename = "ChromeStandaloneSetup64.exe"
    try:
        download_with_progress(chrome_download_url, installer_filename)
        run_installer(installer_filename, "Google Chrome")
        print(Back.BLACK + Fore.GREEN + "Google Chrome: installation successful")
    except Exception as e:
        print(Back.BLACK + Fore.RED + f"Google Chrome installation ERROR: {e}")
    finally:
        input("Press Enter to continue...")

def install_mozilla_firefox():
    print(Back.BLACK + Fore.GREEN + "Starting download: Mozilla Firefox...")
    firefox_download_url = "https://download.mozilla.org/?product=firefox-latest&os=win&lang=pt-BR"
    installer_filename = "FirefoxSetup.exe"
    try:
        download_with_progress(firefox_download_url, installer_filename)
        run_installer(installer_filename, "Mozilla Firefox")
        print(Back.BLACK + Fore.GREEN + "Mozilla Firefox: installation successful")
    except Exception as e:
        print(Back.BLACK + Fore.RED + f"Mozilla Firefox installation ERROR: {e}")
    finally:
        input("Press Enter to continue...")

def install_zoom():
    print(Back.BLACK + Fore.GREEN + "Starting download: Zoom...")
    zoom_download_url = "https://zoom.us/client/latest/ZoomInstaller.exe"
    installer_filename = "ZoomInstaller.exe"
    try:
        download_with_progress(zoom_download_url, installer_filename)
        run_installer(installer_filename, "Zoom")
        print(Back.BLACK + Fore.GREEN + "Zoom: installation successful")
    except Exception as e:
        print(Back.BLACK + Fore.RED + f"Zoom installation ERROR: {e}")
    finally:
        input("Press Enter to continue...")

def install_vlc_media_player():
    print(Back.BLACK + Fore.GREEN + "Starting download: VLC Media Player...")
    system_architecture = platform.architecture()[0]
    arch_suffix = "64" if system_architecture == "64bit" else "32"
    vlc_download_url = f"https://get.videolan.org/vlc/last/win{arch_suffix}/vlc-{arch_suffix}.0.16-win{arch_suffix}.exe"
    installer_filename = f"vlc-{arch_suffix}.0.16-win{arch_suffix}.exe"
    try:
        download_with_progress(vlc_download_url, installer_filename)
        run_installer(installer_filename, "VLC Media Player")
        print(Back.BLACK + Fore.GREEN + "VLC Media Player: installation successful")
    except Exception as e:
        print(Back.BLACK + Fore.RED + f"VLC Media Player installation ERROR: {e}")
    finally:
        input("Press Enter to continue...")

def install_microsoft_office():
    print(Back.BLACK + Fore.GREEN + "Starting download: Microsoft Office (online)...")
    office_download_url = "https://www.office.com/"
    installer_filename = "OfficeInstaller.exe"
    try:
        download_with_progress(office_download_url, installer_filename)
        run_installer(installer_filename, "Microsoft Office")
        print(Back.BLACK + Fore.GREEN + "Microsoft Office: installation successful")
    except Exception as e:
        print(Back.BLACK + Fore.RED + f"Microsoft Office installation ERROR: {e}")
    finally:
        input("Press Enter to continue...")

def install_visual_studio_code():
    print(Back.BLACK + Fore.GREEN + "Starting download: Visual Studio Code...")
    system_architecture = platform.architecture()[0]
    vscode_download_url = "https://code.visualstudio.com/sha/download?build=stable&os=win32-x64" if system_architecture == "64bit" else "https://code.visualstudio.com/sha/download?build=stable&os=win32"
    installer_filename = "VSCodeSetup.exe"
    try:
        download_with_progress(vscode_download_url, installer_filename)
        run_installer(installer_filename, "Visual Studio Code")
        print(Back.BLACK + Fore.GREEN + "Visual Studio Code: installation successful")
    except Exception as e:
        print(Back.BLACK + Fore.RED + f"Visual Studio Code installation ERROR: {e}")
    finally:
        input("Press Enter to continue...")

def install_discord():
    print(Back.BLACK + Fore.GREEN + "Starting download: Discord...")
    system_architecture = platform.architecture()[0]
    arch_suffix = "x64" if system_architecture == "64bit" else "ia32"
    discord_download_url = f"https://discord.com/api/download?platform=win&arch={arch_suffix}"
    installer_filename = f"DiscordSetup-{arch_suffix}.exe"
    try:
        download_with_progress(discord_download_url, installer_filename)
        run_installer(installer_filename, "Discord")
        print(Back.BLACK + Fore.GREEN + "Discord: installation successful")
    except Exception as e:
        print(Back.BLACK + Fore.RED + f"Discord installation ERROR: {e}")
    finally:
        input("Press Enter to continue...")

def install_winrar():
    print(Back.BLACK + Fore.GREEN + "Starting download: WinRAR...")
    system_architecture = platform.architecture()[0]
    arch_suffix = "x64" if system_architecture == "64bit" else "x86"
    winrar_download_url = f"https://www.win-rar.com/fileadmin/winrar-versions/{arch_suffix}/wrar641.exe"
    installer_filename = f"winrar-{arch_suffix}.exe"
    try:
        download_with_progress(winrar_download_url, installer_filename)
        run_installer(installer_filename, "WinRAR")
        print(Back.BLACK + Fore.GREEN + "WinRAR: installation successful")
    except Exception as e:
        print(Back.BLACK + Fore.RED + f"WinRAR installation ERROR: {e}")
    finally:
        input("Press Enter to continue...")

def install_notepad_plus_plus():
    print(Back.BLACK + Fore.GREEN + "Starting download: Notepad++...")
    npp_download_url = "https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v8.3.1/npp.8.3.1.Installer.exe"
    installer_filename = "npp.8.3.1.Installer.exe"
    try:
        download_with_progress(npp_download_url, installer_filename)
        run_installer(installer_filename, "Notepad++")
        print(Back.BLACK + Fore.GREEN + "Notepad++: installation successful")
    except Exception as e:
        print(Back.BLACK + Fore.RED + f"Notepad++ installation ERROR: {e}")
    finally:
        input("Press Enter to continue...")

def install_dropbox():
    print(Back.BLACK + Fore.GREEN + "Starting download: Dropbox...")
    dropbox_download_url = "https://www.dropbox.com/download?plat=win"
    installer_filename = "DropboxInstaller.exe"
    try:
        download_with_progress(dropbox_download_url, installer_filename)
        run_installer(installer_filename, "Dropbox")
        print(Back.BLACK + Fore.GREEN + "Dropbox: installation successful!")
    except Exception as e:
        print(Back.BLACK + Fore.RED + f"Dropbox installation ERROR: {e}")
    finally:
        input("Press Enter to continue...")

def install_adobe_cc():
    print(Back.BLACK + Fore.GREEN + "Starting download: Adobe Creative Cloud (Trial Version)...")
    adobe_cc_download_url = "https://www.adobe.com/creativecloud/desktop-app.html"
    installer_filename = "AdobeCreativeCloud.exe"
    try:
        download_with_progress(adobe_cc_download_url, installer_filename)
        run_installer(installer_filename, "Adobe Creative Cloud (Trial Version)")
        print(Back.BLACK + Fore.GREEN + "Adobe Creative Cloud (Trial Version): installation successful")
    except Exception as e:
        print(Back.BLACK + Fore.RED + f"Adobe Creative Cloud (Trial Version) installation ERROR: {e}")
    finally:
        input("Press Enter to continue...")

def download_with_progress(url, filename):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        total_size = int(r.headers.get('content-length', 0))
        with open(filename, 'wb') as f, tqdm(
            desc=f"Downloading {filename}",
            total=total_size,
            unit='B',
            unit_scale=True,
            unit_divisor=1024,
            colour='green'
        ) as progress_bar:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
                progress_bar.update(len(chunk))

def run_installer(filename, app_name):
    print(Back.BLACK + Fore.YELLOW + f"Starting installation: {app_name}...")
    try:
        #Execute with admin privilegies
        if platform.system() == "Windows":
            ctypes.windll.shell32.ShellExecuteW(None, "runas", filename, None, None, 1)
        else:
            subprocess.run(["sudo", filename], check=True)
    except subprocess.CalledProcessError as e:
        raise Exception(f"Error during installation {app_name}: {e}")

def clean_up():
    # Limpa o terminal
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    print(Back.BLACK + Fore.RED + "by Romulo Gusman de Oliveira.")
    main()