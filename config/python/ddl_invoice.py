# Pandas df definitions
import pandas as pd

# Function which creates df relevant for initial df information
class DfCreator:
    def df_invoice_detail():
        # Attributes
        df = pd.DataFrame(
            columns={
                'id',
                'cf_do',
                'd_fak',
                'd_usk',
                'd_spl',
                'castk',
                'dan',
                'c_buc',
                'k_ban'
                }
        )

        # Attributes comments
        df.attrs['column_comments'] = {
            'id':      'unikátní identifikátor', 
            'cf_do':   'číslo faktury',
            'd_fak':   'vystavení',
            'd_usk':   'zdanitelné pnění',
            'd_spl':   'splatnost',
            'castk':   'částka celkem',
            'dan':     'daň',
            'c_buc':   'účet',
            'k_ban':   'banka',
            }

        # Attributes dtypes
        df_column_types = {
            'id':     'object',
            'cf_do':  'object',
            'd_fak':  'datetime64',
            'd_usk':  'datetime64',
            'd_spl': 'datetime64',
            'castk': 'float64',
            'dan': 'float64',
            'c_buc': 'int',
            'k_ban': 'int',
            }

        # Casting to proper dtypes
        df = df.astype(df_column_types)

        # Proper column order
        df = df[[
            'id',
            'cf_do',
            'd_fak',
            'd_usk',
            'd_spl',
            'castk',
            'dan',
            'c_buc',
            'k_ban'
        ]]
        return df
    
    def df_location():
        # Attributes
        df = pd.DataFrame(
            columns={
                'id',
                'file_name',
                'file_path'
                }
        )

        # Attributes comments
        df.attrs['column_comments'] = {
            'id' : 'unikátní identifikátor faktury',
            'file_name' : 'jméno souboru',
            'file_path' : 'cesta k souboru'
        }

        # Attributes dtypes
        df_column_types = {
            'id' : 'object',
            'file_name': 'object',
            'file_path': 'object'
        }

        # Casting to proper dtypes
        df = df.astype(df_column_types)

        # Proper column order
        df = df[[
            'id',
            'file_name',
            'file_path'
        ]]
        return df
    
    def df_location_full():
        # Attributes
        df = pd.DataFrame(
            columns={
                'id',
                'file_name_img',
                'file_path_img',
                'file_name_entities',
                'file_path_entities',
                }
        )

        # Attributes comments
        df.attrs['column_comments'] = {
            'id' : 'unikátní identifikátor faktury',
            'file_name_img' : 'jméno souboru fotka',
            'file_path_img' : 'cesta k souboru fotka',
            'file_name_entities' : 'jméno souboru entity',
            'file_path_entities' : 'cesta k souboru entity'
        }

        # Attributes dtypes
        df_column_types = {
            'id' : 'object',
            'file_name_img': 'object',
            'file_path_img': 'object',
            'file_name_entities' : 'object',
            'file_path_entities' : 'object'
        }

        # Casting to proper dtypes
        df = df.astype(df_column_types)

        # Proper column order
        df = df[[
            'id',
            'file_name_img',
            'file_path_img',
            'file_name_entities',
            'file_path_entities'
        ]]
        return df
