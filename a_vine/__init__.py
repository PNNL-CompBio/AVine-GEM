import cobra
import pathlib
import pandas as pd


path = pathlib.Path(__file__).parent

model = cobra.io.read_sbml_model(
    path.joinpath('azo_vine.xml').__str__()
)

exp_file_path = path.joinpath('data', 'experiments.yml').__str__()
expected_metab = pd.read_csv(
    path.joinpath('data', 'excreted', 'metabolites.csv').__str__(),
).bigg_id

# expected_metab = ['EX_nh4_e']