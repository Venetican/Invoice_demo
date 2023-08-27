# Preproccessing data script
# -*- coding: utf-8 -*-
# Transformation libraries
from pathlib import Path
import os
import pandas as pd
import xml.etree.ElementTree as ET

# Repo special scripts
from config_invoice import settings
from ddl_invoice import DfCreator
from logging_invoice import setup_logger

# Constants needed for data prep
APP = Path(settings.APP.REPO)
THIS_SCRIPT_NAME = settings.SCRIPTS.MAKE_DATASET_PY
RAW_DATA = APP / settings.SRC.DATA / settings.DATA.RAW
RAW_BOX_DATA = RAW_DATA / settings.DATA_STRUCTURE.BOX
RAW_ENTITIES_DATA = RAW_DATA / settings.DATA_STRUCTURE.ENTITIES
RAW_IMG_DATA = RAW_DATA / settings.DATA_STRUCTURE.IMG

# logger connection
logger = setup_logger(THIS_SCRIPT_NAME)

class TrDf:
    def __init__(
            self,
            df:pd.DataFrame
            ):
        self.df = df

    def get_file_path(
            self,
            folder_path: str
            ) -> pd.DataFrame:

        files_info = [
            (os.path.splitext(f)[0], f, os.path.join(folder_path, f))
            for f in os.listdir(folder_path) 
            if os.path.isfile(os.path.join(folder_path, f))
            ]

        df = pd.DataFrame(files_info,columns=self.df.columns) 
        return df
    
    def extract_all_xml(
            self
            ) -> pd.DataFrame:
        df = self.df
        tmp_dfs = []
        for index,row in df.iterrows():
            file_path = row['file_path_entities']
            id = row['id']
            tmp_df = HelpFunc.extract_one_xml(
                id,
                file_path,
                DfCreator.df_invoice_detail()
            )
            tmp_dfs.append(tmp_df)
        all_tmp_dfs = pd.concat(tmp_dfs, ignore_index=True)
        df = df.merge(all_tmp_dfs, on='id', how='left')
        return df

class TrDfst:
    def __init__(
            self,
            df_1:pd.DataFrame,
            df_2:pd.DataFrame
            ):
        self.df_1 = df_1
        self.df_2 = df_2

    def df_location_merge(
            self,
            df: pd.DataFrame):
        df_entry = pd.merge(
            self.df_1,
            self.df_2,
            how='inner',
            on='id',
        )
        df_entry.columns = df.columns
        df_entry =  df_entry.astype(df.dtypes.to_dict())
        return df_entry

class HelpFunc:
    def extract_one_xml(
            id: str,
            file_path: str, 
            df_structure: pd.DataFrame
            ) -> pd.DataFrame:
        xml_raw = ET.parse(file_path)
        root = xml_raw.getroot()
        # Extract information
        attributes_found = []
        for p_dh in root.findall(settings.INVOICE_ATTRIBUTES.P_DH):
            for child in p_dh:
                attributes_found.append(child.tag)
        df_tmp = pd.DataFrame(columns=df_structure.columns)
        for attribute in attributes_found:
            df_tmp.loc[0,attribute] = p_dh.find(attribute).text
        df_tmp.loc[0,'id'] = id
        df_tmp = df_tmp.astype(df_structure.dtypes.to_dict())
        return df_tmp

def main():
    # get img files
    df_img = TrDf(DfCreator.df_location()) \
            .get_file_path(RAW_IMG_DATA)
    # get entities files
    df_entities = TrDf(DfCreator.df_location()) \
            .get_file_path(RAW_ENTITIES_DATA)
    # merge all together
    df_entry = TrDfst(df_img,df_entities) \
            .df_location_merge(DfCreator.df_location_full())
    # Scrape all xmls
    df_xml = TrDf(df_entry).extract_all_xml()
