import csv


def get_rows():
    """Open csv files and return the data"""
    with open('wellbeing.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)


def get_ageattrs():
    """Read each row and get the agegroups, the attributes-satisfaction level and the percentage of the agegroups that have that level in a dictionary of agegroup:percentage."""
    reader = get_rows()
    agegroups = ['C02A', 'C02B', 'C02C', 'C02D']
    attributes = ['V01A', 'V01B', 'V01C', 'V01D', 'V01E', 'V03A', 'V03B', 'V03C', 'V03D', 'V03E', 'V05A', 'V05B', 'V05C', 'V05D',  'V16A', 'V16B', 'V16C', 'V16D',  'V20A', 'V20B',
                  'V20C', 'V20D', 'V22A', 'V22B', 'V22C', 'V22E']
    ages = {}
    for row in reader:
        if row['CACode'] in agegroups:
            if row['VaCode'] in attributes:
                ages.setdefault(row['CACode'], []).append(
                    row['Estimate'])
    return ages


def change_agekeys():
    ages = get_ageattrs()
    key_arr = ['Age_15-24', 'Age_25-44', 'Age_45-64', 'Age_65+']
    new_ages = dict(zip(key_arr, list(ages.values())))
    return new_ages


change_agekeys()


def print_csv():
    """Get the agegroup-percentage dictionary, set the attributes-satisfaction level as column headers and print out a csv file."""
    ages = change_agekeys()
    with open('age.csv', 'w') as f:
        f.write('LS_poor, LS_low, LS_mod, LS_high, LS_great, FW_poor, FW_low, FW_mod, FW_high, FW_great, H_poor, H_mod, H_good, H_great, Lon_high, Lon_mod, Lon_low, Lon_no, Edu_low, Edu_mod, Edu_high, Edu_great, Par_low, Par_mod, Par_high, Par_great, agegroup\n')
        for key, value in ages.items():
            f.write(",".join(value) + "," + key + "\n")


print_csv()


def get_ethattrs():
    """Read each row and get the ethnicities, the attributes-satisfaction level and the percentage of the agegroups that have that level in a dictionary of agegroup:percentage."""
    reader = get_rows()
    ethnicities = ['C12A', 'C12B', 'C12C', 'C12D']
    attributes = ['V04A', 'V04B', 'V04C', 'V04D', 'V10A', 'V11A', 'V11B', 'V11C', 'V11D', 'V11E', 'V17A', 'V17B', 'V17C', 'V17D',  'V21A', 'V21B', 'V21C', 'V21D',  'V23A', 'V23B',
                  'V23C', 'V23D']
    ethnics = {}
    for row in reader:
        if row['CACode'] in ethnicities:
            if row['VaCode'] in attributes:
                ethnics.setdefault(row['CACode'], []).append(
                    row['Estimate'])
    return ethnics


def change_ethnickeys():
    ethnics = get_ethattrs()
    key_arr = ['European', 'Maori', 'Pacific', 'Asians']
    new_ethnics = dict(zip(key_arr, list(ethnics.values())))
    return new_ethnics


def print_csv2():
    """Get the ethnicities-percentage dictionary, set the attributes-satisfaction level as column headers and print out a csv file."""
    ethnics = change_ethnickeys()
    with open('ethnic.csv', 'w') as f:
        f.write(' Inc_poor, Inc_low, Inc_mod, Inc_high, Disc, Cr_vhigh, Cr_high, Cr_mod, Cr_low, Cr_poor, Tr_poor, Tr_mod, Tr_good, Tr_great, Med_low, Med_mod, Med_high, Med_great, Pol_low, Pol_mod, Pol_high, Pol_great, ethnicities\n')
        for key, value in ethnics.items():
            f.write(",".join(value) + "," + key + "\n")


print_csv2()

# The legend is: age.csv: C02A is 15-24, C02B is 25-44, C02C is 45-64 and C024 is 65+
# LS is life satisfaction, FW is family well being, H is health, Lon is loneliness, Edu is trust in education system, Par is trust in Parliament
# ethnic.csv: C12A is European, C12B is Maori, C12C is Pacific and CI2D is Asian
# Inc is income adequacy, Disc is discrimination(which is just one figure of which percentage of the population feels it), Cr is fear of crime, Tr is trust in people, Med is trust in media and Pol is trust in police.
