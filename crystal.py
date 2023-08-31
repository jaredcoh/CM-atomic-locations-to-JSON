from mendeleev import element
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import csv
import json
import os
import sys
import re
import numpy as np
import shutil



ATM_RAD = {'H': 0.25, 'He': 1.2, 'Li': 1.45, 'Be': 1.05, 'B': 0.85, 'C': 0.7, 'N': 0.65, 'O': 0.6, 'F': 0.5, 'Ne': 1.6, 'Na': 1.8, 'Mg': 1.5, 'Al': 1.25, 'Si': 1.1, 'P':1.0, 'S': 1.0, 'Cl': 1.0, 'Ar': 0.71, 'K': 2.2, 'Ca': 1.8, 'Sc': 1.6, 'Ti': 1.4,'V': 1.35, 'Cr': 1.4, 'Mn': 1.4, 'Fe': 1.4, 'Ni': 1.35, 'Cu': 1.35, 'Zn': 1.35,'Ga': 1.3, 'Ge': 1.25, 'As': 1.15, 'Se': 1.15, 'Br': 1.15, 'Kr': '2.02', 'Rb': 2.35, 'Sr': 2.0, 'Y': 1.8, 'Zr': 1.55, 'Nb': 1.45, 'Mo': 1.45, 'Tc': 1.35, 'Ru':1.3, 'Rh': 1.35, 'Pd': 1.4, 'Ag': 1.6, 'Cd': 1.55, 'In': 1.55, 'Sn': 1.45, 'Sb': 1.45, 'Te': 1.4, 'I': 1.4, 'Xe': '1.08', 'Cs': 2.6, 'Ba': 2.15, 'La': 1.95, 'Ce': 1.85, 'Pr': 1.85, 'Nd': 1.85, 'Pm': 1.85, 'Sm': 1.85, 'Eu': 1.85, 'Gd': 1.8,'Tb': 1.75, 'Dy': 1.75, 'Ho': 1.75, 'Er': 1.75, 'Tm': 1.75, 'Yb': 1.75, 'Lu': 1.75, 'Hf': 1.55, 'Ta': 1.45, 'W': 1.35, 'Re': 1.35, 'Os': 1.3, 'Ir': 1.35, 'Pt':1.35, 'Au': 1.35, 'Hg': 1.5, 'Tl': 1.9, 'Pb': 1.8, 'Bi': 1.6, 'Po': 1.9, 'At': None, 'Rn': None, 'Fr': None, 'Ra': 2.15, 'Ac': 1.95, 'Th': 1.8, 'Pa': 1.8, 'U': 1.75, 'Np': 1.75, 'Pu': 1.75, 'Am': 1.75, 'Cm': None, 'Bk': None, 'Cf': None, 'Es': None, 'Fm': None, 'Md': None, 'No': None, 'Lr': None,'Rf': None, 'Db': None, 'Sg': None, 'Bh': None, 'Hs': None, 'Mt': None, 'Ds': None, 'Rg': None, 'Cn': None, 'Nh': None, 'Fl': None, 'Mc':None, 'Lv': None, 'Ts': None, 'Og': None}

def introPopUp():

    # Create the main window
    window = tk.Tk()
    window.title("Introduction to Setting Up your file")

    # Create the message label
    message = "This will take you through the steps on setting up your file to be viewed on Unity.\n\n Things to note:\n-This system cannot currently show more than 16 different atom types\n-This system canot show bonds\n-This system does not show the unit cell\n-This system cannot increase the range\n\nProgress will continue to try to increase functionality, but is dependent upon the designers to do so.\n\nIf you would like to skip to opening your file, click 'Skip'. If you would like to learn how to create your file in CrystalMaker to be parsed, click 'OK'"
    label = tk.Label(window, text=message)
    label.pack(padx=20, pady=20)
    def on_ok():
        window.destroy()
        openCrystalMakerPopUp()
    def on_skip():
        window.destroy()
        openFilePopUp()
    # Create the OK button
    ok_button = tk.Button(window, text="OK", width=10, command=on_ok)
    ok_button.pack(padx=10, pady=10, side=tk.LEFT)
    skip_button = tk.Button(window, text="Skip", width=10, command=on_skip)
    skip_button.pack(padx=10, pady=10, side=tk.LEFT)
    # Create the Cancel button
    cancel_button = tk.Button(window, text="Cancel", width=10, command = window.destroy)
    cancel_button.pack(padx=10, pady=10, side=tk.RIGHT)

    # Run the main event loop
    window.mainloop()


def openCrystalMakerPopUp():
    # Create the main window

    window = tk.Tk()
    window.title("CrystalMaker")

    # Create the message label
    message = "Open up CrystalMaker and create/select your desired crystal to be viewed in AR"
    label = tk.Label(window, text=message)
    label.pack(padx=20, pady=20)
    def on_ok():
        window.destroy()
        downloadFilePopUp()
    def on_back():
        window.destroy()
        introPopUp()
    # Create the OK button
    ok_button = tk.Button(window, text="OK", width=10, command=on_ok)
    ok_button.pack(padx=10, pady=10, side=tk.LEFT)

    # Create the Cancel button
    back_button = tk.Button(window, text="Back", width=10, command = on_back)
    back_button.pack(padx=10, pady=10, side=tk.RIGHT)

    cancel_button = tk.Button(window, text="Cancel", width=10, command=window.destroy)
    cancel_button.pack(padx=10, pady=10, side=tk.LEFT)

    # Run the main event loop
    window.mainloop()

def downloadFilePopUp():
    # Create the main window

    window = tk.Tk()
    window.title("Download File From CrystalMaker")

    # Create the message label
    message = "Go to 'File > Export Data > Atomic Coordinates' and save on the Desktop (or somewhere you know where to find it)"
    label = tk.Label(window, text=message)
    label.pack(padx=20, pady=20)
    def on_ok():
        window.destroy()
        openFilePopUp()
    def on_back():
        window.destroy()
        openCrystalMakerPopUp()
    # Create the OK button
    ok_button = tk.Button(window, text="OK", width=10, command=on_ok)
    ok_button.pack(padx=10, pady=10, side=tk.LEFT)

    # Create the Cancel button
    back_button = tk.Button(window, text="Back", width=10, command = on_back)
    back_button.pack(padx=10, pady=10, side=tk.RIGHT)

    cancel_button = tk.Button(window, text="Cancel", width=10, command=window.destroy)
    cancel_button.pack(padx=10, pady=10, side=tk.LEFT)

    # Run the main event loop
    window.mainloop()

def openFilePopUp():
    def on_continue(file_path):
        window.destroy()
        conversion(file_path)
    def on_rechoose():
        window.destroy()
        openFilePopUp()
    def open_file():
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            # Open the selected file
            with open(file_path, 'r') as file:
                content = file.read()
                text.insert(tk.END, content)
            open_button.configure(text="Continue", command=lambda: on_continue(file_path))
            rechoose_button = tk.Button(window, text="Rechoose", command=on_rechoose)
            rechoose_button.pack(padx=10, pady=10, side=tk.RIGHT)
    window = tk.Tk()
    window.title("Text File Viewer")

    # Create a text widget to display the file contents
    text = tk.Text(window, height=10, width=50)
    text.pack(padx=10, pady=10)

    # Create an "Open" button
    open_button = tk.Button(window, text="Open", command=open_file)
    open_button.pack(padx=10, pady=10)


    # Run the main event loop
    window.mainloop()

def conversion(file_path):
    def tkinter_stuff():
        window = tk.Tk()
        window.title("Converting File")

        # Create the message label in the new popup
        message = f"Code will start running after you click okay. Inputs will pop-up as needed. \nThe code will result in one of two options: Successful or Unsuccessful (with error shown)"
        label = tk.Label(window, text=message)
        label.pack(padx=20, pady=20)
        ok_button = tk.Button(window, text="OK", width=10, command=window.destroy)
        ok_button.pack(padx=10, pady=10)
        # Run the main event loop
        window.mainloop()


    def open_text_popup(message):
        def on_ok():
            nonlocal value
            value = entry.get()
            print("BBB", value)
            popup_window.destroy()

        value = None
        # Create the popup window
        popup_window = tk.Tk()
        popup_window.title("Input Required")

        # Create the message label in the popup window
        label = tk.Label(popup_window, text=message)
        label.pack(padx=20, pady=20)

        # Create an entry field for user input
        entry = tk.Entry(popup_window)
        entry.pack(pady=10)

        # Create the OK button for the popup window
        ok_button = tk.Button(popup_window, text="OK", width=10, command=on_ok)
        ok_button.pack(padx=10, pady=10)

        popup_window.mainloop()
        return value

    def successful_popup(file_loc):
        window = tk.Tk()
        window.title("Success!")
        message = "Your file conversion was a success! Your TXT file was moved to 'Documents > TXT Files' folder. Click OK to move onto the next step\n\nYour JSON file is located at " + file_loc
        # Create the message label in the popup window
        label = tk.Label(window, text=message)
        label.pack(padx=20, pady=20)

        def on_ok():
            window.destroy()
            unityPopUp()
        def on_exit():
            window.destroy()
            sys.exit()
        def on_ch():
            window.destroy()
            openFilePopUp()


        # Create the OK button for the popup window
        ok_button = tk.Button(window, text="OK", width=10, command=on_ok)
        ok_button.pack(padx=10, pady=10, side = tk.LEFT)

        ch_button = tk.Button(window, text="Choose Another", width=15, command=on_ch)
        ch_button.pack(padx=10, pady=10, side = tk.RIGHT)

        ex_button = tk.Button(window, text="Exit", width=10, command=on_exit)
        ex_button.pack(padx=10, pady=10, side = tk.RIGHT)

        # Run the main event loop for the popup window
        window.mainloop()

    def unsuccessful_popup(error):
        popup_window = tk.Tk()
        popup_window.title("Failed")
        message = "Your file conversion was not succesful\n\nError: " + error + "\nPlease look at your file or the python code to resolve issue."
        ok_button = tk.Button(popup_window, text="OK", width=10, command=popup_window.destroy)
        ok_button.pack(padx=10, pady=10)
        # Create the message label in the popup window
        label = tk.Label(popup_window, text=message)
        label.pack(padx=20, pady=20)
        popup_window.mainloop()

    def dict_to_json_file(dict, file_path):
        file_name = os.path.basename(file_path)
        # Example dictionary
        # Convert dictionary to JSON string
        json_str = json.dumps(dict)
        print(json_str)
        # Save JSON string to a fileC:
        new_file_path = "C:\\Users\\MSE-HOLOLENS-COMP\\Documents\\JSON Files\\" + file_name.replace(" ", "").replace(".txt", "")+".json"
        with open(new_file_path, "w") as file:
            file.write(json_str)
        print(new_file_path)
        return new_file_path

    def find_last_two_lines(lines):
        count = 0
        indices = []

        # Iterate through the lines in reverse order
        for i in range(len(lines) - 1, -1, -1):
            line = lines[i]
            if line.startswith('---'):
                # Add the index to the indices list
                indices.append(i)
                count += 1

                if count == 2:
                    # Break the loop if we have found the last two lines
                    break

        return indices[::-1]

    def clean_elements(array):
        array = [element for element in array if element.strip() != ""]
        new_array = []
        for elem in array:
            new_array.append(elem.replace("\n", "").replace(" ",""))
        return new_array

    def get_number_locations(lines):
        for line in lines:
            if line.split(" ")[0] == "Listing":
                return line.split(" ")[3]

    def center_origin(dict):
        # Extract "xor", "yor", and "zor" values
        atoms = dict["atoms"]
        xor_list = [atom["xor"] for atom in atoms]
        yor_list = [atom["yor"] for atom in atoms]
        zor_list = [atom["zor"] for atom in atoms]

        # Compute the average of xor, yor, and zor
        xor_avg = np.mean(xor_list)
        yor_avg = np.mean(yor_list)
        zor_avg = np.mean(zor_list)

        # Shift the values
        shifted_xor = [xor - xor_avg for xor in xor_list]
        shifted_yor = [yor - yor_avg for yor in yor_list]
        shifted_zor = [zor - zor_avg for zor in zor_list]

        # Update the shifted values in the JSON
        for i, atom in enumerate(atoms):
            atom["xor"] = shifted_xor[i]
            atom["yor"] = shifted_yor[i]
            atom["zor"] = shifted_zor[i]

        # Convert the updated JSON back to string
        return dict

    def move_file(source_path, destination_path):
        try:
            # Move the file from the source path to the destination path
            shutil.move(source_path, destination_path)
            print(f"TXT File moved successfully")
        except FileNotFoundError:
            print(f"Source file '{source_path}' not found.")
        except PermissionError:
            print(f"Permission error occurred while moving the file.")
        except shutil.Error as e:
            print(f"An error occurred while moving the file: {e}")


    tkinter_stuff()
    colors = ["red", "green", "blue", "orange" ,"cyan", "magenta", "yellow", "purple",  "brown", "teal", "silver", "gold", "lime", "grey", "white", "black"]
    print(file_path)
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            all_dict = { "cell_info": {},"atoms": []}
            for line in lines:
                array = [element.rstrip('\n') for element in line.split() if element.strip() != '']
                if len(array) == 10:
                    array_new = [elem for elem in array if not '=' in elem][:-1]
                    for key, value in zip(array_new[::2], array_new[1::2]):
                        all_dict["cell_info"][key] = float(value.rstrip(';'))
        print(get_number_locations(lines))
        important_info_range = find_last_two_lines(lines)
        first = important_info_range[0]
        last = important_info_range[1]
        for line in lines[first+1:last]:
            info = line.split("   ")
            info = clean_elements(info)
            atomic_radius = None
            color = None
            try:
                atomic_radius = ATM_RAD[info[0]]
                if atomic_radius == None:
                    raise "AAAA"
            except:
                if all_dict["atoms"] != []:
                    for atom in all_dict["atoms"]:
                        if atom["symbol"] == info[0]:
                            atomic_radius = atom["atomic_radius"]
                            break

            if atomic_radius == None:
                atomic_radius = open_text_popup("What is the radius (in Angstroms) of " + info[0] + "? ")
                atomic_radius = float(atomic_radius)

            if color == None and all_dict["atoms"] != []:
                for atom in all_dict["atoms"]:
                    if atom["symbol"] == info[0]:
                        color = atom["color"]
                        break
            if color == None:
                color = colors[0]
                colors = colors[1:]
            array = [info[0], round(atomic_radius,4), color, float(info[-3]), float(info[-2]), float(info[-1])]
            print(array)
            all_dict["atoms"].append({"symbol":info[0], "atomic_radius":atomic_radius, "color":color, "xor":float(info[-3]),"yor":float(info[-2]),"zor":float(info[-1])})
        all_dict = center_origin(all_dict)
        file_loc = dict_to_json_file(all_dict, file_path)
        move_file(file_path, r"C:\\Users\\MSE-HOLOLENS-COMP\\Documents\\Text Files\\"+os.path.basename(file_path))
        successful_popup(file_loc)
    except Exception as e:
        unsuccessful_popup(str(e))

def unityPopUp():
    def on_ok():
        window.destroy()
        sys.exit()
    window = tk.Tk()
    window.title("Hololens Files + Holocrystal Information")
    message = f"-Plug in Hololens to computer and turn the Hololens on. \n-Drag the JSON file into Hololens's Documents folder\n-Run HoloCrystal on Hololens\n-Choose your desired Crystal in HoloCrystal\n\nThat's it! Enjoy visualizing your crystal :)"
    label = tk.Label(window, text=message)
    label.pack(padx=20, pady=20)
    ok_button = tk.Button(window, text="OK", width=10, command=on_ok)
    ok_button.pack(padx=10, pady=10)

    window.mainloop()

introPopUp()
