# Feedstock Mixture Ultimate Analysis Predictor

A Python script that predicts the theoretical ultimate analysis (C, H, N, O, S as % mass) of multi-feedstock biomass blends based on known elemental compositions and defined mass fractions.

## Author

**Nitish Kapur**<br>
GitHub: [github.com/nitish-kapur](https://github.com/nitish-kapur)

## How It Works

The script computes a weighted average of the elemental compositions of the constituent feedstocks based on their mass fractions. This is a theoretical prediction assuming ideal mixing — no chemical reactions or transformations are accounted for. It reflects the pre-reaction feedstock blend composition only.

## Feedstocks

The elemental compositions (C, H, N, O, S as % mass) for each feedstock are hard-coded as dictionaries at the top of the script. Update these values to match your own feedstocks and experimental data.

## Mixture Ratios

The sample mixtures and their mass fractions are defined in the `mixture_ratios_list`. Each entry contains a sample name and the mass fractions of each feedstock (values must sum to 1.0). Update, add, or remove entries to match your experimental design.

## Requirements

No external libraries are required. The script uses only Python built-ins.

## Usage

Run the script directly:

    python feedstock-mixture-ultimate-analysis.py

Results are printed to the console for each defined sample mixture.

## Output

For each sample, the console prints:

    Sample Name (feedstock: mass%) => Ultimate Analysis: C: x.xx%, H: x.xx%, N: x.xx%, O: x.xx%, S: x.xx%

Feedstocks with a mass fraction of zero are automatically excluded from the ratio string in the output.

## Notes

- This is a theoretical prediction based on ideal mixing — it does not account for any chemical transformations during pyrolysis or co-processing.
- Elemental compositions and mixture ratios are both hard-coded in the script. Update them to match your own feedstocks and experimental samples.
- Commented-out entries in `mixture_ratios_list` can be uncommented to include additional samples.
