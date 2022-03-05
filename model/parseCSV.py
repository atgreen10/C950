import csv
# Imports the Package CSV file
import Package
import hashTable

with open('packageCSV.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    packages_list = []
    # packageIDs = []
    # addresses = []
    # cities = []
    # states = []
    # postCodes = []
    # deadlines = []
    # weights = []
    # notes = []

    myHash = hashTable.Hash_Table()

    for row in readCSV:

        # Package.Package.get_package_id = row[0]
        # Package.Package.get_address = row[1]
        # Package.Package.get_city = row[2]
        # Package.Package.get_state = row[3]
        # Package.Package.get_postalCode = row[4]
        # Package.Package.get_deadline = row[5]
        # Package.Package.get_kilos = row[6]
        # Package.Package.get_notes = row[7]

        package_obj = Package.Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
        packages_list.append([package_obj.get_package_id(), package_obj])
        myHash.add(package_obj.get_package_id(), package_obj)

    # package_obj[0].__str__()
    # print(packages_list[0].get_package_id())



