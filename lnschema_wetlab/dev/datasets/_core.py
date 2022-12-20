import numpy as np
import pandas as pd


def biosample():
    """Simple, dummy biosample example."""
    sample = pd.DataFrame(
        {
            "Name": [
                "hc_hea_021",
                "cv_acu_027",
                "cv_acu_010",
                "cv_con_049",
                "cv_rec_002",
            ],
            "Species": ["human", "human", "human", "human", "human"],
            "Cell Type": ["CD8+T", "CD8+T", "CD8+T", "CD8+T", "CD8+T"],
            "Experiment": ["001", "002", "003", "004", "004"],
            "Donor": ["021", "027", "010", "049", "002"],
            "Disease": [None, "U07.1", "U07.1", "U07.1", "U07.1"],
            "Custom 1": ["healthy", "acute", "acute", "convalescent", "recovered"],
            "Custom 2": ["control", "covid-19", "covid-19", "covid-19", "covid-19"],
            "Custom 3": [12.11, np.nan, 0.87, np.nan, 11.91],
        }
    )
    return sample


def techsample():
    """Simple, dummy techsample example."""
    sample = pd.DataFrame(
        {
            "Name": ["TS001", "TS002", "TS003", "TS004", "TS005"],
            "Batch": [1, 1, 1, 2, 2],
            "File Type": ["fastq", "fastq", "fastq", "fastq", "fastq"],
            "Filepath R1": [
                "SRX1603629_T1_1.fastq.gz",
                "SRX1603629_T1_2.fastq.gz",
                "SRX1603629_T1_3.fastq.gz",
                "SRX1603629_T1_4.fastq.gz",
                "SRX1603629_T1_5.fastq.gz",
            ],
            "Filepath R2": [
                "SRX1603629_T2_1.fastq.gz",
                "SRX1603629_T2_2.fastq.gz",
                "SRX1603629_T2_3.fastq.gz",
                "SRX1603629_T2_4.fastq.gz",
                "SRX1603629_T2_5.fastq.gz",
            ],
            "Custom 1": ["13.42%", "2.43%", "4.57%", np.nan, "9.36%"],
            "Custom 2": [
                "Gene Expression",
                "Gene Expression",
                "Gene Expression",
                "Gene Expression",
                "Gene Expression",
            ],
        }
    )
    return sample
