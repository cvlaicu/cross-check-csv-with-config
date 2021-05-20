import csv


def get_hostname(csvfile):
    # the hostname is returned as abcde200.mgt.uk.ro.com
    # what I need to do is only return "abcde200"

    # hostnames_dictionary will contain dictionary of associated values
    hostnames_dictionary = []

    for line in csvfile:
        if line[0] == "Name":
            pass
        else:

            # here I split abcde200.mgt.uk.ro.com by "." and I attach it to the HOSTNAMES_DICTIONARY list
            hostname1 = line[0].upper().split(".")
            # hostname1 is line[0] that contains the list that results from SPLITTING of hostname1
            # "abcde200.mgt.uk.ro.com"
            hostname = hostname1[0]
            # hostname is only abcde200
            interface = line[4]

            dictionary = {"hostname": hostname, "interface": interface}
            hostnames_dictionary.append(dictionary)

    return hostnames_dictionary


def add_path_to_dict(dictionaries):

    final_dict1 = []
    # basically this function iterates through the dictionaries and tries to see if the HOSTNAME corresponds to any
    # of the registered paths. If yes, that path is being appended to the dictionary for easier manipulation

    for dict in dictionaries:
        for key1, value1 in list(dict.items()):
            for path1 in paths:
                if value1 in path1:
                    dict["path"] = path1

        final_dict1.append(dict)

    return final_dict1


def extract_vlan(dictionaries1):

    vlan_numbers = []

    for dictionary in dictionaries1:
        hostname = dictionary['hostname']
        interface = dictionary["interface"]
        path2 = dictionary["path"]

        with open(path2, "r") as text:

            files = text.readlines()
            for line in files:
                if interface in line:
                    index1 = files.index(line)
                    index1 += 3
                    vlan_numbers.append(files[index1])

    return vlan_numbers


def manipulate_extracted_information(vlan_list, dicts2):

    vlan_numbers = []

    for element in vlan_list:
        element = element.split()
        vlan_no = element[3]
        vlan_numbers.append(vlan_no)

    for vlan, each_dict in zip(vlan_numbers, dicts2):
        each_dict['vlan'] = vlan

    with open("output.csv", 'w', newline='') as csvoutput:
        writer = csv.writer(csvoutput)
        for dictionary in dicts2:
            info_list = []
            hostname3 = dictionary['hostname']
            interface3 = dictionary['interface']
            vlan3 = dictionary['vlan']
            info_list.append(hostname3)
            info_list.append(interface3)
            info_list.append(vlan3)
            writer.writerows([info_list])


if __name__ == "__main__":

    with open("file.csv", "r") as file:

        data = csv.reader(file)
        hostnames_dict = get_hostname(data)

    paths = []

    for dicti in hostnames_dict:

        path = "xxxxxxxxxxxxxxxxxxx" ### CHANGE PATH TO CONFIG FOLDER HERE ###
        path += "/" + dicti['hostname'] + "_new.txt"
        paths.append(path)

    final_dict = add_path_to_dict(hostnames_dict)
    access_vlans = extract_vlan(final_dict)
    manipulate_extracted_information(access_vlans, final_dict)

