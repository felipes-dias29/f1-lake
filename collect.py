# %%

import fastf1
import pandas as pd

# %%

class CollectResults:

    def __init__(self, years=[2021,2022,2023,2024,2025], modes=["R", "S"]):
        self.years = years
        self.modes = modes

    def get_data(self, year, gp, mode) -> pd.DataFrame:
        session = fastf1.get_session(year, gp, mode)
        session._load_drivers_results()
        return session.results