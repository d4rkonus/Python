#!/usr/bin/python3

from pathlib import Path
import shutil
import os
import time


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    try:
        print("\n[$] Welcome to Terminal File Manager [$]")
        print("\n· Options available to use:")
        print("1) List directories and subdirectories")
        print("2) Create new file")
        print("3) Create new directory")
        print("4) Move file")
        print("5) Delete directory")
        print("6) Delete file")
        print("7) Exit")

        option = input("\n· Select your option here --> ").strip()

        # ----------------- OPTION 1 -----------------
        if option == "1":
            path_input = input("Put the complete path here --> ").strip()
            path = Path(path_input).expanduser().resolve()

            if not path.exists():
                print("[!] The path does not exist.")
            elif not path.is_dir():
                print("[!] The path is not a directory.")
            else:
                for content in path.rglob("*"):
                    print(content.name)
                input("\nPlease press Enter to continue ...")
                clear_screen()
    
        # ----------------- OPTION 2 -----------------
        elif option == "2":
            path_input = input("Give me the directory to create the file: ").strip()
            path = Path(path_input).expanduser().resolve()

            if not path.exists() or not path.is_dir():
                print("[!] Invalid directory.")
            else:
                filename = input("Give me the file name (with extension): ").strip()
                file_path = path / filename

                if file_path.exists():
                    print("[!] The file already exists.")
                else:
                    file_path.touch()
                    print(f"[+] New file created at {file_path}")
                    time.sleep(3)
            clear_screen()
        # ----------------- OPTION 3 -----------------
        elif option == "3":
            path_input = input("Where do you want to create the directory? ").strip()
            path = Path(path_input).expanduser().resolve()

            if not path.exists() or not path.is_dir():
                print("[!] Invalid path.")
            else:
                dirname = input("Directory name: ").strip()
                new_dir = path / dirname

                if new_dir.exists():
                    print("[!] The directory already exists.")
                else:
                    new_dir.mkdir()
                    print(f"[+] New directory created at {new_dir}")
                    time.sleep(3)
            clear_screen()
        # ----------------- OPTION 4 -----------------
        elif option == "4":
            file_input = input("File to move (full path): ").strip()
            destination_input = input("Destination directory: ").strip()

            file_path = Path(file_input).expanduser().resolve()
            destination = Path(destination_input).expanduser().resolve()

            if not file_path.exists():
                print("[!] The file does not exist.")
            elif not destination.exists() or not destination.is_dir():
                print("[!] Invalid destination.")
            else:
                shutil.move(str(file_path), str(destination))
                print("[+] File moved successfully.")
                time.sleep(3)
            clear_screen()
        # ----------------- OPTION 5 -----------------
        elif option == "5":
            dir_input = input("Directory to remove (full path): ").strip()
            dir_path = Path(dir_input).expanduser().resolve()

            if not dir_path.exists() or not dir_path.is_dir():
                print("[!] Invalid directory.")
            else:
                confirm = input("Are you sure? (y/n): ").lower()
                if confirm == "y":
                    shutil.rmtree(dir_path)
                    print("[!] Directory deleted successfully.")
                    time.sleep(3)
            clear_screen()
        # ----------------- OPTION 6 -----------------
        elif option == "6":
            file_input = input("File to remove (full path): ").strip()
            file_path = Path(file_input).expanduser().resolve()

            if not file_path.exists() or not file_path.is_file():
                print("[!] Invalid file.")
            else:
                confirm = input("Are you sure? (y/n): ").lower()
                if confirm == "y":
                    file_path.unlink()
                    print("[+] File deleted successfully.")
                    time.sleep(3)
            clear_screen()
        # ----------------- OPTION 7 -----------------
        elif option == "7":
            print("\n[!] Leaving the Terminal File Manager ...")
            break

        else:
            print("[!] Invalid option.")

    except KeyboardInterrupt:
        print("\n\n[!] Moving to safe zone...")
        break