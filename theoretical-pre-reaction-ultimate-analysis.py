"""
Pre-Analysis Ultimate Analysis Mixture Predictor
Copyright (C) 2026 Nitish Kapur
GitHub: github.com/nitish-kapur
Licensed under GNU GPLv3

    This script was made as a part of a biofuel research project.

    1.  Defines the elemental compositions (C, H, N, O, S as % mass) for
        each feedstock as dictionaries at the top of the script. Update
        these values to match your own feedstocks and experimental data.

    2.  Defines a list of sample mixtures in mixture_ratios_list, where
        each entry contains a sample name and the mass fractions of each
        feedstock. Mass fractions must sum to 1.0. Update, add, or remove
        entries to match your experimental design.

    3.  For each sample mixture, computes the theoretical ultimate analysis
        by calculating a weighted average of the elemental compositions:

            element% = sum(mass_fraction_i × element%_i)

        This is a theoretical prediction assuming ideal mixing — no
        chemical reactions or transformations are accounted for.

    4.  Filters out feedstocks with zero mass fraction from the printed
        ratio string to keep the output concise.

    5.  Prints the following to the console for each sample:

            Sample Name (feedstock: mass%) => Ultimate Analysis:
            C: x.xx%, H: x.xx%, N: x.xx%, O: x.xx%, S: x.xx%
"""

def calculate_mixture_ultimate_analysis(mixture_ratios, coconut, rice, walnut, LDPE):
    elements = ['C', 'H', 'N', 'O', 'S']
    mixture_analysis = {}

    # Calculate weighted average for each element
    for element in elements:
        mixture_analysis[element] = (mixture_ratios['coconut'] * coconut[element] +
                                     mixture_ratios['rice'] * rice[element] +
                                     mixture_ratios['walnut'] * walnut[element] +
                                     mixture_ratios['LDPE'] * LDPE[element])

    return mixture_analysis

# Ultimate analysis data for coconut shells, rice straw, walnut, and LDPE
rice={'C': 37.51, 'H': 10.043,  'N': 0.52,  'O': 51.560, 'S': 0.368}
LDPE= {'C': 79.22, 'H': 8.253, 'N': 0.0, 'O': 12.301,  'S': 0.226}
coconut={'C': 46.53,  'H': 5.829,  'N': 0.30, 'O': 46.991,  'S': 0.350}
walnut={'C': 45.53,  'H': 5.829,   'N': 0.30,  'O': 47.893, 'S': 0.254}

# Define several named mass fraction sets for mixtures
mixture_ratios_list = [
    {'name': 'Sample 1/24/38', 'ratios': {'coconut': 0.333, 'rice': 0.0, 'walnut': 0.333, 'LDPE': 0.333}},
    {'name': 'Sample 2/39/54', 'ratios': {'coconut': 0, 'rice': 0.333, 'walnut': 0.333, 'LDPE': 0.333}},
    {'name': 'Sample 3/40/55', 'ratios': {'coconut': 0.333, 'rice': 0.333, 'walnut': 0, 'LDPE': 0.333}},
    {'name': 'Sample 4/41', 'ratios': {'coconut': 0.333, 'rice': 0.333, 'walnut': 0.333, 'LDPE': 0}},

    {'name': 'Sample 5/51', 'ratios': {'coconut': 0.166, 'rice': 0.50, 'walnut': 0.166, 'LDPE': 0.166}},
    {'name': 'Sample 6/52', 'ratios': {'coconut': 0.50, 'rice': 0.166, 'walnut': 0.166, 'LDPE': 0.166}},
    {'name': 'Sample 7/53', 'ratios': {'coconut': 0.166, 'rice': 0.166, 'walnut': 0.50, 'LDPE': 0.166}},
    {'name': 'Sample 8/45/57', 'ratios': {'coconut': 0.166, 'rice': 0.166, 'walnut': 0.166, 'LDPE': 0.50}},

    {'name': 'Sample 9/46', 'ratios': {'coconut': 0.833, 'rice': 0.75, 'walnut': 0.8333, 'LDPE': 0.8333}},
    {'name': 'Sample 10/47', 'ratios': {'coconut': 0.75, 'rice': 0.8333, 'walnut': 0.8333, 'LDPE': 0.8333}},
    {'name': 'Sample 11/48', 'ratios': {'coconut': 0.8333, 'rice': 0.8333, 'walnut': 0.75, 'LDPE': 0.8333}},
    {'name': 'Sample 12/49', 'ratios': {'coconut': 0.8333, 'rice': 0.8333, 'walnut': 0.8333, 'LDPE': 0.75}},

    {'name': 'Sample 13/25/44', 'ratios': {'coconut': 0, 'rice': 1.0, 'walnut': 0, 'LDPE': 0}},
    {'name': 'Sample 14/30', 'ratios': {'coconut': 1.0, 'rice': 0, 'walnut': 0, 'LDPE': 0}},
    {'name': 'Sample 15/34', 'ratios': {'coconut': 0, 'rice': 0, 'walnut': 1.0, 'LDPE': 0}},
    {'name': 'Sample 16/29/42', 'ratios': {'coconut': 0, 'rice': 0, 'walnut': 0, 'LDPE': 1.0}},

    {'name': 'Sample 17/50/58', 'ratios': {'coconut': 0.25, 'rice': 0.25, 'walnut': 0.25, 'LDPE': 0.25}},

    {'name': 'Sample 18/26/69', 'ratios': {'coconut': 0, 'rice': 0.25, 'walnut': 0, 'LDPE': 0.75}},
    {'name': 'Sample 19/27/70', 'ratios': {'coconut': 0, 'rice': 0.50, 'walnut': 0, 'LDPE': 0.50}},
    {'name': 'Sample 20/28/43', 'ratios': {'coconut': 0, 'rice': 0.75, 'walnut': 0, 'LDPE': 0.25}},

    {'name': 'Sample 31', 'ratios': {'coconut': 0.75, 'rice': 0.25, 'walnut': 0, 'LDPE': 0}},
    {'name': 'Sample 32', 'ratios': {'coconut': 0.50, 'rice': 0.50, 'walnut': 0, 'LDPE': 0}},
    {'name': 'Sample 33', 'ratios': {'coconut': 0.25, 'rice': 0.75, 'walnut': 0, 'LDPE': 0}},

    {'name': 'Sample 35', 'ratios': {'coconut': 0, 'rice': 0.25, 'walnut': 0.75, 'LDPE': 0}},
    {'name': 'Sample 36', 'ratios': {'coconut': 0, 'rice': 0.50, 'walnut': 0.50, 'LDPE': 0}},
    {'name': 'Sample 37', 'ratios': {'coconut': 0, 'rice': 0.75, 'walnut': 0.25, 'LDPE': 0}},

    #{'name': 'Sample 56', 'ratios': {'coconut': 0, 'rice': 0.75, 'walnut': 0.25, 'LDPE': 0}},

    {'name': 'Sample 59', 'ratios': {'coconut': 0, 'rice': 0.40, 'walnut': 0.40, 'LDPE': 0.20}},
    {'name': 'Sample 60', 'ratios': {'coconut': 0, 'rice': 0.25, 'walnut': 0.50, 'LDPE': 0.25}},
    {'name': 'Sample 61', 'ratios': {'coconut': 0, 'rice': 0.50, 'walnut': 0.25, 'LDPE': 0.25}},
    {'name': 'Sample 62', 'ratios': {'coconut': 0.50, 'rice': 0.25, 'walnut': 0, 'LDPE': 0.25}},
    {'name': 'Sample 63', 'ratios': {'coconut': 0.40, 'rice': 0.40, 'walnut': 0, 'LDPE': 0.20}},
    {'name': 'Sample 64', 'ratios': {'coconut': 0.25, 'rice': 0.50, 'walnut': 0, 'LDPE': 0.25}},
    {'name': 'Sample 65', 'ratios': {'coconut': 0.20, 'rice': 0.60, 'walnut': 0, 'LDPE': 0.20}},
    {'name': 'Sample 66', 'ratios': {'coconut': 0, 'rice': 0.60, 'walnut': 0.25, 'LDPE': 0.20}},

    #{'name': 'Sample 67', 'ratios': {'coconut': 0, 'rice': 0.75, 'walnut': 0.25, 'LDPE': 0}},
    #{'name': 'Sample 68', 'ratios': {'coconut': 0, 'rice': 0.75, 'walnut': 0.25, 'LDPE': 0}},
    #{'name': 'Sample 71', 'ratios': {'coconut': 0, 'rice': 0.75, 'walnut': 0.25, 'LDPE': 0}},
    #{'name': 'Sample 72', 'ratios': {'coconut': 0, 'rice': 0.75, 'walnut': 0.25, 'LDPE': 0}},
]


# Calculate and print the ultimate analysis for each set of mixing ratios
for mixture in mixture_ratios_list:
    name = mixture['name']
    mixture_ratios = mixture['ratios']

    # Filter out components with 0 ratios
    non_zero_ratios = {key: value for key, value in mixture_ratios.items() if value > 0}

    # Format the ratio string
    ratio_str = ', '.join([f"{key}: {value * 100:.1f}%" for key, value in non_zero_ratios.items()])

    # Calculate ultimate analysis
    mixture_analysis = calculate_mixture_ultimate_analysis(mixture_ratios, coconut, rice, walnut, LDPE)

    # Format the output
    output = ', '.join([f"{element}: {value:.2f}%" for element, value in mixture_analysis.items()])

    print(f"{name} ({ratio_str}) => Ultimate Analysis: {output}")
