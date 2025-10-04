import pandas as pd
import numpy as np
import datetime
import random

# --- New: List of cosmic codenames ---
codename_list = [
    "Orion", "Andromeda", "Pulsar", "Quasar", "Nebula",
    "Supernova", "Pegasus", "Cygnus", "Draco", "Lyra",
    "Aquila", "Cassiopeia", "Hydra", "Centaurus", "Sirius"
]

# API call for detailed exoplanet data
api_url = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+pl_name,hostname,pl_letter,discoverymethod,disc_year,pl_orbper,pl_rade,pl_masse,sy_dist+from+ps&format=csv"

try:
    print("Fetching the latest 'supersized' data from NASA...")
    exoplanet_df = pd.read_csv(api_url)

    # Clean the data
    exoplanet_df.dropna(subset=['pl_name', 'discoverymethod', 'disc_year', 'pl_rade', 'pl_orbper'], inplace=True)
    
    # --- New: Version and Filename Generation ---
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M") # e.g., 20251004_0001
    version = f"v{timestamp}"
    codename = random.choice(codename_list)
    file_name = f"exoplanets_{version}_{codename}.csv"
    # --- End New ---

    # Save the new, versioned DataFrame to a CSV file
    exoplanet_df.to_csv(file_name, index=False)

    print(f"✅ Success! Created a new data file:")
    print(f"   --> {file_name}")
    print(f"   It contains {len(exoplanet_df)} confirmed planets.")
    print(f"   Data sourced from: https://exoplanetarchive.ipac.caltech.edu")

except Exception as e:
    print(f"An error occurred: {e}")